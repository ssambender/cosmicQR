import time
from cosmic import CosmicUnicorn
from picographics import PicoGraphics, DISPLAY_COSMIC_UNICORN as DISPLAY
from uQR import QRCode

cu = CosmicUnicorn()
graphics = PicoGraphics(DISPLAY)

# create QR code
qr = QRCode()
# set the data/link
qr.add_data('http://sambender.net')
# genereate true/false matrix representation
matrix = qr.get_matrix()

def draw_pixel(x, y):
    graphics.set_pen(graphics.create_pen(255, 255, 255))  # white pen
    graphics.pixel(x, y)

cu.set_brightness(0.5)

# Set the font and clear the display
graphics.set_font("bitmap8")
graphics.set_pen(graphics.create_pen(0, 0, 0))  # black background
graphics.clear()

# set pixels
for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        if matrix[y][x]:  # if true, draw white pixel
            draw_pixel(x, y)

# update the display
cu.update(graphics)

print("done")
