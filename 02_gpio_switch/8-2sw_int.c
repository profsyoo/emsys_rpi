/* GPIO Edge Detection (Interrupt) for Raspberry Pi 5
* Compile: gcc -Wall -o switch_int switch_int.c -llgpio
 * Run: sudo ./switch_int    */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <lgpio.h>

#define PIN 21
#define CHIP_ID 0
int chip_handle;

/* callback function signature */
/* The second argument must be a pointer to lgGpioAlert_t structure */
void my_callback(int chip, lgGpioAlert_t *alert, void *userdata) {
    /* Extracting data from the alert structure */
    int gpio = alert->report.gpio;
    int level = alert->report.level;
    uint64_t timestamp = alert->report.timestamp;

    /* Small delay as requested (0.1s) */
    usleep(100000); 
    
    printf("Edge detected on GPIO %d at %llu (Level: %d)\n", 
            gpio, (unsigned long long)timestamp, level);
}

/* Cleanup function for safe exit */
void handle_sigint(int sig) {
    printf("\nCleaning up and exiting...\n");
    lgGpiochipClose(chip_handle);
    exit(0);
}

int main(void) {
    /* Set up signal handler for Ctrl+C */
    signal(SIGINT, handle_sigint);

    /* 1. Open the GPIO chip */
    chip_handle = lgGpiochipOpen(CHIP_ID);
    if (chip_handle < 0) {
        fprintf(stderr, "Error: Could not open gpiochip %d\n", CHIP_ID);
        return 1;
    }

    /* 2. Configure the pin for rising edge alerts */
    if (lgGpioClaimAlert(chip_handle, LG_SET_PULL_DOWN, LG_RISING_EDGE, PIN, -1) < 0) {
        fprintf(stderr, "Error: Could not claim alert for GPIO %d\n", PIN);
        lgGpiochipClose(chip_handle);
        return 1;
    }

    /* 3. Register the alert function with the correct signature */
    if (lgGpioSetAlertsFunc(chip_handle, PIN, my_callback, NULL) < 0) {
        fprintf(stderr, "Error: Could not set alert function\n");
        lgGpiochipClose(chip_handle);
        return 1;
    }

    printf("Waiting for events on GPIO %d... Press Ctrl+C to stop.\n", PIN);

    /* 4. Main loop */
    while (1) {
        sleep(1); 
    }

    return 0;
}
