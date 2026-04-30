
import time
import lgpio

BUZZER = 13                              # BCM GPIO13 (Passive buzzer)

h = lgpio.gpiochip_open(0)               # Open gpiochip0
lgpio.gpio_claim_output(h, BUZZER)        # Set BUZZER as output


def beep(freq, duration):                # Generate sound with given frequency
    period = 1.0 / freq
    cycles = int(freq * duration)

    for _ in range(cycles):
        lgpio.gpio_write(h, BUZZER, 1)
        time.sleep(period / 2)
        lgpio.gpio_write(h, BUZZER, 0)
        time.sleep(period / 2)


INIT_DIST = 100
dist = INIT_DIST
try:
    while True:
        dist = dist - 5
        time.sleep(0.3)
      
        if dist > 50:                     # Far distance
            time.sleep(0.3)               # Long silent interval

        elif 30 < dist <= 50:             # Medium distance
            beep(800, 0.05)               # Low frequency beep
            time.sleep(0.3)

        elif 15 < dist <= 30:             # Close distance
            beep(1200, 0.05)              # Higher frequency
            time.sleep(0.15)

        else:                             # Very close
            beep(2000, 0.1)               # Continuous high pitch
            time.sleep(0.05)
          
        if dist <= 0:
            dist = INIT_DIST
            

except KeyboardInterrupt:
    pass

finally:
    lgpio.gpiochip_close(h)               # Release GPIO resources
