from PIL.ImageGrab import grab as image_grab
from ctypes import windll

# Fix PIL dpi issue
windll.user32.SetProcessDPIAware()

def get_position_color(x, y):
    image_pil = image_grab(bbox=(x, y, x+1, y+1))

    color_rgb = image_pil.getpixel((0, 0))
    color_hex = '#%02x%02x%02x' % (color_rgb)
    color_hex = color_hex.upper()
    r, g, b = color_rgb
    return color_hex, f'rgb({r}, {g}, {b})'


if __name__ == '__main__':
    color_hex, color_rgb = get_position_color(10, 10)
    print(color_hex, color_rgb)
