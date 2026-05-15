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
### ⚙️ 5.3 play with fswebcam
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

- 다른 옵션:
  - 180도 회전
    ```bash
    pi@myhost: ~/ch05/images $ fswebcam -r 640x480 --rotate 180 --jpeg 95 option.jpg
    ```
  - resize
    ```bash
    pi@myhost: ~/ch05/images $ fswebcam -r 200x150 image_200x150.jpg
    pi@myhost: ~/ch05/images $ ls
    image_200x150.jpg image.jpg
    ```
  - tile&subtitle
    ```bash
    pi@myhost: ~/ch05/images $ fswebcam --title "Hellow" --subtitle "good to see you"
    pi@myhost: ~/ch05/images $ ls
    image_200x150.jpg image.jpg image_title.jpg
    ```
    
### ⚙️ 5.4 camera control with OpenCV
- 가상환경 실행: 이미 lgpio모듈이 설치된 가상환경 실행
  ```bash
  pi@myhost: src/py $ source myvenv/bin/activate
  (myven) pi@myhost: src/py $ cd ch05
  (myven) pi@myhost: src/py/ch05 $
  ```
- OpenCV설치
  ```bash
  (myven) pi@myhost: src/py/ch05 $ pip install opencv-python
  ....
  Successfully installed numpy-2.4.2 opencv-python-4.13.0.92
  ```
  OpenCV 버전: opencv-python-4.13.0.92
  numpy 버전: numpy-2.4.2
- OpenCV버전 확인
  - python shell
    ```bash
    (myven) pi@myhost: src/py/ch05 $ pythonpip install opencv-python
    Python 3.13.5 (main, Jun 25 2025, 18:55:22) [GCC 14.2.0] on linux
    Type “help”, “copyright”, “credits” or “license” for more information.
    >>> import cv2
    >>>
    >>> cv2.__version__
    ‘4.13.0’
    >>>
    ```  
  - pip
    ```bash
    (myven) pi@myhost: src/py/ch05 $ pip show opencv-python
    Name: opencv-python
    Version: 4.13.0.92
    Summary: Wrapper package for OpenCV python bindings.
    Home-page: https://github.com/opencv/opencv-python
    Author:
    Author-email:
    License: Apache 2.0
    Location: /home/pi/myenv/lib/python3.13/site-packages
    Requires: numpy
    Required-by:
    (myenv) pi@pi:src/py/ch05 $
    ```
    ```bash
    (myenv) pi@pi:~/ch05 $ pip show numpy
    Name: numpy
    Version: 2.4.2
    Summary: Fundamental package for array computing in Python
    Home-page: https://numpy.org
    Author: Travis E. Oliphant et al.
    Author-email:
    License-Expression: BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0
    Location: /home/pi/myenv/lib/python3.13/site-packages
    Requires:
    Required-by: opencv-python
    (myenv) pi@pi:src/py/ch05 $
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

