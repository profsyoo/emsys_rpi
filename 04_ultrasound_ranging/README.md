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
- passive-buzzer(+-GPIO13, --GND)
- LED(GPIO06)
- 330Ω 저항
- ~~SWITCH~~
- ~~10kOhm pull-down register~~
- Breadboard, Jumper wires

---

## 💻 C 예제

### 📄 파일
- ~~`8-6ranging.c`~~

### ⚙️ 컴파일
```bash
pi@myhost: ~/src $ gcc -o pwm_led 8-5pwm_led.c-llgpio
pi@myhost: ~/src $ ./pw_led
```
---

## 💻 Python 예제

### 📄 파일
- `8-6ranging_us.py`

### ⚙️ 실행
```bash
pi@myhost: ~/src/py $ source myvenv/bin/activate 
(myvenv) pi@myhost: ~/src/py $ python 8-6ranging_us.py
```
---

## 💻 DIY

### 📄 mini project
- 차량 후방 감지기와 유사한 시스템을 만들어라(단, 거리에 따라서 LED의 밝기를 다르게 표현)
- 요구사항 분석->설계->구현(python)

### 📄 파일
- `car_ranging.py`

### ⚙️ 실행
```bash
pi@myhost: ~/src/py $ source myvenv/bin/activate 
(myvenv) pi@myhost: ~/src/py $ python car_ranging.py
```
