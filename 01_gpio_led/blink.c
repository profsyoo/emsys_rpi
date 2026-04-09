/*blink.c
$gcc –o blink_led blink.c -llgpio
*/
#include <stdio.h>
#include <unistd.h>
#include <lgpio.h>

#define LED_PIN  6
#define CHIP_NUM  0

int main(void) {
    int h = lgGpiochipOpen(CHIP_NUM);
    if (h < 0) return 1;

    lgGpioClaimOutput(h, 0, LED_PIN, 0);

    for (int i = 0; i < 10; i++) {
        lgGpioWrite(h, LED_PIN, 1);
        usleep(500000);
        lgGpioWrite(h, LED_PIN, 0);
        usleep(500000);
    }

    lgGpiochipClose(h);
    return 0;
}
