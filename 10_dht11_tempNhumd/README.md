# 🔌 GPIO Serial Comm. Example

Raspberry Pi 5에서 **DHT11 기본 동작**을 실습하는 예제입니다. 
<a href="https://gemini.google.com/">**Google Geminni**</a>를 활용하여 제조사가 제공한 이전 코드를 Raspberry Pi5에 맞게 수정하였습니다.

---

## 🎯 목적
- GPIO 출력/입력 설정 이해
- Seirial Protocol 이해
- DHT11 이해

---

## 🧰 하드웨어
- Raspberry Pi 5
- **<a href = "https://www.mouser.com/datasheet/2/758/DHT11-Technical-Data-Sheet-Translated-Version-1143054.pdf?srsltid=AfmBOoo9eabUqoBSPZdhw6zsjnxrcXep_eyau1uOid2S6jUx_5ejUms3">dht11</a>**(VCC-5V, DATA-GPIO4, GND-GND)
  
  <img width="316" height="125" alt="image" src="https://github.com/user-attachments/assets/f61a836f-540e-4485-bb09-db8dcfb3763c" />
- <a href = "https://www.nxp.com/docs/en/data-sheet/PCF8591.pdf">PCF8591</a> AD/DA(SDA-GPIO02, SCL-GPIO03, Vcc-3.3V, GND-GND)
  
  <img width="437" height="220" alt="image" src="https://github.com/user-attachments/assets/6e4e698a-dbdc-4d8e-b7dc-8a945ce84ab2" />
  
  - potentiometer(AIN0), photoresistor(AIN1, 밝으면 저항 감소, 어두우면 저항 증가)/LDR(Light Dependent Resistor), thermistor(AIN2, 온도 하강->저항 증가)
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
### 📄 adafruit-circuitpython-dht 모듈 설치 for python
- 가상환경 진입&설치.
  ```bash
  pi@myhost: ~/src/py $ source myvenv/bin/activate 
  (myvenv) pi@myhost: ~/src/py $ pip install adafruit-circuitpython-dht
  ```
 
### ⚙️ lgpio for C
- 이미 설치

---

## 💻 C 예제

### 📄 파일
- `dht11.c`

### ⚙️ 컴파일
```bash
pi@myhost: ~/src $ gcc -o dht11 dht11.c -llgpio
pi@myhost: ~/src $ ./dht11
```
---

## 💻 Python 예제

### 📄 파일
- `dht11.py`
- `dht11_lgpio.py`

### ⚙️ 실행
```bash
pi@myhost: ~/src/py $ source myvenv/bin/activate 
(myvenv) pi@myhost: ~/src/py $ python dht11.py
(myvenv) pi@myhost: ~/src/py $ python dht11_lgpio.py
```

---
## 💻 DIY

### 📄 mini project
- 여름이 다가오고있다. 일정 온도보다 높아지면 음식이 상할 수 있다. 음식의 신선도 유지에 도움을 줄 수 있는 응용을 개발하라(단, dht11모듈 기본 활용, + led/buzzer 등 활용)
- 요구사항 분석->설계->구현(python)

### 📄 파일
- `dht11_fresh.py`

### ⚙️ 실행
```bash
pi@myhost: ~/src/py $ source myvenv/bin/activate 
(myvenv) pi@myhost: ~/src/py $ python dht11_fresh.py
```

