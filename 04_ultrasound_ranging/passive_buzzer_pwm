import time
import lgpio

BUZZER = 13                             # BCM GPIO13

h = lgpio.gpiochip_open(0)              # Open gpiochip0
lgpio.gpio_claim_output(h, BUZZER)      # Claim GPIO as output

try:
    while True:
        for freq in range(500, 5000, 250):
            print("freq = ", freq)
            lgpio.tx_pwm(h, BUZZER, freq, 0.5)  # 1 kHz tone, 50% duty
            time.sleep(1)

        lgpio.tx_pwm(h, BUZZER, 0, 0)       # Stop sound
        time.sleep(2)

except KeyboardInterrupt:
    pass

finally:
    lgpio.gpiochip_close(h)

