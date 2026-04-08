import lgpio
import time

PIN = 6
chip = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(chip, PIN)

for duty in range(0, 101, 10):
    lgpio.tx_pwm(chip, PIN, 1000, duty)
    time.sleep(0.5)

lgpio.tx_pwm(chip, PIN, 0, 0)   # PWM 중지
lgpio.gpiochip_close(chip)
