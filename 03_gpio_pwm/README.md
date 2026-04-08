# 🔌 GPIO SW PWM Example

Raspberry Pi 5에서 **GPIO 기본 동작**을 실습하는 예제입니다.

---

## 🎯 목적
- GPIO 출력 설정 이해
- software PWM(Pulse Width Modulation) 제어

---

## 🧰 하드웨어
- Raspberry Pi 5
- LED
- 330Ω 저항
- SWITCH
- 10kOhm pull-down register
- Breadboard, Jumper wires

---

## 💻 C 예제

### 📄 파일
- `8-2sw_polling.c`

### ⚙️ 컴파일
```bash
gcc -o 8-2sw_polling 8-2sw_polling.c -llgpio
./8-2sw_polling
```
---

## 💻 Python 예제

### 📄 파일
- `8-5lgpio_pwm.py`

### ⚙️ 실행
```bash
python 8-5lgpio_pwm.py
```
