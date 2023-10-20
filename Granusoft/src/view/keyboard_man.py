"""
The keyboard manager adds the ability to change keyboard layouts depending on the current
screen.  For example, the plot number screen uses a "numeric" keyboard (number pad),
while the operator uses a "text" keyboard (qwerty).
"""

from kivy.core.window import Window

keyboard = None

def show_keyboard(caller, layout):
    """Shows a keyboard with the specified layout.

    The folder view/keyboard_layouts contains keyboard layouts used in this software,
    including 'numeric' (number pad) and 'text' (qwerty).  These are custom keyboard
    layouts.  Kivy contains its own keyboard layouts; however, Kivy's layouts are
    designed for multi-touch screens."""
    kb = Window.request_keyboard(_close_keyboard, caller)
    if kb.widget:
        keyboard = kb.widget
        if layout=='numeric':
            keyboard.layout = "view/keyboard_layouts/numeric.json"
            keyboard.margin_hint = [0.05, 0.2, 0.05, 0.2]
        elif layout=='integer':
            keyboard.layout = "view/keyboard_layouts/integer.json"
            keyboard.margin_hint = [0.05, 0.2, 0.05, 0.2]
        elif layout=='text':
            keyboard.layout = "view/keyboard_layouts/text.json"
            keyboard.margin_hint = [0.05, 0.06, 0.05, 0.06]
        else:
            keyboard.layout = layout
            keyboard.margin_hint = [0.05, 0.06, 0.05, 0.06]

        # Using internal members is probably not the best way to do this.  But...
        # Turn off capslock each time a new keyboard is requested
        keyboard.have_capslock = False
        keyboard.active_keys.clear()
        keyboard.refresh_active_keys_layer()
    else:
        keyboard = kb

def _close_keyboard():
    """When the keyboard is closed, clear the keyboard global."""
    global keyboard
    if keyboard:
        keyboard = None
