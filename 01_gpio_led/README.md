# 🔌 GPIO LED Example

Raspberry Pi 5에서 **GPIO 기본 동작**을 실습하는 예제입니다.

---

## 🎯 목적
- GPIO 출력 설정 이해
- LED ON / OFF 제어

---

## 🧰 하드웨어
- Raspberry Pi 5
- LED (GPIO06)
- 330Ω 저항
- Breadboard, Jumper wires

---

## 💻 C 예제

### 📄 파일
- `blink_led.c`

### ⚙️ 컴파일
```bash
pi@myhost: ~/src $ gcc blink_led.c -o blink -llgpio
```
---

## 💻 Python 예제
### 가상환경
- 실행
```bash
pi@myhost: ~/src $ source myve/bin/activate
```
- 모듈설치:
```bash
(myvenv) pi@myhost: ~/src $ pip install lgpio
```


### 📄 파일
- `blink_led.py`

### ⚙️ 실행
```bash
(myvenv) pi@myhost: ~/src $ python blin_led.py
```
