# Development Environments
## 1. Mobile hotspot at the Development Host(Windows 11) 
- 모바일 핫스팟 활성화(SSID/passwd확인): use your mobile phoe to test the hotspot.

## 2. Raspberry Pi  켜기
- 정상적인 경우 Green LED가 켜짐
- 모바일 핫스팟 설정 정보에서 연결된 디바이스의 ip확인(192.168.137.51?)
- ping from Development host to the target embedded system(i.e., RPi5)
```bash
C:\Users\OWNER>ping 192.168.137.51
```
- Connect to the RPi5 via ssh(secure shell) protocol: assuming the user id at RPi5 is 'pi' and the ip of it is 192.168.137.51
  ```bash
  C:\Users\OWNER>ssh pi@192.168.137.51
  ```
  - 서버에 처음 접속하는 경우, 서버 identity를 확인하라는 메시지가 나오며, 'yes', 비밀번호를 물으면 RPi5 OS이미지 생성할 때 입력했던 비번('pi'user에 대한 비번)을 입력
  - 리눅스 명령어 실습
    ```bash
    pi@myhost: ~/ $ uname -a
    pi@myhost: ~/ $ ls
    ```
  - 원격데스크톱 설정 xrdp
    ```bash
    pi@myhost: ~/ $ sudo apt install -y xrdp
    ```
    - Development Host에서 mstsc(원격데스크톱 응용 프로그램)을 실행시켜 컴퓨터 이름에 RPi5 ip를 입력하고 연결('connect')를 누르면, 접속되자마자 종료(이미 local에 사용자가 로긴되어 있는 경우, xrdp는 접속되자 마자 바로 종료)
    - 자동 로그인(Console, Desktop) 비활성화 & reboot
      ```bash
      pi@myhost: ~/ $ sudo raspi-config
      ```
    - 일반 사용자가 WiFi스캔 허용, polkit에 xrdp rule 추가
      - 사용자, pi를 netdev그룹에 추가 & 규칙 파일 열기
      ```bash
      pi@myhost: ~/ $ sudo usermod -aG netdev pi
      pi@myhost: ~/ $ sudo nano /etc/polkit-1/rules.d/10-networkmanager-wifi.rules
      pi@myhost: ~/ $ sudo reboot
      ```
      - 위의 두 번재 명령어를 실행해서 nano 편집기에서 /etc/polkit-1/rules.d/10-networkmanager-wifi.rules에 추가활 내용.
      ``` text
      polkit.addRule(function(action, subject) {
        // Wi-Fi 스캔 허용 규칙
        if (action.id == "org.freedesktop.NetworkManager.wifi.scan" && subject.isInGroup("netdev") ) {
          return polkit.Result.YES;
        }
      });
      ```
      - 규칙을 추가하였다면, 추가한 내용 확인 후 재부팅
      ```bash
      pi@myhost: ~/ $ sudo cat /etc/polkit-1/rules.d/10-networkmanager-wifi.rules
      pi@myhost: ~/ $ sudo reboot
      ```

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

