import time
import board
import adafruit_dht

# When connected to GPIO pin 4 (change to any pin if needed)
# On Raspberry Pi 5, specify the pin as board.D4, etc.
sensor = adafruit_dht.DHT11(board.D4)

print("--- Starting DHT11 sensor reading ---")

try:
    while True:
        try:
            # Read temperature and humidity data
            temperature_c = sensor.temperature
            humidity = sensor.humidity

            if temperature_c is not None and humidity is not None:
                print(f"Temperature: {temperature_c:.1f}°C | Humidity: {humidity}%")

        except RuntimeError as error:
            # DHT sensors often produce read errors, so keep trying
            print(f"Read error: {error.args[0]}")
            time.sleep(2.0)
            continue

        except Exception as error:
            sensor.exit()
            raise error

        # DHT11 requires a minimum delay of 2 seconds between readings
        time.sleep(2.0)

except KeyboardInterrupt:
    print("\nProgram terminated")

finally:
    sensor.exit()
