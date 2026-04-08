import lgpio
import time

PIN = 21
# For Raspberry Pi 5, chip ID 0 or 4 is commonly used.
CHIP_ID = 0 

def my_callback(chip, gpio, level, timestamp):
    time.sleep(0.1)    
    print(f"Edge detected on GPIO {gpio} at {timestamp} (Level: {level})")

handle = lgpio.gpiochip_open(CHIP_ID)

# Configure alert settings and connect the callback function
lgpio.gpio_claim_alert(handle, PIN, lgpio.RISING_EDGE,  lgpio.SET_PULL_DOWN)
lgpio.callback(handle, PIN, lgpio.RISING_EDGE, my_callback)

print("Waiting for events... Press Ctrl+C to stop.")

try:
    while True:
        time.sleep(1)  # Main loop only needs to wait.
except KeyboardInterrupt:
    pass
finally:
    lgpio.gpiochip_close(handle)
