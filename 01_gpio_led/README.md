```markdown
# GPIO LED Example

## 목적
GPIO 기본 동작 이해

## 하드웨어
- Raspberry Pi 5
- LED + 330Ω 저항

## 컴파일(in C)
```bash
gcc -o blink blink_led.c -llgpio
sudo ./gpio_led

## 파이썬 (in Python)
```bash
gcc -o blink blink_led.c -llgpio
sudo ./gpio_led
