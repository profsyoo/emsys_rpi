#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <linux/i2c-dev.h>

#define I2C_DEV     "/dev/i2c-1"
#define PCF8591_ADDR 0x48

int i2c_fd;

/* ADC channel read */
uint8_t pcf8591_read(int chn)
{
    uint8_t ctrl;
    uint8_t value;

    if (chn < 0 || chn > 3) return 0;

    /* Control byte: 0x40 | channel */
    ctrl = 0x40 | chn;

    /* Select channel */
    write(i2c_fd, &ctrl, 1);

    /* Dummy read (start conversion) */
    read(i2c_fd, &value, 1);

    /* Actual ADC read */
    read(i2c_fd, &value, 1);

    return value;
}

/* DAC write */
void pcf8591_write(uint8_t val)
{
    uint8_t buf[2];
    buf[0] = 0x40;   // DAC enable
    buf[1] = val;

    write(i2c_fd, buf, 2);
}

int main(void)
{
    int i;
    uint8_t tmp;

    /* Open I2C */
    i2c_fd = open(I2C_DEV, O_RDWR);
    if (i2c_fd < 0) {
        perror("I2C open failed");
        return 1;
    }

    /* Set slave address */
    if (ioctl(i2c_fd, I2C_SLAVE, PCF8591_ADDR) < 0) {
        perror("I2C set address failed");
        close(i2c_fd);
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

        /* Scale value (same as Python code) */
        tmp = tmp * (255 - 125) / 255 + 125;

        /* Output to DAC */
        pcf8591_write(tmp);

        sleep(1);
    }

    close(i2c_fd);
    return 0;
}
