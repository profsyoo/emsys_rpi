# 🔌 GPIO SW PWM Example

Raspberry Pi 5에서 **GPIO 기본 동작**을 실습하는 예제입니다.

---

## 🎯 목적
- GPIO 출력 설정 이해
- software PWM(Pulse Width Modulation) 제어

---

## 🧰 하드웨어
- Raspberry Pi 5
- LED (GPIO06)
- 330Ω 저항
- SWITCH (GPIO21)
- 10kOhm pull-down register
- Breadboard, Jumper wires

---

## 💻 C 예제

### 📄 파일
- `8-5pwm_led.c`

### ⚙️ 컴파일
```bash
pi@myhost: ~/src $ gcc -o pwm_led 8-5pwm_led.c -llgpio
pi@myhost: ~/src $ ./pw_led
```
---

## 💻 Python 예제

### 📄 파일
- `8-5lgpio_pwm.py`
- `8-5pwm.py`

### ⚙️ 실행
```bash
pi@myhost: ~/src/py $ source myvenv/bin/activate 
(myvenv) pi@myhost: ~/src/py $ python 8-5lgpio_pwm.py
```

### ⚙️ DIY
- switch를 한 번 누르면 밝아지고, 다시 누르면 어두워지고, 다시 누르면 밝아지도록 LED(pwm활용)를 제어하라(hint: `8-5lgpio_pwm.py` 활용하여 `8-5pwm_ledNswitch.py`구현).
```bash
(myvenv) pi@myhost: ~/src/py $ python 8-5pwm_ledNswitch.py
```
