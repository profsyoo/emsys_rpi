import time
import RPi.GPIO as GPIO

def increase(pwm):
    print("increase the light")
    # Loop for 5 seconds (100 steps * 0.05s)
    for value in range(0, 100): 
        pwm.ChangeDutyCycle(value)
        time.sleep(0.05)

def decrease(pwm):
    print("decrease the light")
    # Loop for 5 seconds (100 steps * 0.05s)
    for value in range(99, -1, -1): 
        pwm.ChangeDutyCycle(value)
        time.sleep(0.05)

# Set GPIO pin numbering to BCM mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 6 # Connect LED to GPIO 6
GPIO.setup(led, GPIO.OUT) # Set GPIO 6 as an output pin

GPIO.output(led, GPIO.LOW) # Initial output set to 0V
pwm = GPIO.PWM(led, 100)   # Initialize PWM on GPIO 6 at 100Hz frequency
pwm.start(0)               # Start PWM with a duty cycle of 0%

try:
    while True:
        # Increase duty cycle over 5s: makes LED gradually brighter
        increase(pwm) 
        # Decrease duty cycle over 5s: makes LED gradually dimmer
        decrease(pwm) 
except KeyboardInterrupt:
    # Handle clean exit on Ctrl+C
    pwm.stop()
    GPIO.cleanup()
