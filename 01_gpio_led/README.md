```markdown
# GPIO LED Example

## 목적
Raspberry Pi 5에서 GPIO의 기본 동작을 이해한다.

## 하드웨어
- Raspberry Pi 5
- LED
- 330Ω 저항
- Breadboard, Jumper wires

---

## C 예제

### 파일
- `blink_led.c`

### 컴파일
```bash
gcc blink_led.c -o blink -llgpio
