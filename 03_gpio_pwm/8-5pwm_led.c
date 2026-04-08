/*
*not tested yet.
gcc wm_led.c -o 8-5pwm_led -llgpio
sudo ./pwm_led
  */

#include <stdio.h>
#include <unistd.h>     // usleep
#include <lgpio.h>

#define PIN 6           // GPIO pin number
#define FREQ 1000       // PWM frequency (Hz)

int main(void)
{
    int chip;
    int duty;

    // GPIO chip 0 열기
    chip = lgpio_gpiochip_open(0);
    if (chip < 0) {
        printf("Failed to open gpio chip\n");
        return 1;
    }

    // GPIO 출력으로 설정
    if (lgpio_gpio_claim_output(chip, 0, PIN, 0) < 0) {
        printf("Failed to claim GPIO %d\n", PIN);
        lgpio_gpiochip_close(chip);
        return 1;
    }

    // PWM duty cycle 증가
    for (duty = 0; duty <= 100; duty += 10) {
        lgpio_tx_pwm(chip, PIN, FREQ, duty);
        usleep(500000);   // 0.5초
    }

    // PWM 중지
    lgpio_tx_pwm(chip, PIN, 0, 0);

    // GPIO chip 닫기
    lgpio_gpiochip_close(chip);

    return 0;
}
