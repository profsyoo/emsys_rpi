/*
 * Converted to lgpio version
 * Original author: keen
 * Modified for lgpio
 * Compile : gcc -o passive_buz passive_buz.c -llgpio
 * Run     : sudo ./passive_buz
 */

#include <stdio.h>
#include <stdlib.h>         //exit()
#include <unistd.h>        // usleep()
#include <signal.h>
#include <lgpio.h>

#define BUZZER 13          // BCM GPIO13

int chip_handle;

/* Cleanup function for safe exit */
void handle_sigint(int sig) {
    printf("\nCleaning up and exiting...\n");
    lgGpiochipClose(chip_handle);
    exit(0);
}

int main(void)
{
    int h;                // GPIO chip handle

    /* Set up signal handler for Ctrl+C */
    signal(SIGINT, handle_sigint);
    
    printf("Welcome to Elecrow\n");
    printf("Raspberry Pi Passive Buzzer test program (lgpio)\n");
    printf("Press Ctrl+C to exit\n");

    chip_handle = lgGpiochipOpen(0);                     // Open gpiochip0
    h = chip_handle;
    lgGpioClaimOutput(h, 0, BUZZER, 0);           // Set BUZZER pin as output

    while (1)
    {
        for (int i = 0; i < 80; i++)           // Output frequency sound
        {
            lgGpioWrite(h, BUZZER, 1);          // Sound ON
            usleep(1000);                      // 1 ms delay
            lgGpioWrite(h, BUZZER, 0);          // Sound OFF
            usleep(1000);                      // 1 ms delay
        }

        for (int j = 0; j < 100; j++)          // Output another frequency
        {
            lgGpioWrite(h, BUZZER, 1);          // Sound ON
            lgGpioWrite(h, BUZZER, 0);          // Sound OFF
            usleep(2000);                      // 2 ms delay
        }
    }

    lgGpiochipClose(h);                         // Release GPIO resources
    return 0;
}
