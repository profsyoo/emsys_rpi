#02_gpio_switch/8-2sw_polling.py
#+
#03_gpio_pwm/8-5lgpio_pwm.py
 
import lgpio
import time
 
PIN = 6
sPIN = 21
chip = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(chip, PIN)
 
lgpio.gpio_claim_input(chip, sPIN, lgpio.SET_PULL_DOWN)
 
 
duty = 0
step = 1
print("press-->brighten, release-->darken.., Ctrl+c to stop")
try:
    while True:
        v = lgpio.gpio_read(chip, sPIN)
        if v == 1:
          duty = duty + step
          if duty > 100:
              duty = 100
        else:
          duty = duty - step
          if duty < 0:
              duty = 0
        lgpio.tx_pwm(chip, PIN, 1000, duty)
        time.sleep(0.3)
except KeyboardInterrupt:
    pass
finally:
    lgpio.tx_pwm(chip, PIN, 0, 0)   # PWM 중지
    lgpio.gpiochip_close(chip)
