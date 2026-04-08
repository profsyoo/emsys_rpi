/*
 * Read a switch input (lgpio) - C version of the given Python code
 *
 * Behavior:
 *  - Reads GPIO21 repeatedly.
 *  - Prints "Pressed" if value == 0, else "Released".
 *  - Sleeps 0.1 seconds between reads.
 *
 * Build:
 *   gcc -Wall -O2 -o sw_read sw_read.c -llgpio
 *
 * Run:
 *   sudo ./sw_read
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <lgpio.h>

#define PIN     21
#define CHIP_ID 0

static int chip = -1;

/* Clean exit on Ctrl+C */
static void handle_sigint(int sig)
{
    (void)sig; /* Intentionally unused */
    printf("\nExiting...\n");
    if (chip >= 0) lgGpiochipClose(chip);
    exit(0);
}


int main(void)
{
    signal(SIGINT, handle_sigint);

    /* Open gpiochip 0 */
    chip = lgGpiochipOpen(CHIP_ID);
    if (chip < 0) {
        fprintf(stderr, "Error: Could not open gpiochip %d\n", CHIP_ID);
        return 1;
    }

    /* Claim GPIO as input (no internal pull specified, same as the Python code) */
    if (lgGpioClaimInput(chip, LG_SET_PULL_DOWN, PIN) < 0) {
        fprintf(stderr, "Error: Could not claim GPIO %d as input\n", PIN);
        lgGpiochipClose(chip);
        return 1;
    }

    while (1) {
        int v = lgGpioRead(chip, PIN);
        if (v < 0) {
            /* Read error */
            fprintf(stderr, "Error: Failed to read GPIO %d\n", PIN);
        } else {
            printf("%s\n", (v == 0) ? "Released" : "Pressed");
            fflush(stdout);
        }

        /* 0.1 seconds = 100 ms */
        usleep(100000);
    }

    /* Unreachable */
    lgGpiochipClose(chip);
    return 0;
}
