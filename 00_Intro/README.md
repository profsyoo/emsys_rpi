# Development Environments
## 1. Mobile hotspot
모바일 핫스팟 활성화(SSID/passwd확인)

## 2. Raspberry Pi  켜기
정상적인 경우 Green LED가 켜짐

---
# H/W platform
## Raspberry Pi 5
https://www.raspberrypi.com/products/raspberry-pi-5/

---
# Linux Commands
```bash
pi@myhost: ~/src $ cd
pi@myhost: ~/src $ ls
pi@myhost: ~/src $ ls ~
pi@myhost: ~/src $ ls /
pi@myhost: ~/src $ cat hello.c
pi@myhost: ~/src $ sudo shutdown -h now
```
## C
```bash
pi@myhost: ~/src $ gcc -o hello helloc.
pi@myhost: ~/src $ gcc -o myled myled.c -llgpiols
pi@myhost: ~/src $ source myven/bin/activate
pi@myhost: ~/src $ python hello.py
```

## Python
### 가상환경(myven) 만들기
```bash
pi@myhost: ~/src $ python -m venv myven
```
### 가상환경(myven) 활성화/비활성화
```bash
pi@myhost: ~/src $ source myven/bin/activate
(myvenv) pi@myhost: ~/src $ deactivate
```

