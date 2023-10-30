from kivy.uix.textinput import TextInput

class StrInput(TextInput):
    def validate(self):
        notempty = len(self.text) > 0 # String is not empty or all whitespace
        notspace = not self.text.isspace()
        test = notempty and notspace
        if test:
            self.show_valid()
        else:
            self.show_invalid()
        return test

    def show_invalid(self):
        self.background_color = (1, .7, .7, 1)

    def show_valid(self):
        self.background_color = (1, 1, 1, 1)
