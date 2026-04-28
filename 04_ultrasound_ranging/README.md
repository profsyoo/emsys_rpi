# 🔌 GPIO Ultrasound Ranging Example

Raspberry Pi 5에서 **GPIO 기본 동작**을 실습하는 예제입니다. Not Ready!

---

## 🎯 목적
- GPIO 출력/입력 설정 이해
- Ultrasound Ranging 제어

---

## 🧰 하드웨어
- Raspberry Pi 5
- HC-SR04(Vcc-5V, Trigger(Out)-GPIO20, Echo(In)-GPIO16, Gnd-GND(0V))
- LED(GPIO06)
- 330Ω 저항
- ~~SWITCH~~
- ~~10kOhm pull-down register~~
- Breadboard, Jumper wires

---

## 💻 C 예제

### 📄 파일
- `8-6ranging.c`

### ⚙️ 컴파일
```bash
pi@myhost: ~/src $ gcc -o pwm_led 8-5pwm_led.c-llgpio
pi@myhost: ~/src $ ./pw_led
```
---

## 💻 Python 예제

### 📄 파일
- `8-5lgpio_pwm.py`

### ⚙️ 실행
```bash
pi@myhost: ~/src/py $ source myvenv/bin/activate 
(myvenv) pi@myhost: ~/src/py $ python 8-5lgpio_pwm.py
```
