/*
*not tested yet.
gcc pwm_led.c -o 8-5pwm_led -llgpio
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
    chip = lgGpiochipOpen(0);
    if (chip < 0) {
        printf("Failed to open gpio chip\n");
        return 1;
    }

    // GPIO 출력으로 설정
    if (lgGpioClaimOutput(chip, 0, PIN, 0) < 0) {
        printf("Failed to claim GPIO %d\n", PIN);
        lgGpiochipClose(chip);
        return 1;
    }

    // PWM duty cycle 증가
    // check /usr/include/lgpio.h
    /*int lgTxPwm(                 
       int handle,               
       int gpio,                 
       float pwmFrequency,       
       float pwmDutyCycle,
       int pwmOffset,
       int pwmCycles);           
   
        handle: >= 0 (as returned by [*lgGpiochipOpen*])
        gpio: the GPIO to be pulsed
        pwmFrequency: PWM frequency in Hz (0=off, 0.1-10000)
        pwmDutyCycle: PWM duty cycle in % (0-100)
        pwmOffset: offset from nominal pulse start position
        pwmCycles: the number of pulses to be sent, 0 for infinite
*/

    for (duty = 0; duty <= 100; duty += 10) {
        lgTxPwm(chip, PIN, 1000, duty, 0, 0);
        usleep(500000);   // 0.5초
    }

    // PWM 중지
    lgTxPwm(chip, PIN, 0, 0, 0, 0);

    // GPIO chip 닫기
    lgGpiochipClose(chip);

    return 0;
}
