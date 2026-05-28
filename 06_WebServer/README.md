# 🕷️🕸️ Web Service

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
- `hello_flash.py`: 
- `6_1newURL.py`: a URL
- `6_2URLRouting.py`: URL routing
- `6_3URLRoutingSlashTest.py`: the ending '/'
- `6_4StaticContents.py`: http://ip:8080/static routed to './staic/' directory(default) 


### ⚙️ 실행
```bash
pi@myhost: ~/src/py $ source myvenv/bin/activate
(myvenv) pi@myhost: ~/src/py/ $ cd ch06
(myvenv) pi@myhost: ~/src/py/ch06 $ python 6_1newURL.py
```

### ⚙️ DIY
- 새로운 URL라우팅 테이블을 추가하고 서로 다른 URL 요청을 테스트 하라.
- LED제어를 위한 새로운 URL라우팅 테이블을 추가혹 테스트하라.
- port forwarding: how to access your Raspberry Pi from the external network such as your mobile network(your phone?)
    
## 💻 ~~Troubleshooting~~
- to be updated

## 💻 References
- <a href="https://flask.palletsprojects.com/en/stable/">Flask</a>
