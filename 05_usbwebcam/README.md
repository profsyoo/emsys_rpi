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
  - HD720p(1280x720), 30fps
  <img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/9cfac6c9-184b-41a7-a433-bf6cdcddc132" />
- passive buzzer, tact switch, LED, ultrasound ranging sensor, etc.

---

## 💻 Warmup
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
  
  <img width="586" height="345" alt="image" src="https://github.com/user-attachments/assets/7273966c-62ae-4844-93e8-9b850f43001a" />

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

### ⚙️ 5.4 Python Virtual Environment
- skip
<img width="520" height="224" alt="image" src="https://github.com/user-attachments/assets/a4081f4f-38da-4ef6-a724-10a4bae744d7" />
<img width="597" height="312" alt="image" src="https://github.com/user-attachments/assets/6f02544f-bc7c-4b1d-86a0-7a620f149ff4" />

    
### ⚙️ 5.5 camera control with OpenCV
- 가상환경 실행: 이미 lgpio모듈이 설치된 가상환경 실행
  ```bash
  pi@myhost: src/py $ source myvenv/bin/activate
  (myven) pi@myhost: src/py $ cd ch05
  (myven) pi@myhost: src/py/ch05 $
  ```
- OpenCV설치(+numpy): 2분 정도 소요
  ```bash
  (myven) pi@myhost: src/py/ch05 $ pip install opencv-python
  ....
  Successfully installed numpy-2.4.5 opencv-python-4.13.0.92
  ```
  OpenCV 버전: opencv-python-4.13.0.92
  numpy 버전: numpy-2.4.5
- OpenCV버전 확인
  - python shell
    ```bash
    (myven) pi@myhost: src/py/ch05 $ pythonpip install opencv-python
    Python 3.13.5 (main, Jun 25 2025, 18:55:22) [GCC 14.2.0] on linux
    Type “help”, “copyright”, “credits” or “license” for more information.
    >>> import cv2
    >>> cv2.__version__
    ‘4.13.0’
    >>> import numpy
    >>> numpy.__version__
    ‘2.4.5’
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
    Version: 2.4.5
    Summary: Fundamental package for array computing in Python
    Home-page: https://numpy.org
    Author: Travis E. Oliphant et al.
    Author-email:
    License-Expression: BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0
    Location: /home/pi/myenv/lib/python3.13/site-packages
    Requires:
    Required-by: opencv-python
    (myenv) pi@pi:src/py/ch05 $

### ⚙️ 5.6 Object Recognition with Haar Cascades
- Object Recognition with Haar Cascades Model

---


## 💻 C 예제

### 📄 파일
- `no.c`

### ⚙️ 컴파일
```bash
pi@myhost: ~/src/c $ 
```
---

## 💻 Python 예제

### 📄 파일
- `5-4CaptureNSave.py`: Capture the image & Save it
- `5-5Preview.py`: Show the preview in real-time. To escape, please **click 'preview' window**, then press 'ESC'
- `5-6PreviewNSave.py`: Show the preview and Save it in a video
- `5-7CaptureNSaveViaKey.py`: Capture an image via. a key stroke.
- `5-8FaceRecogHaar.py`: Face recognition based on '5-7...py' and Haar Cascades Model.
- `5-9FaceRecogHaarRev.py`: revision of '5-8...py'

### ⚙️ 실행
```bash
pi@myhost: ~/src/py $ source myvenv/bin/activate
(myvenv) pi@myhost: ~/src/py $ python 5-4CaptureNSave.py
(myvenv) pi@myhost: ~/src/py $ python 5-5Preview.py
(myvenv) pi@myhost: ~/src/py $ python 5-6PreviewNSave.py
```

### ⚙️ DIY
- `fswebcam`명령어를 파이썬에서 제어
  - 스위치를 누를 때 마다, 사진을 촬영하는(파일이름에 현재 날짜/시간 정보 표시) 프로그램(fswebcam명령어 활용, 5-1subpro_fswebcam.py활용)
  - 객체가 일정 거리 이상 근접하는 경우, LED를 켜고 사진 촬영(파일 이름에 event 시간 정보 명시)
- `OpenCV`모듈 활용 파이썬에서 제어
  - 스위치를 누를 때 마다, 사진을 촬영하는(파일이름에 현재 날짜/시간 정보 표시) 프로그램
  - 객체가 일정 거리 이상 근접하는 경우, LED를 켜고 사진 촬영(파일 이름에 event 시간 정보 명시)

    
## 💻 Troubleshooting
- RDP에서 사진 클릭 시 뷰어프로그램 실행 안됨: local login여부 확인 후 로그 아웃
- "QFontDatabase: Cannot find font directory":
  - ⚠️ 아래 에러 메시지의 디렉토리 확인: **home/pi/src/py/book/ve-rpi-lgpio/lib/python3.13/site-packages/cv2/qt/**
  ```text
  QFontDatabase: Cannot find font directory /home/pi/src/py/book/ve-rpi-lgpio/lib/python3.13/site-packages/cv2/qt/fonts.
  Note that Qt no longer ships fonts. Deploy some (from https://dejavu-fonts.github.io/ for example) or switch to fontconfig.
  QFontDatabase: Cannot find font directory /home/pi/src/py/book/ve-rpi-lgpio/lib/python3.13/site-packages/cv2/qt/fonts.
  Note that Qt no longer ships fonts. Deploy some (from https://dejavu-fonts.github.io/ for example) or switch to fontconfig.
  QFontDatabase: Cannot find font directory /home/pi/src/py/book/ve-rpi-lgpio/lib/python3.13/site-packages/cv2/qt/fonts.
  Note that Qt no longer ships fonts. Deploy some (from https://dejavu-fonts.github.io/ for example) or switch to fontconfig.
  QFontDatabase: Cannot find font directory /home/pi/src/py/book/ve-rpi-lgpio/lib/python3.13/site-packages/cv2/qt/fonts.
  Note that Qt no longer ships fonts. Deploy some (from https://dejavu-fonts.github.io/ for example) or switch to fontconfig.
  QFontDatabase: Cannot find font directory /home/pi/src/py/book/ve-rpi-lgpio/lib/python3.13/site-packages/cv2/qt/fonts.
  Note that Qt no longer ships fonts. Deploy some (from https://dejavu-fonts.github.io/ for example) or switch to fontconfig.
  ```
  
  - solution by Gemmini
    ```bash
    (ve-rpi-lgpio) pi@myhost: ~/src/py $ sudo apt install -y fontconfig fonts-dejavu
    ```
  - 여전히 문제라면, "시스템에 폰트를 설치했음에도 불구하고, 파이썬 가상환경(myvenv) 안에 설치된 OpenCV의 내장 Qt 라이브러리가 여전히 특정 경로에서 폰트 디렉토리를 고집스럽게 찾고 있어서 발생하는 현상": "에러 메시지가 가리키는 정확한 가상환경 경로에 폰트 디렉토리를 직접 수동으로 심어주는 방법". ⚠️ **주의(위의 에러 메시지의 경로 확인 후 아래 명령어 적절히 수행)**
    ```bash
    (ve-rpi-lgpio) pi@myhost: ~/src/py $ cd /home/pi/src/py/book/ve-rpi-lgpio/lib/python3.13/site-packages/cv2/qt/
    (ve-rpi-lgpio) pi@myhost: ~/src/py/book/ve-rpi-lgpio/lib/python3.13/site-packages/cv2/qt $ mkdir fonts
    (ve-rpi-lgpio) pi@myhost: ~/src/py/book/ve-rpi-lgpio/lib/python3.13/site-packages/cv2/qt $ cp /usr/share/fonts/truetype/dejavu/* ./fonts/
    ```

## 💻 References
- <a href="https://docs.opencv.org/4.x/">OpenCV</a>

