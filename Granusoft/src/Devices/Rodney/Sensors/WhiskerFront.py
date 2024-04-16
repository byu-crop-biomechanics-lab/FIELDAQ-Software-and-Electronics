from .connections import *
from Devices.Rodney.Settings.configurator import SettingsSingleton as settings

# NOT WORKING
# This is likley because the encoders usea 5.0v spi and the board runs off of 3.3v.
# Need to try this with a new SPI interface then this code should be close to correct.

class WhiskerFront:

    def __init__(self):
        self.NO_OP_CMD = 0x00
        self.READ_POSITION_CMD = 0x10
        self.SET_ZERO_POINT_CMD = 0x70
        self.speed_hz = 1000000
        self.delay_us = 20
        self.config = settings()
        self.config_data = self.config.get('sensors', {})
        self.angle = 0.0

    def send_command(self, hex_command):
        spi.open(0, 0)
        spi.max_speed_hz = self.speed_hz
        spi.mode = 0b00
        spi.cshigh = False
        spi.bits_per_word = 8
        spi.lsbfirst = False

        GPIO.output(SPI_CE0, False)
        time.sleep(2e-5)
        spi.writebytes([hex_command])
        out = spi.readbytes(16)
        # out = spi.xfer2([hex_command], self.speed_hz, self.delay_us)
        print(out)
        time.sleep(2e-5)
        spi.close()
        GPIO.output(SPI_CE0, True)
        return bytes(out).hex()

    def read_angle(self):
        rtrn = self.send_command(self.READ_POSITION_CMD)
        while rtrn != '10':
            print('front ang:', rtrn)
            rtrn = self.send_command(self.NO_OP_CMD)
        msb = self.send_command(self.NO_OP_CMD)
        lsb = self.send_command(self.NO_OP_CMD)
        angle_in_hex_str = msb + lsb
        print(angle_in_hex_str)
        return int(angle_in_hex_str, 16)

    def set_zero_point(self):
        # Requires that the encoder is power cycled after this command
        # https://www.cuidevices.com/resource/amt20-v.pdf
        rtrn = self.send_command(self.SET_ZERO_POINT_CMD)
        while rtrn != '80':
            print('front zero:', rtrn)
            rtrn = self.send_command(self.NO_OP_CMD)

    def get_data(self, adc_out=0):
        try:
            self.angle = self.read_angle()
        except Exception as e:
            print(f'Front Whisker Error: {e}')
            return self.angle