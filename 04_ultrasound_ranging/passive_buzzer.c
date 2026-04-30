/*
 * Converted to lgpio version
 * Original author: keen
 * Modified for lgpio
 * Compile : gcc -o passive_buz passive_buz.c -llgpio
 * Run     : sudo ./passive_buz
 */

#include <stdio.h>
#include <unistd.h>        // usleep()
#include <lgpio.h>

#define BUZZER 22          // BCM GPIO22 (wiringPi pin 15)

int main(void)
{
    int h;                // GPIO chip handle

    printf("Welcome to Elecrow\n");
    printf("Raspberry Pi Passive Buzzer test program (lgpio)\n");
    printf("Press Ctrl+C to exit\n");

    h = gpiochip_open(0);                     // Open gpiochip0
    gpio_claim_output(h, BUZZER, 0);           // Set BUZZER pin as output

    while (1)
    {
        for (int i = 0; i < 80; i++)           // Output frequency sound
        {
            gpio_write(h, BUZZER, 1);          // Sound ON
            usleep(1000);                      // 1 ms delay
            gpio_write(h, BUZZER, 0);          // Sound OFF
            usleep(1000);                      // 1 ms delay
        }

        for (int j = 0; j < 100; j++)          // Output another frequency
        {
            gpio_write(h, BUZZER, 1);          // Sound ON
            gpio_write(h, BUZZER, 0);          // Sound OFF
            usleep(2000);                      // 2 ms delay
        }
    }

    gpiochip_close(h);                         // Release GPIO resources
    return 0;
}
