from tests.gpio_test import *
from tests.adc_test import *
from tests.gps_test import *
from tests.motor_test import *
from tests.temp_test import *
from tests.accl_test import *
import RPi.GPIO as GPIO

if __name__ == "__main__":
    temp_test()
    accl_test()
    gpio_test()
    adc_test()
    gps_test()
    motor_test()
    GPIO.cleanup()
