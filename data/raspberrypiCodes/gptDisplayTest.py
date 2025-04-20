import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# Use I2C0
i2c = busio.I2C(board.SCL, board.SDA)  # GPIO 1 and GPIO 0

oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.show()

image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)
draw.text((0, 0), "System Ready", fill=255)
oled.image(image)
oled.show()
