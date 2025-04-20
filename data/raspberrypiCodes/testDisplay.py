import os
import time
from PIL import Image
import board
import busio
import adafruit_ssd1306

# Initialize I2C and OLED
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Directory containing your .bmp images
image_dir = "/home/kirtan/images"

# Clear OLED
oled.fill(0)
oled.show()

# Get list of .bmp files
bmp_files = [f for f in os.listdir(image_dir) if f.endswith(".bmp")]

if not bmp_files:
    print("? No BMP images found!")
else:
    for bmp_file in bmp_files:
        try:
            # Load and show image
            path = os.path.join(image_dir, bmp_file)
            image = Image.open(path).convert("1")
            oled.image(image)
            oled.show()

            print(f"? Displaying: {bmp_file}")
            time.sleep(2)

        except Exception as e:
            print(f"? Error displaying {bmp_file}: {e}")

# Optionally clear OLED at end
oled.fill(0)
oled.show()
