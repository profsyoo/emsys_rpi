#define FINAL //seyoo, Gemini
#ifdef FINAL
/*
 * DHT11 Sensor Reading for Raspberry Pi 5
 * Optimized with Threshold 20 based on real-time debug counts
 * Compile: gcc -Wall -o dht11_final dht11_final.c -llgpio
 * Run: sudo ./dht11_final
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>
#include <lgpio.h>

#define DHTPIN 4          // BCM 4 (WiringPi pin 7)
#define MAXTIMINGS 85

int read_dht11(int handle) {
    int data[5] = {0, 0, 0, 0, 0};
    uint32_t laststate = LG_HIGH;
    uint32_t counter = 0;
    int j = 0, i;

    /* 1. Send Start Signal to DHT11 */
    lgGpioClaimOutput(handle, LG_SET_PULL_UP, DHTPIN, LG_HIGH);
    usleep(200000);       // Wait for sensor stability
    lgGpioWrite(handle, DHTPIN, LG_LOW);
    usleep(18000);        // Pull down for 18ms
    lgGpioWrite(handle, DHTPIN, LG_HIGH);
    
    /* 2. Switch to Input Mode to Receive Data */
    lgGpioClaimInput(handle, LG_SET_PULL_UP, DHTPIN);

    /* 3. Read Data Bits */
    for (i = 0; i < MAXTIMINGS; i++) {
        counter = 0;
        while (lgGpioRead(handle, DHTPIN) == laststate) {
            counter++;
            if (counter == 1000) break; 
        }
        laststate = lgGpioRead(handle, DHTPIN);

        if (counter == 1000) break;

        /* Skip first 3 transitions and process only High pulses */
        if ((i >= 4) && (i % 2 == 0)) {
            data[j / 8] <<= 1;
            /* * Threshold 20: 
             * Bit '0' is ~10 counts, Bit '1' is ~38 counts on Pi 5 
             */
            if (counter > 20) 
                data[j / 8] |= 1;
            j++;
        }
    }

    /* 4. Release GPIO pin */
    lgGpioFree(handle, DHTPIN);

    /* 5. Checksum Verification & Result Output */
    if ((j >= 40) && (data[4] == ((data[0] + data[1] + data[2] + data[3]) & 0xFF))) {
        printf("Humidity = %d.%d %% Temperature = %d.%d °C\n", 
                data[0], data[1], data[2], data[3]);
        return 1;
    } 
    
    return 0; // Return 0 on Checksum/Timing error
}

int main(void) {
    int handle;

    printf("Starting DHT11 Reader for Raspberry Pi 5...\n");
    printf("Press Ctrl+C to stop.\n");

    handle = lgGpiochipOpen(0);
    if (handle < 0) {
        fprintf(stderr, "Error: Could not open lgpio chip.\n");
        return 1;
    }

    while (1) {
        if (!read_dht11(handle)) {
            // Optional: Notify user on failure (useful for troubleshooting)
            // printf("Read failed, retrying...\n");
            usleep(500000); 
        } else {
            sleep(2); // DHT11 needs at least 2s between readings
        }
    }

    lgGpiochipClose(handle);
    return 0;
}
#else
/*
 * DHT11 Sensor Reading for Raspberry Pi 5
 * Debug version to find the perfect threshold
 * Compile: gcc -Wall -o dht11_debug dht11_pi5_debug.c -llgpio
 * Run: sudo ./dht11_debug
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>
#include <lgpio.h>

#define DHTPIN 4
#define MAXTIMINGS 85

void read_dht11(int handle) {
    int data[5] = {0, 0, 0, 0, 0};
    uint32_t laststate = LG_HIGH;
    uint32_t counter = 0;
    uint32_t counts[40]; // To store counter values for 40 bits
    int j = 0, i;

    /* 1. Start Signal */
    lgGpioClaimOutput(handle, LG_SET_PULL_UP, DHTPIN, LG_HIGH);
    usleep(200000); 
    lgGpioWrite(handle, DHTPIN, LG_LOW);
    usleep(18000); 
    lgGpioWrite(handle, DHTPIN, LG_HIGH);
    
    /* 2. Switch to Input */
    lgGpioClaimInput(handle, LG_SET_PULL_UP, DHTPIN);

    /* 3. Read loop */
    for (i = 0; i < MAXTIMINGS; i++) {
        counter = 0;
        while (lgGpioRead(handle, DHTPIN) == laststate) {
            counter++;
            if (counter == 2000) break; 
        }
        laststate = lgGpioRead(handle, DHTPIN);

        if (counter == 2000) break;

        /* * Final Adjustment for Raspberry Pi 5 
         * Threshold logic updated based on your raw counts (10 vs 38)
         */

        if ((i >= 4) && (i % 2 == 0)) {
            data[j / 8] <<= 1;
            
            /* * Based on your debug output:
             * Bit 0 is around 10 counts.
             * Bit 1 is around 35 counts.
             * So, 20 is the perfect divider.
             */
            if (counter > 20) 
                data[j / 8] |= 1;
            j++;
        }
    }

    lgGpioFree(handle, DHTPIN);

    /* 4. Checksum and Output */
    if ((j >= 40) && (data[4] == ((data[0] + data[1] + data[2] + data[3]) & 0xFF))) {
        printf("SUCCESS! Humidity = %d.%d %% Temperature = %d.%d *C\n", 
                data[0], data[1], data[2], data[3]);
    } else {
        printf("READ FAILED. Bits: %d. Showing raw counts:\n", j);
        for(int n=0; n<j; n++) {
            printf("%d ", counts[n]); // Look at these numbers!
            if ((n+1)%8 == 0) printf("| ");
        }
        printf("\n");
    }
}

int main(void) {
    int handle = lgGpiochipOpen(0);
    if (handle < 0) return 1;

    printf("Starting DHT11 Debugger...\n");
    while (1) {
        read_dht11(handle);
        sleep(3);
    }
    lgGpiochipClose(handle);
    return 0;
}
#endif
