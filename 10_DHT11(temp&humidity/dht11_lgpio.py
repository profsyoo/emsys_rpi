#translated by Gemini
import time
import lgpio

# Configuration
DHT_PIN = 4
CHIP_ID = 0

def read_dht11(handle):
    # 1. Send Start Signal
    # Using claim_output with level 1 initially for stability
    lgpio.gpio_claim_output(handle, DHT_PIN)
    lgpio.gpio_write(handle, DHT_PIN, 0)
    time.sleep(0.018)  # 18ms Pull down
    lgpio.gpio_write(handle, DHT_PIN, 1)
    
    # 2. Quickly Switch to Input mode
    lgpio.gpio_claim_input(handle, DHT_PIN)
    
    # 3. High-speed sampling
    # We record timestamps of state changes for better precision than loop counts
    # lgpio.gpio_read is fast, but Python's list append adds overhead
    max_unchanged_count = 1000
    unchanged_count = 0
    last_state = -1
    times = []
    
    start_time = time.time()
    while (time.time() - start_time) < 0.1: # Max 100ms total sampling
        current_state = lgpio.gpio_read(handle, DHT_PIN)
        if current_state != last_state:
            times.append(time.time())
            last_state = current_state
            unchanged_count = 0
        else:
            unchanged_count += 1
        
        if unchanged_count > max_unchanged_count:
            break
        if len(times) >= 85:
            break

    # 4. Filter and Process pulses
    # We need at least 40 bits (80 transitions) + header transitions
    if len(times) < 80:
        return None, None

    # Calculate durations of HIGH pulses
    # HIGH pulses start at index 3, 5, 7... and end at 4, 6, 8...
    durations = []
    for i in range(3, len(times) - 1, 2):
        durations.append(times[i+1] - times[i])

    if len(durations) < 40:
        return None, None

    # 5. Adaptive Thresholding
    # DHT11 '0' is ~26us, '1' is ~70us. 
    # Python overhead makes absolute time tricky, so we find the midpoint.
    d_min = min(durations)
    d_max = max(durations)
    threshold = (d_min + d_max) / 2

    binary_data = [0] * 5
    for i in range(40):
        binary_data[i // 8] <<= 1
        if durations[i] > threshold:
            binary_data[i // 8] |= 1

    # 6. Checksum Verification
    if (binary_data[4] == ((binary_data[0] + binary_data[1] + binary_data[2] + binary_data[3]) & 0xFF)):
        return binary_data[0], binary_data[2] # Humidity, Temperature
    else:
        # Debug: Print threshold info if needed
        # print(f"Debug: Min={d_min:.6f} Max={d_max:.6f} Thres={threshold:.6f}")
        return None, None

# Main Loop
handle = lgpio.gpiochip_open(CHIP_ID)
print("--- Starting DHT11 Adaptive Reader (lgpio) ---")

try:
    while True:
        humidity, temperature = read_dht11(handle)
        if humidity is not None:
            print(f"Temperature: {temperature}.0°C | Humidity: {humidity}.0%")
            time.sleep(2.0)
        else:
            # DHT11 often needs a short break after a failed read
            time.sleep(0.5) 

except KeyboardInterrupt:
    print("\nInterrupted by user")
finally:
    lgpio.gpiochip_close(handle)
