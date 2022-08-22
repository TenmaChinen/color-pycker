from pystray import Menu, MenuItem, Icon
from PIL import Image


class Stray:
    def __init__(self):
        self.init_stray()
        self.__show_callback = None
        self.__quit_callback = None
        self.__is_first_time = True

    def init_stray(self):
        # set 'Show' as the default action
        menu = Menu(
            MenuItem('Show', self.__on_click_show, default=True),
            MenuItem('Quit', self.__on_click_quit))

        image = Image.open('favicon.ico')
        self.__icon = Icon('name', icon=image, title='title', menu=menu)

    def run(self):
        setup = None
        if self.__is_first_time:
            self.__is_first_time = False
            setup = self.__show_notification
        self.__icon.run(setup=setup)

    def __on_click_show(self):
        if self.__show_callback:
            self.__icon.stop()
            self.__show_callback()

    def __on_click_quit(self):
        if self.__quit_callback:
            self.__icon.stop()
            self.__quit_callback()        

    def set_callbacks(self, show_callback=None, quit_callback=None):
        self.__show_callback = show_callback
        self.__quit_callback = quit_callback

    def __show_notification(self,icon):
        self.__icon.visible = True
        self.__icon.notify(
            title='I will be here!',
            message='Click on the icon to open Color Pycker again.\n Right click on the icon to see other options.'
            )
