# 🔌 USB WEBCAM Example

Raspberry Pi 5에서 **USB Web Cam 기본 동작**을 실습하는 예제입니다.

---

## 🎯 목적
- USB Webcam 동작 이해
- Webcam 제어

---

## 🧰 하드웨어
- Raspberry Pi 5
- USB Webcam: <a href="https://www.abko.co.kr/brand/detail.php?it_id=1602055135&device=pc">ABKO APC720 HD 웹캠</a>
<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/9cfac6c9-184b-41a7-a433-bf6cdcddc132" />

- passive buzzer, tact switch, LED, ultrasound ranging sensor, etc.

---

## 💻 Warmup

### 📄 파일
- `8-2sw_polling.c`
- `8-2sw_int.c`

### ⚙️ lsusb&fswebcam
- plug-in the cam.: "Bus 003 Device 002: ID 0806:0806 SunplusIT Inc ABKO APC720 HD WEBCAM"
```bash
pi@myhost: ~ $ lsusb
```
- <a href="https://www.sanslogic.co.uk/fswebcam/">fswebcam</a>:
```text
fswebcam  is  a small and simple webcam app for *nix. It can capture im‐
       ages from a number of different sources and perform simple  manipulation
       on the captured image. The image can be saved as one or more PNG or JPEG
       files.

       The  PNG  or JPEG image can be sent to stdio using the filename "-". The
       output filename is formatted by strftime.
```
```bash
pi@myhost: ~ $ sudo apt-get install fswebcam
pi@myhost: ~ $ fswebcam image.jpg
```
### ⚙️ play with fswebcam
- ~/ch05/images 디렉토리 생성 및 경로 이동
```bash
pi@myhost: ~ $ mkdir ch05
pi@myhost: ~ $ cd ch05
pi@myhost: ~/ch05 $ mkdir images
pi@myhost: ~/ch05 $ cd images
```
- 사진 촬영 및 myimage.jpg저장
```bash
pi@myhost: ~/ch05/images $ fswebcam image.jpg
pi@myhost: ~/ch05/images $ ls
```
- 사진 확인:
<img width="879" height="517" alt="image" src="https://github.com/user-attachments/assets/7273966c-62ae-4844-93e8-9b850f43001a" />

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

