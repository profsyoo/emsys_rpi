import time
import lgpio

BUZZER = 22                         # BCM GPIO22 (wiringPi pin 15 equivalent)

print("Welcome to Elecrow")
print("Raspberry Pi Passive Buzzer test program (lgpio)")
print("Press Ctrl+C to exit")

h = lgpio.gpiochip_open(0)          # Open gpiochip0
lgpio.gpio_claim_output(h, BUZZER)  # Configure BUZZER pin as output

try:
    while True:
        for i in range(80):         # Output first frequency sound
            lgpio.gpio_write(h, BUZZER, 1)  # Sound ON
            time.sleep(0.001)       # 1 ms delay
            lgpio.gpio_write(h, BUZZER, 0)  # Sound OFF
            time.sleep(0.001)       # 1 ms delay

        for j in range(100):        # Output second frequency sound
            lgpio.gpio_write(h, BUZZER, 1)  # Sound ON
            lgpio.gpio_write(h, BUZZER, 0)  # Sound OFF
            time.sleep(0.002)       # 2 ms delay

except KeyboardInterrupt:
    pass

finally:
    lgpio.gpiochip_close(h)         # Release GPIO resources
