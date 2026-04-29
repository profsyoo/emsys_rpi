#lgpio module rather than R
import time
import lgpio

def measureDistance(h, trig, echo):
    time.sleep(0.2)                          # Mandatory 200 ms delay for sensor stabilization

    lgpio.gpio_write(h, trig, 1)             # Set TRIG pin HIGH
    time.sleep(0.00001)                      # Keep HIGH pulse for 10 microseconds
    lgpio.gpio_write(h, trig, 0)             # Set TRIG pin LOW (trigger ultrasonic burst)

    while lgpio.gpio_read(h, echo) == 0:     # Wait until ECHO goes HIGH
        pass

    pulse_start = time.time()                # Record start time

    while lgpio.gpio_read(h, echo) == 1:     # Wait until ECHO goes LOW
        pass

    pulse_end = time.time()                  # Record end time
    pulse_duration = pulse_end - pulse_start # Calculate pulse duration

    return pulse_duration * 340 * 100 / 2    # Distance in cm


TRIG = 20                                   # GPIO20 (BCM)
ECHO = 16                                   # GPIO16 (BCM)

h = lgpio.gpiochip_open(0)                  # Open gpiochip0

lgpio.gpio_claim_output(h, TRIG)            # Configure TRIG as output
lgpio.gpio_claim_input(h, ECHO)             # Configure ECHO as input

try:
    while True:
        distance = measureDistance(h, TRIG, ECHO)  # Measure distance
        print("The distance to the object is %.2f cm." % distance)
        time.sleep(0.5)                     # Measure every 0.5 seconds

except KeyboardInterrupt:
    pass

finally:
    lgpio.gpiochip_close(h)                 # Release GPIO resources
