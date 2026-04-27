# 🔌 USB WEBCAM Example

Raspberry Pi 5에서 **USB Web Cam 기본 동작**을 실습하는 예제입니다.

---

## 🎯 목적
- USB Webcam 동작 이해
- Webcam 제어

---

## 🧰 하드웨어
- Raspberry Pi 5
- USB Webcam: ABKO APC720 HD 웹캠
- 330Ω 저항
- SWITCH (GPIO21)
- 10kOhm pull-down register
- Breadboard, Jumper wires

---

## 💻 Warmup

### 📄 파일
- `8-2sw_polling.c`
- `8-2sw_int.c`

### ⚙️ 명령어
```bash
pi@myhost: ~ $ lsusb
```
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
(myvenv) pi@myhost: ~/src/py $ python 8-2sw_polling.py
(myvenv) pi@myhost: ~/src/py $ python 8-2sw_int.py
(myvenv) pi@myhost: ~/src/py $ python 8-2.py
```

### ⚙️ DIY
- time stamp 정보를 활용하여 이전 event와 지금 event의 시간 차(iterval)을 ms단위로 출력하도록 소스(`8-2sw_int.py`) 수정(`8-2sw_int_diff.py`)
```bash
(myvenv) pi@myhost: ~/src/py $ python 8-2sw_int_diff.py
```
- C언어기반의 intterupt코드에서 똑같은 작업(`8-2sw_int.c` --> `8-2sw_int_diff.c`)
```bash
pi@myhost: ~/src $ gcc -o 8-2sw_int_diff 8-2sw_int_diff.c -llgpio
pi@myhost: ~/src $ ./8-2sw_int_diff
```
- 스위치를 누를 때마다 LED toggle(on->off->on->off...)하도록 소스(`8-4swNled.py`) 수정(`8-2swNled_toggle.py`)
```bash
(myvenv) pi@myhost: ~/src/py $ python 8-2swNled_toggle.py
```

