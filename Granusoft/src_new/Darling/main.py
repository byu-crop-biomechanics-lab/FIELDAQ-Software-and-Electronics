from kivy.config import Config as KivyConfig
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition, NoTransition

import configurator as config

# Kivy Configuration
KivyConfig.set('kivy', 'desktop', 0) # Disable OS-specific features for testing
KivyConfig.set('kivy', 'keyboard_mode', 'systemanddock') # Allow barcode scanner and
                                                         # on screen keyboard
KivyConfig.set('graphics', 'height', 480) # Set window size to be the same as touchscreen
KivyConfig.set('graphics', 'width', 800)  # (not used when fullscreen enabled)
CLOCK_TYPE = "default"
KivyConfig.set('kivy', 'kivy_clock', CLOCK_TYPE)
KivyConfig.set('graphics', 'maxfps', 250)
KivyConfig.write()

class GranuScreenManager(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        sm = GranuScreenManager(transition=NoTransition())
        return sm

if __name__ == "__main__":
    config.load() # Load our own app preferences
    # Run the App
    MainApp().run()
