# 🔌 GPIO LED Example

Raspberry Pi 5에서 **GPIO 기본 동작**을 실습하는 예제입니다.

---

## 🎯 목적
- GPIO 출력 설정 이해
- LED ON / OFF 제어

---

## 🧰 하드웨어
- Raspberry Pi 5
- LED
- 330Ω 저항
- Breadboard, Jumper wires

---

## 💻 C 예제

### 📄 파일
- `blink_led.c`

### ⚙️ 컴파일
```bash
gcc blink_led.c -o blink -llgpio
```
---

## 💻 Python 예제

### 📄 파일
- `blink_led.py`

### ⚙️ 실행
```bash
python blin_led.py
```
