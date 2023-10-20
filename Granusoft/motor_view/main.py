from kivy.config import Config as KivyConfig
from kivy.app import App

from MotorView import MotorView

# Kivy Configuration
KivyConfig.set('kivy', 'desktop', 0) # Disable OS-specific features for testing
KivyConfig.set('kivy', 'keyboard_mode', 'systemanddock') # Allow barcode scanner and
                                                         # on screen keyboard
KivyConfig.set('graphics', 'height', 480) # Set window size to be the same as touchscreen
KivyConfig.set('graphics', 'width', 800)  # (not used when fullscreen enabled)
KivyConfig.set('kivy', 'kivy_clock', 'default')
KivyConfig.set('graphics', 'maxfps', 60)
KivyConfig.write()

class MotorApp(App):
    def build(self):
        root = MotorView()
        return root

if __name__ == "__main__":
    MotorApp().run()
