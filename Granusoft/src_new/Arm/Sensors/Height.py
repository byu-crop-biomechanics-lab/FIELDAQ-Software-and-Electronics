from .connections import *
import configurator as config

class HeightPoT:

    def __init__(self):
        self.config_data = config.get('sensors', {})
        self.height_pot = 0.0
        self.height_pot_adc = 0.0
        try:
            self.slope = self.config_data['Load Cell\nHeight']['slope']
            self.intercept = self.config_data['Load Cell\nHeight']['intercept']
        except:
            self.slope = 1.0
            self.intercept = 0.0

    def get_data(self, adc_out = 0):
        try:
            if adc_out == 1:
                self.height_pot_adc = HEIGHT_POT_CHAN.value
                return self.height_pot_adc
            else:
                self.height_pot = self.interpolate_height_data(HEIGHT_POT_CHAN.value)
                return self.height_pot
        except:
            if adc_out == 1:
                return self.height_pot_adc
            else:
                return self.height_pot
    
    
    def interpolate_height_data(self, x):
            try:
                self.points_list = self.config_data['Load Cell\nHeight']['points_list']
                adc_points = [x[0] for x in self.points_list]
                real_points = [x[1] for x in self.points_list]
            except:
                return x*self.slope+self.intercept

            if x > max(adc_points) or x < min(adc_points) or len(adc_points)<3:
                return x*self.slope+self.intercept

            else:
                adc_points.append(x)
                lst = sorted(adc_points)

                x1 = lst[lst.index(x)-1]
                x2 = lst[lst.index(x)+1]

                adc_points.remove(x)

                y1 = real_points[adc_points.index(x1)]
                y2 = real_points[adc_points.index(x2)]

                y = y1+(x-x1)*((y2-y1)/(x2-x1))

                return y
