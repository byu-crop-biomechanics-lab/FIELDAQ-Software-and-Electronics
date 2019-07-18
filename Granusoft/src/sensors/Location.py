from .connections import *

class Location:

    def __init__(self):
        self.lat = 0.0
        self.long = 0.0
        gps.update()
        if gps.has_fix:
            self.lat = gps.latitude
            self.long = gps.longitude

    def get_data(self):
        gps.update()
        if gps.has_fix:
            self.lat = gps.latitude
            self.long = gps.longitude
        return self.lat, self.long

    def update_gps_location(self):
        uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=3000)
        UART = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=3000)
        gps = adafruit_gps.GPS(uart, debug=False)
        gps.update()
        gps = adafruit_gps.GPS(UART, debug=False)
        gps.send_command(b'PMTK184,1')
        while True:
            try:
                gps = adafruit_gps.GPS(uart, debug=False)
                gps.update()
                break
            except:
                gps = adafruit_gps.GPS(UART, debug=False)
                gps.send_command(b'PMTK184,1')
        self.ids['test_text'].text = 'GPS MEMORY\nCLEARED'
