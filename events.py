from mouse import get_position as get_mouse_position
from mouse import ButtonEvent as MouseButtonEvent
from mouse import unhook as remove_mouse_hook
from mouse import hook as add_mouse_hook

class MouseEvent:

    def __init__(self):
        self._callback = None
        self.is_enabled = False

    def set_mouse_callback(self,callback):
        self._callback = callback

    def enable_mouse_events(self):
        add_mouse_hook(self.__on_mouse_event)
        self.is_enabled = True

    def disable_mouse_events(self):
        remove_mouse_hook(self.__on_mouse_event)
        self.is_enabled = False

    def __on_mouse_event(self,event):
        if type(event) is not MouseButtonEvent:
            return

        if event.button == 'left' and event.event_type != 'up':
            if self._callback :
                x, y = get_mouse_position()
                self._callback(x, y)