import RPi.GPIO as GPIO
import time

# Callback function called when the button is pressed
def button_pressed(channel):
    print("Switch connected to pin %d pressed" % channel)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button = 21  # GPIO21
GPIO.setup(button, GPIO.IN, GPIO.PUD_DOWN)

# Set to call button_pressed() after 10 ms debounce when the button is pressed
GPIO.add_event_detect(button, GPIO.RISING, button_pressed, bouncetime=10)

try:
    while True:
        pass  # The user can write other required tasks here
finally:
    GPIO.cleanup()
