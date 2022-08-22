from tkinter import Tk, Frame, Label, Button
from tkinter import LEFT, RIGHT, TOP, BOTTOM

BG_HEAD = '#404040'
BG_FOOT = '#565656'

d_txt_head = dict(font='Arial 18 bold', fg='white', bg=BG_HEAD, bd=0)
# d_lbl_foot = dict(**d_font, fg='white', bg=BG_FOOT, bd=0)
d_btn_foot = dict(font='Arial 14 bold', fg='white',
                  bg=BG_FOOT, relief='raised', bd=1)
d_btn_toggle_foot = dict(font='Arial 20 bold', fg='white',
                         bg=BG_FOOT, relief='raised', bd=1)

d_head = dict(bg=BG_HEAD)
d_foot = dict(bg=BG_FOOT)


class Layout:

    def __init__(self, w=300, h=250):
        self.__create_root(w, h)
        self.__create_head()
        self.__create_body()
        self.__create_foot()
        self.__set_bindings()
        self.__on_toggle_callback = None
        self.__on_select_color_callback = None
        self.__on_close_window_callback = None
        self._w = w
        self._h = h

    def __create_root(self, w, h):
        self._root = Tk()
        self._root.wm_title('Color Picker')
        self._root.resizable(False, False)
        self._root.wm_attributes('-topmost', True)
        self._root.geometry(f'{w}x{h}')
        self._root.config(bg='red', highlightthickness=2)
        self._root.overrideredirect(True)

    def __hide_window(self):
        self._root.withdraw()
        if self.__on_close_window_callback:
            self.__on_close_window_callback()

    def start_layout(self):
        self._root.mainloop()

    def __create_head(self):
        self.__fr_head = Frame(master=self._root, **d_head)
        self.__fr_head.pack(side=TOP, fill='x')

        self.__lbl_title = Label(
            master=self.__fr_head, text='Color Pycker', **d_txt_head)
        self.__lbl_title.pack(side=LEFT, padx=(10, 0))

        btn_close = Button(master=self.__fr_head, text='✖', **d_txt_head)
        btn_close['command'] = self.__hide_window
        btn_close.pack(side=RIGHT)

    def __create_body(self):
        self.__fr_body = Frame(
            master=self._root, bg='black', highlightthickness=1)
        self.__fr_body.pack(side=TOP, fill='both', expand=True)

    def __create_foot(self):
        fr_foot = Frame(master=self._root, **d_foot)
        fr_foot.pack(side=TOP, fill='x')

        fr_foot.grid_columnconfigure(0, weight=10)
        fr_foot.grid_columnconfigure(1, weight=1)

        self.__btn_clr_hex = Button(
            master=fr_foot, text='#000000', **d_btn_foot)
        self.__btn_clr_hex['command'] = lambda x = 'hex': self.__on_click_button(
            x)
        self.__btn_clr_hex.grid(row=0, column=0, sticky='news')

        self.__btn_clr_rgb = Button(
            master=fr_foot, text='rgb(0,0,0)', **d_btn_foot)
        self.__btn_clr_rgb['command'] = lambda x = 'rgb': self.__on_click_button(
            x)
        self.__btn_clr_rgb.grid(row=1, column=0, sticky='news')

        self.__btn_toggle = Button(
            master=fr_foot, text='P', width=3,  **d_btn_toggle_foot)
        self.__btn_toggle['command'] = self.__toggle_pick
        self.__btn_toggle.grid(row=0, column=1, rowspan=2, sticky='news')

    def __on_click_button(self, option):
        if self.__on_select_color_callback:
            color = self.__btn_clr_hex['text'] if option == 'hex' else self.__btn_clr_rgb['text']
            self.__on_select_color_callback(color)

    def __toggle_pick(self):
        state = self.__btn_toggle['relief'] != 'sunken'
        self.set_toggle_state(state)
        if self.__on_toggle_callback:
            self.__on_toggle_callback(state)

    def __set_bindings(self):
        self.__bind_group('<Button-1>', self.__start_move)
        self.__bind_group('<B1-Motion>', self.__on_motion)

    def __bind_group(self, sequence, callback):
        self.__fr_head.bind(sequence, callback)
        self.__lbl_title.bind(sequence, callback)

    def __start_move(self, event):
        self._x_start = event.x
        self._y_start = event.y

    def __on_motion(self, event):
        x_delta = event.x - self._x_start
        y_delta = event.y - self._y_start

        x_master = self._root.winfo_x()
        y_master = self._root.winfo_y()

        x_new, y_new = int(x_master + x_delta), int(y_master + y_delta)

        self._root.geometry(f'+{x_new}+{y_new}')

    def set_callbacks(self,
                      on_toggle_callback=None,
                      on_select_color_callback=None,
                      on_close_window_callback=None):
        self.__on_toggle_callback = on_toggle_callback
        self.__on_select_color_callback = on_select_color_callback
        self.__on_close_window_callback = on_close_window_callback

    def set_toggle_state(self, state):
        self.__btn_toggle['relief'] = 'sunken' if state else 'raised'

    def set_picker_color(self, color_hex, color_rgb):
        self.__btn_clr_hex['text'] = color_hex
        self.__btn_clr_rgb['text'] = color_rgb
        self.__fr_body['bg'] = color_hex

    def get_root_pos(self):
        return self._root.winfo_x(), self._root.winfo_y()

    def is_inside(self, x, y):
        x_app, y_app = self.get_root_pos()
        return (x >= x_app) and (x <= (x_app + self._w)) and (y >= y_app) and (y <= (y_app + self._h))

    def show(self):
        self._root.deiconify()

    def hide(self):
        self._root.withdraw()

    def finish(self):
        self._root.destroy()

    def copy_to_clipboard(self,string):
        self._root.clipboard_clear()
        self._root.clipboard_append(string)
        self._root.update()
        print('DEBUG B')

