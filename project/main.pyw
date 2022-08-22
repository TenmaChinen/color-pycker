from events import MouseEvent
from layout import Layout
from stray import Stray
import pil_color
import mouse

def mouse_callback(x, y):
    if not layout.is_inside(x, y):
        color_hex, color_rgb = pil_color.get_position_color(x, y)
        mouse_event.disable_mouse_events()
        layout.set_toggle_state(state=False)
        layout.set_picker_color(color_hex, color_rgb)


def toggle_callback(is_active):
    if is_active:
        mouse_event.enable_mouse_events()
    else:
        mouse_event.disable_mouse_events()


def on_color_selected(color):
    layout.copy_to_clipboard(string=color)


def on_close_window():
    stray.init_stray()
    stray.run()

mouse_event = MouseEvent()
mouse_event.set_mouse_callback(callback=mouse_callback)
# mouse_event.enable_mouse_events()

layout = Layout(w=350, h=300)
layout.set_callbacks(
    on_toggle_callback=toggle_callback,
    on_select_color_callback=on_color_selected,
    on_close_window_callback=on_close_window)

stray = Stray()
stray.set_callbacks(
    show_callback=layout.show,
    quit_callback=layout.finish
)

layout.start_layout()
