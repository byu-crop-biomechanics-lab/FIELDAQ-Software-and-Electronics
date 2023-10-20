import time
import board
import busio
import digitalio
from time import sleep
import RPi.GPIO as GPIO
import serial
import adafruit_gps
import adafruit_lis3dh
#import adafruit_am2320
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# THIS IS AN EXACT DUPLICATE OF THE CONNECTIONS.PY FILE IN src/sensors

GPIO.setmode(GPIO.BCM)
i2c = busio.I2C(board.SCL, board.SDA, 115200)
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=3000)

# Temperature and Humidity sensor, off of the I2C pins on bottom right of board
# am = adafruit_am2320.AM2320(i2c)

# Accelerometer, top middle of board
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c)
lis3dh.range = adafruit_lis3dh.RANGE_2_G


# GPIO, right edge of board
GPIO1 = 4 #BOARD 7, BCM 4
GPIO2 = 17 #BOARD 11, BCM 17
GPIO3 = 27 #BOARD 13, BCM 27
GPIO4 = 22 #BOARD 15, BCM 22

# SPI/GPIO, top edge of board
SPI_CE1 = 7 #BOARD 26, BCM 7
SPI_CE0 = 8 #BOARD 24, BCM 8
SPI_SCLK = 11 #BOARD 23, BCM 11
SPI_MISO = 9 #BOARD 21, BCM 9
SPI_MOSI = 10 #BOARD 19, BCM 10

GPIO_PINS = [GPIO1, GPIO2, GPIO3, GPIO4, SPI_CE1, SPI_CE0,\
        SPI_SCLK, SPI_MISO, SPI_MOSI]

for pin in GPIO_PINS:
    GPIO.setup(pin, GPIO.OUT)


# ADC
ads1 = ADS.ADS1015(i2c, address=0x49, data_rate = 3300, mode=0)
ads2 = ADS.ADS1015(i2c, address=0x48, data_rate = 3300, mode=0)
CHAN0 = AnalogIn(ads1, ADS.P0)
CHAN1 = AnalogIn(ads1, ADS.P1)
CHAN2 = AnalogIn(ads1, ADS.P2)
CHAN3 = AnalogIn(ads1, ADS.P3)
CHAN4 = AnalogIn(ads2, ADS.P0, ADS.P1)
# CHAN5 = AnalogIn(ads2, ADS.P1)
CHAN6 = AnalogIn(ads2, ADS.P3)
CHAN7 = AnalogIn(ads2, ADS.P2)

# Channels for the pot and force sensors
POT_CHAN = CHAN3
X_LOAD_CHAN = CHAN4
Y_LOAD_CHAN = CHAN2

# Scaling factor for the force sensor
FORCE_SENSOR_SCALING = 3556.1878

# GPS
gps = adafruit_gps.GPS(uart, debug=False)
gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
gps.send_command(b'PMTK220,1000')
try:
    gps.update()
except:
    print("GPS may have a problem. Try Rebooting")

# MOTORS
PWMA = 16 #BOARD 36, BCM 16
AIN1 = 25 #BOARD 22, BCM 25
AIN2 = 20 #BOARD 38, BCM 20

PWMB = 21 #BOARD 40, BCM 21
BIN1 = 5 #BOARD 29, BCM 5
BIN2 = 12 #BOARD 32, BCM 12

PWMC = 13 #BOARD 33, BCM 13
CIN1 = 26 #BOARD 37, BCM 26
CIN2 = 19 #BOARD 35, BCM 19

PWMD = 24 #BOARD 18, BCM 24
DIN1 = 18 #BOARD 12, BCM 18
DIN2 = 23 #BOARD 16, BCM 23

MOTORS = ['A', 'B', 'C', 'D']
IN1 = [AIN1, BIN1, CIN1, DIN1]
IN2 = [AIN2, BIN2, CIN2, DIN2]
PWM = [PWMA, PWMB, PWMC, PWMD]

for in1, in2, pwm in zip(IN1, IN2, PWM):
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(pwm, GPIO.OUT)
