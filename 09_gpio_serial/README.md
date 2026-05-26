# 🔌 GPIO Serial Comm. Example

Raspberry Pi 5에서 **Serial Comm. 기본 동작**을 실습하는 예제입니다. Not Ready!

---

## 🎯 목적
- GPIO 출력/입력 설정 이해
- Seirial Protocol 이해
- ADC(pcf8591)/Photoresistor/Thermistor 이해

---

## 🧰 하드웨어
- Raspberry Pi 5
- <a href = "https://www.nxp.com/docs/en/data-sheet/PCF8591.pdf">PCF8591</a> AD/DA(SDA-GPIO02, SCL-GPIO03, Vcc-3.3V, GND-GND)
  <img width="437" height="220" alt="image" src="https://github.com/user-attachments/assets/6e4e698a-dbdc-4d8e-b7dc-8a945ce84ab2" />
  - potentiometer(AIN0), photoresistor(AIN1, 밝으면 저항 감소, 어두우면 저항 증가)/LDR(Light Dependent Resistor), thermistor(AIN2, 온도하강->저항증가)
     ```text
               +3.3V (Vcc)
                  |
                 [10kOhm]
                  |
     AIN0 --------+--------[VR1]---GND
         
     AIN1 ---------<-------[R3:10kOhm]----Vcc
                   |
            GND---[LDR]
                   
     AIN2 ---------<-------[R4:10kOhm]----Vcc
                   |
            GND---[Thermistor]
                  
     AIN3 ---------<-GND
- HC-SR04(Vcc-5V, Trigger(Out)-GPIO20, Echo(In)-GPIO16, Gnd-GND(0V))
- passive-buzzer(+-GPIO13, --GND)
- LED(GPIO06)
- 330Ω 저항
- SWITCH
- 10kOhm pull-down register
- Breadboard, Jumper wires

---

## 💻 Prerequisite
### 📄 I2C활성화 전
- (Before) kernal module&device file
  ```bash
  pi@myhost: ~/src/c $ lsmod | grep i2c
  pi@myhost: ~/src/c $ ls -l /dev/i3c*
  ```
 
### ⚙️ I2C활성화 시키기
라즈베리파이가 I2C 통신을 할 수 있도록 운영체제 설정 과정. i2c_bcm2835 커널 모듈을 라즈베리파이 운영체제에 추가
- 3 Interface option 선택 -> I5 I2C 선택 -> enable
  ```bash
  pi@myhost: ~/src/c $ sudo raspi-config
  ```

### 📄 I2C활성화 후
- (After) kernal module&device file
  ```bash
  pi@myhost: ~/src/c $ lsmod | grep i2c
  pi@myhost: ~/src/c $ ls -l /dev/i3c*
  ```
- i2c 유틸리티 프로그램 설치 & i2c 버스에 연결된 Slave 장치 확인
  - 1번 i2c 버스에 대해, 라즈베리파이의 i2c master에 연결된 127개의 Slave를 찾아 정보 출력
  - 현재 연결된  i2c 장치가 없기 때문에 아무것도 출력되지 않음
  - 아직 브레드보드에 아무 장치가 구성되지 않았기 때문
  ```bash
  pi@myhost: ~/src/c $ ssudo apt-get install i2c-tools
  pi@myhost: ~/src/c $ i2cdetect –y 1 
  ```
- HW구성 후 버스 검사
  - 1번 i2c 버스에 대해, 라즈베리파이의 i2c master에 연결된 127개의 Slave를 찾아 정보 출력
  - 1번 i2c 버스에 연결된 모든 slave 장치를 찾아 출력
  - 0x48번 번호를 가진 I2C slave 장치 발견 – <a href = "https://www.nxp.com/docs/en/data-sheet/PCF8591.pdf">pcf1891</a> 모듈(AD/DC with Photoresistor, LED, etc.)
  ```bash
  pi@myhost: ~/src/c $ i2cdetect –y 1 
       0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
  00:                         -- -- -- -- -- -- -- -- 
  10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
  20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
  30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
  40: -- -- -- -- -- -- -- -- 48 -- -- -- -- -- -- -- 
  50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
  60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
  70: -- -- -- -- -- -- -- --
  ```

---

## 💻 C 예제

### 📄 파일
- `PhotoResistor-pcf8591_lgpio.c`
- `PhotoResistor-pcf8591.c`

### ⚙️ 컴파일
```bash
pi@myhost: ~/src $ gcc -o PhotoReisistor PhotoResistor-pcf8591_lgpio.c -llgpio
pi@myhost: ~/src $ ./PhotoReisistor
```
---

## 💻 Python 예제

### 📄 파일
- `PhotoRegistor-pcf8591_lgpio.py`(i2c)
- `pcf8591sensors_lgpio.py`(sensors: °C and lux)
- `PhotoResistor-pcf8591.py`(SMBus)

### ⚙️ 실행
```bash
pi@myhost: ~/src/py $ source myvenv/bin/activate 
(myvenv) pi@myhost: ~/src/py $ python PhotoRegistor-pcf8591_lgpio.py
(myvenv) pi@myhost: ~/src/py $ python pcf8591sensors_lgpio.py
(myvenv) pi@myhost: ~/src/py $ python PhotoRegistor-pcf8591.py
((myvenv) pi@myhost: ~/src/py $ pip install smbus)
```

---
## 💻 DIY

### 📄 mini project
- 조도에 따라서 외부 LEDD의 밝기를 제어하라(단, SW PWM활용)
- 요구사항 분석->설계->구현(python)

### 📄 파일
- `photoresistor_led.py`

### ⚙️ 실행
```bash
pi@myhost: ~/src/py $ source myvenv/bin/activate 
(myvenv) pi@myhost: ~/src/py $ python photoresistor_led.py
```

