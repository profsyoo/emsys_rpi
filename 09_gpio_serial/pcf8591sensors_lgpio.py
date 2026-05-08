#lgpio version
import time
import lgpio


# ===== 사용자 보정값 =====
VCC = 3.3
R_FIXED = 10000  # 10kΩ

# LDR 경험식 계수 (대략값)
A = 500000
GAMMA = 1.4


def setup(addr):
    global address
    address = addr                             # Store PCF8591 I2C address

def read(chn):                                 # Read ADC channel
    try:
        if chn == 0:
            lgpio.i2c_write_byte(h, 0x40)      # Select AIN0
        if chn == 1:
            lgpio.i2c_write_byte(h, 0x41)      # Select AIN1
        if chn == 2:
            lgpio.i2c_write_byte(h, 0x42)      # Select AIN2
        if chn == 3:
            lgpio.i2c_write_byte(h, 0x43)      # Select AIN3

        lgpio.i2c_read_byte(h)                 # Dummy read to start conversion

    except Exception as e:
        print("Address: 0x%02X" % address)     # Print device address
        print(e)

    return lgpio.i2c_read_byte(h)              # Return ADC value

def write(val):                                # Write DAC output
    try:
        temp = int(val)                        # Convert value to integer
        lgpio.i2c_write_byte_data(h, 0x40, temp)  # Write DAC value
    except Exception as e:
        print("Error: Device address: 0x%02X" % address)
        print(e)

def adc_to_voltage(adc):
    return adc / 255.0 * VCC

def voltage_to_resistance(v):
    """
    센서가 GND쪽에 있는 분압회로 기준
    """
    if v <= 0:
        return 9999999

    return R_FIXED * v / (VCC - v)

def resistance_to_lux(r):
    """
    매우 대략적 lux 근사
    R = A * Lux^-gamma
    """
    lux = (A / r) ** (1.0 / GAMMA)
    return lux

if __name__ == "__main__":

    #check your PCF8591 address by type in 'i2cdetect -y -1' in terminal.
    #check your PCF8591 address by type in 'i2cdetect -y 1' in terminal.
    address = 0x48                              # PCF8591 I2C address
    setup(address)

    h = lgpio.i2c_open(1, address)              # Open I2C bus 1, slave address

    try:
        while True:
            print("AIN0 =", read(0))            # Read channel 0
            print("AIN1 =", read(1))            # Read channel 1
            print("AIN2 =", read(2))            # Read channel 2
            print("AIN3 =", read(3))            # Read channel 3
            print(" ")

           tmp = read(1)                       # Read light sensor value
           v = adc_to_voltage(tmp)
           r = voltage_to_resistance(v)
           lux = resistance_to_lux(r)
  
        
            print("Current light intensity: {}lux {}mV\n".format(lux, v))

            tmp = tmp * (255 - 125) / 255 + 125 # Scale value (LED threshold)
            write(tmp)                          # Output to DAC

            time.sleep(1.0)                     # 1 second delay

    except KeyboardInterrupt:
        pass

    finally:
        lgpio.i2c_close(h)                      # Close I2C handle
