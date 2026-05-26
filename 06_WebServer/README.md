# 🕷️🕸️ ~~Web Service~~

Not ready! Coming Soon
Raspberry Pi 5에서 **Web Service**을 실습하는 예제입니다.

---

## 🎯 목적
- Web service를 제공하기 위한 Web Server, Web Application Server 동작 이해
- 파이썬 기반의 Web Server Framework인 '<a href="https://flask.palletsprojects.com/en/stable/">Flask</a>'에 대한 이해
  
  <img width="479" height="200" alt="image" src="https://github.com/user-attachments/assets/05373346-d1bc-4eec-8b27-f398ae1beb73" />

- Web을 통한 Raspberry Pi 제어

---

## 🧰 하드웨어
- Raspberry Pi 5
- USB Webcam: <a href="https://www.abko.co.kr/brand/detail.php?it_id=1602055135&device=pc">ABKO APC720 HD 웹캠</a>
- passive buzzer, tact switch, LED, ultrasound ranging sensor, temp./humid. sensor, light sensor, etc.

---

## 💻 Warmup
### ⚙️ Flask 설치
- ~/src/py/ch06 디렉토리 생성 및 경로 이동 & 가상환경 활성화
  ```bash
  pi@myhost: ~/src/py $ mkdir ch06
  pi@myhost: ~/src/py $ source myvenv/bin/activate
  ```
- Flask 설치: ~/myven/lib/python3.13/site-packages에 Flask라이브러리 설치됨.
- Flask 설치 여부 확인
  ```bash
  (myven) pi@myhost:~/src/py $ pip install flask
  (myven) pi@myhost:~/src/py $ cd myenv/lib/python3.13/site-packages
  (myven) pi@myhost:~/src/py/mvenv/lib/python3.13/site-packages $ ls | grep flask
  flask
  flask-3.1.3.dist-info
  (myven) pi@myhost:~/src/py/mvenv/lib/python3.13/site-packages $ cd flask
  (myven) pi@myhost:~/src/py/mvenv/lib/python3.13/site-packages/flask $ ls
  app.py globals.py __pycache__ testing.py
  blueprints.py helpers.py py.typed typing.py
  cli.py __init__.py sansio views.py
  config.py json sessions.py wrappers.py
  ctx.py logging.py signals.py
  debughelpers.py __main__.py templating.py
  ```

### ⚙️ hello_flask.py
- `~/src/py/ch06/hello_flask.py`에 다음을 저장. 
```text
from flask import Flask

app = Flask(__name__) # Flask 객체 생성

@app.route('/') # 다음 2라인이 라우팅 테이블에 ['/':home]를 저장하도록 함 
def home(): 
	return '<h2>Hello, Flask</h2>'

if __name__ == '__main__':	# 이 프로그램이 독립적으로 실행되는 경우
	app.run(host='0.0.0.0', port=8080, debug=True) # app.run() 함수 실행
```
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

    
## 💻 ~~Troubleshooting~~
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
- <a href="https://flask.palletsprojects.com/en/stable/">Flask</a>
