import time
import lgpio

# Configuration
LED = 6
chip = lgpio.gpiochip_open(0)

# Claim the GPIO pin for output
lgpio.gpio_claim_output(chip, LED)

try:
    while True:
        # Turn LED ON
        lgpio.gpio_write(chip, LED, 1)
        time.sleep(0.5)
        
        # Turn LED OFF
        lgpio.gpio_write(chip, LED, 0)
        time.sleep(0.5)

except KeyboardInterrupt:
    # Cleanup on exit
    print("\nProgram stopped by user")
    lgpio.gpio_write(chip, LED, 0)
    lgpio.gpiochip_close(chip)
