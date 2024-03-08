import traceback
import sys
try:
    from .SensorReal import Sensor
except:
    # print(traceback.print_exc()) # Tell us what happened
    from .SensorFake import Sensor
