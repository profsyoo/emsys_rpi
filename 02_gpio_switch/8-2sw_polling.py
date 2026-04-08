import time
import lgpio

PIN = 21
chip = lgpio.gpiochip_open(0)
lgpio.gpio_claim_input(chip, PIN, lgpio.SET_PULL_DOWN)

try:
    while True:
        v = lgpio.gpio_read(chip, PIN)
        print("Released" if v == 0 else "Pressed")
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    lgpio.gpiochip_close(chip)
