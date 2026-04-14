# 🔌 GPIO SWITCH Example

Raspberry Pi 5에서 **GPIO 기본 동작**을 실습하는 예제입니다.

---

## 🎯 목적
- GPIO 입력 설정 이해
- SWITCH read(polling vs interrupt) 제어

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
- `8-2sw_polling.c`
- `8-2sw_int.c`

### ⚙️ 컴파일
```bash
pi@myhost: ~/src $ gcc -o 8-2sw_polling 8-2sw_polling.c -llgpio
pi@myhost: ~/src $ ./8-2sw_polling
pi@myhost: ~/src $ gcc -o 8-2sw_int 8-2sw_int.c -llgpio
pi@myhost: ~/src $ ./8-2sw_int
```
---

## 💻 Python 예제

### 📄 파일
- `8-2sw_polling.py`
- `8-2sw_int.py`
- `8-3event.py`
- `8-4swNled.py`

### ⚙️ 실행
```bash
pi@myhost: ~/src/py $ source myvenv/bin/activate
pi@myhost: ~/src/py $ python 8-2sw_polling.py
pi@myhost: ~/src/py $ python 8-2sw_int.py
pi@myhost: ~/src/py $ python 8-2.py
```
