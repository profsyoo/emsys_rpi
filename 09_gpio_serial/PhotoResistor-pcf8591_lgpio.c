#include <stdio.h>
#include <stdint.h>
#include <unistd.h>
#include <lgpio.h>

#define I2C_BUS        1        // /dev/i2c-1
#define PCF8591_ADDR  0x48

int i2c_handle;

/* ADC channel read */
uint8_t pcf8591_read(int chn)
{
    uint8_t ctrl;
    uint8_t value;

    if (chn < 0 || chn > 3)
        return 0;

    /* Control byte: enable ADC, select channel */
    ctrl = 0x40 | chn;

    /* Select channel */
    lgI2cWriteDevice(i2c_handle, (char *)&ctrl, 1);

    /* Dummy read (start conversion) */
    lgI2cReadDevice(i2c_handle, (char *)&value, 1);

    /* Actual ADC read */
    lgI2cReadDevice(i2c_handle, (char *)&value, 1);

    return value;
}

/* DAC write */
void pcf8591_write(uint8_t val)
{
    char buf[2];
    buf[0] = 0x40;   /* DAC enable */
    buf[1] = val;

    lgI2cWriteDevice(i2c_handle, buf, 2);
}

int main(void)
{
    int i;
    uint8_t tmp;

    /* Open I2C using lgpio */
    i2c_handle = lgI2cOpen(I2C_BUS, PCF8591_ADDR, 0);
    if (i2c_handle < 0) {
        fprintf(stderr, "lgI2cOpen failed\n");
        return 1;
    }

    while (1) {
        for (i = 0; i < 4; i++) {
            uint8_t v = pcf8591_read(i);
            printf("AIN%d = %d\n", i, v);
        }

        printf("\n");

        /* Read channel 1 (light sensor) */
        tmp = pcf8591_read(1);
        printf("Current light intensity: %.2f mV\n\n",
               (float)tmp * 5000.0f / 255.0f);

        /* Scale value */
        tmp = tmp * (255 - 125) / 255 + 125;

        /* Output to DAC */
        pcf8591_write(tmp);

        sleep(1);
    }

    lgI2cClose(i2c_handle);
    return 0;
}
