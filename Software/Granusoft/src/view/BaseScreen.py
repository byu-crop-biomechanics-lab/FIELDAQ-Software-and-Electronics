from kivy.uix.screenmanager import Screen

class BaseScreen(Screen):
    '''Keeps track of the screen history to allow users to move to the previous screen,
    rather than having to specify which screen to move to each time.'''

    screen_history = []

    def move_to(self, screen_name):
        '''Add the current screen to the screen history and move to a new screen.  If we
        are moving to the previous screen, remove it from the screen history.'''
        if self.screen_history and self.screen_history[-1] == screen_name:
            # Make sure to pop the stack if we're moving back to the previous screen
            self.back()
        else:
            self.screen_history.append(self.name)
            self.manager.current = screen_name

    def back(self):
        '''Go to the previous screen.'''
        self.manager.current = self.screen_history.pop()
