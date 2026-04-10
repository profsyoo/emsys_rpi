
import time
import RPi.GPIO as GPIO

# Function to turn the LED on or off by outputting value (0/1) to the LED-connected pin
def led_on_off(pin, value):
    GPIO.output(pin, value)

GPIO.setmode(GPIO.BCM)      # Operate in BCM mode
GPIO.setwarnings(False)    # Disable warning messages

led = 6                    # GPIO6 pin
GPIO.setup(led, GPIO.OUT)  # Set GPIO6 pin as output

button = 21                # GPIO21 pin
# Set GPIO21 pin as input and enable pull-down resistor
GPIO.setup(button, GPIO.IN, GPIO.PUD_DOWN)

print("The LED turns on while the switch is pressed and turns off when released.")

try:
    while True:
        status = GPIO.input(button)   # Read digital value (0/1) from GPIO21 pin
        led_on_off(led, status)       # Output the read value (0/1) to the LED (GPIO6 pin)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
