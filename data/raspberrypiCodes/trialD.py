from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from PIL import Image, ImageDraw, ImageFont
import time

# Initialize the display
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, width=128, height=64)

# Load default font
font = ImageFont.load_default()

# Constants
TOP_HEIGHT = 38  # Arrow area
BOTTOM_HEIGHT = 26  # Text area
WIDTH = 128
HEIGHT = 64

# Arrow Drawing Functions
def draw_arrow(draw, arrow_type, frame):
    center_x = WIDTH // 2
    base_y = TOP_HEIGHT - 5

    if arrow_type == "go_straight":
        # Animate the arrow's height
        arrow_height = 10 + frame % 10
        draw.polygon([
            (center_x - 5, base_y - arrow_height),
            (center_x + 5, base_y - arrow_height),
            (center_x + 5, base_y),
            (center_x + 10, base_y),
            (center_x, base_y + 10),
            (center_x - 10, base_y),
            (center_x - 5, base_y)
        ], outline="white", fill="white")

    elif arrow_type == "turn_left":
        draw.line((center_x + 10, base_y, center_x - 20, base_y), fill="white", width=2)
        draw.polygon([(center_x - 25, base_y), (center_x - 15, base_y - 5), (center_x - 15, base_y + 5)], fill="white")

    elif arrow_type == "turn_right":
        draw.line((center_x - 10, base_y, center_x + 20, base_y), fill="white", width=2)
        draw.polygon([(center_x + 25, base_y), (center_x + 15, base_y - 5), (center_x + 15, base_y + 5)], fill="white")

    elif arrow_type == "u_turn":
        r = 15 + frame % 5
        draw.arc([center_x - r, base_y - r, center_x + r, base_y + r], start=0, end=180, fill="white")
        draw.line((center_x, base_y, center_x, base_y + 10), fill="white", width=2)
        draw.polygon([(center_x - 5, base_y + 10), (center_x + 5, base_y + 10), (center_x, base_y + 15)], fill="white")

# Text Display Function
def draw_text(draw, direction, distance):
    text_y = TOP_HEIGHT + 2
    draw.text((5, text_y), f"Direction: {direction}", font=font, fill="white")
    draw.text((5, text_y + 12), f"Distance: {distance}", font=font, fill="white")

# Main loop
directions = [
    ("go_straight", "Straight", "400m"),
    ("turn_left", "Turn Left", "200m"),
    ("turn_right", "Turn Right", "350m"),
    ("u_turn", "U Turn", "100m")
]

while True:
    for arrow_type, label, distance in directions:
        for frame in range(10):  # 10 frames of animation
            image = Image.new("1", (WIDTH, HEIGHT))
            draw = ImageDraw.Draw(image)

            # Draw the animated arrow
            draw_arrow(draw, arrow_type, frame)

            # Draw the bottom text
            draw_text(draw, label, distance)

            device.display(image)
            time.sleep(0.1)
