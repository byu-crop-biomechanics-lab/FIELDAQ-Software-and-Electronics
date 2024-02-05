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
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from cedargrove_nau7802 import NAU7802
import adafruit_tca9548a

GPIO.setmode(GPIO.BCM)
i2c = busio.I2C(board.SCL, board.SDA, 115200)
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=3000)

# Temperature and Humidity sensor, off of the I2C pins on bottom right of board
#am = adafruit_am2320.AM2320(i2c)

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
onBoardAds1 = ADS.ADS1115(i2c, address=0x49, data_rate = 860, mode=0)
onBoardAds2 = ADS.ADS1115(i2c, address=0x48, data_rate = 860, mode=0, gain=2)
CHAN0 = AnalogIn(onBoardAds1, ADS.P0)
CHAN1 = AnalogIn(onBoardAds1, ADS.P1)
CHAN2 = AnalogIn(onBoardAds1, ADS.P2)
CHAN3 = AnalogIn(onBoardAds1, ADS.P3)
CHAN4 = AnalogIn(onBoardAds2, ADS.P0)
CHAN5 = AnalogIn(onBoardAds2, ADS.P1)
CHAN6 = AnalogIn(onBoardAds2, ADS.P2)
CHAN7 = AnalogIn(onBoardAds2, ADS.P3)

# initialize the multiplexer
mux = adafruit_tca9548a.PCA9546A(i2c, address=0x70)
channels = []
for channel in range(4):
    if mux[channel].try_lock():
        addresses = mux[channel].scan()
        channels = addresses
        mux[channel].unlock()

# ADC on rodney PCB
ADC0 = NAU7802(mux[0], address=0x2a, active_channels=2)  # 0
ADC1 = NAU7802(mux[1], address=0x2a, active_channels=2)  # 1
ADC2 = NAU7802(mux[2], address=0x2a, active_channels=2)  # 2
ADC3 = NAU7802(mux[3], address=0x2a, active_channels=2)  # 3

# Set to channel 2 for half bridge, 1 for full bridge
ADC0.channel = 2
ADC1.channel = 2
ADC2.channel = 2
ADC3.channel = 2

enabled1 = ADC0.enable(True)
enabled2 = ADC1.enable(True)
enabled3 = ADC2.enable(True)
enabled4 = ADC3.enable(True)
# Calibrate and zero the ADC's
time.sleep(3) # wait 3 seconds for zeroing ADCs

print(f'ADC0: {ADC0.read()}')
print(f'ADC1: {ADC1.read()}')
print(f'ADC2: {ADC2.read()}')
print(f'ADC3: {ADC3.read()}')

# Channels for the pot and force sensors

HEIGHT_POT_CHAN = CHAN1
POT_CHAN = CHAN2

X_LOAD_CHAN = CHAN4
Y_LOAD_CHAN = CHAN3

STRAIN_1_CHAN = CHAN4
STRAIN_2_CHAN = CHAN3

# Scaling factor for the force sensor
FORCE_SENSOR_SCALING = 16 # 3556.1878
# ads2.gain = FORCE_SENSOR_SCALING

# GPS
gps = adafruit_gps.GPS(uart, debug=False)
gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
gps.send_command(b'PMTK220,500')
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