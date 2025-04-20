import time 
import requests
from PIL import Image
import board
import busio
import adafruit_ssd1306
import os

# === OLED Setup ===
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.show()

# === HERE API Key ===
HERE_API_KEY = "0c1Ca68_mhEPNQzRVgDMhu5AqmCry1ytvGdmv3YCwzA"

# === Image Directory ===
image_dir = "/home/kirtan/images"

# === Coordinates for Route ===
origin = (22.367317,70.7947037)       # From
destination = (22.2795778,70.7632828)  # To

# === Fetch directions from HERE API ===
def get_route_directions(origin_lat, origin_lng, dest_lat, dest_lng):
    url = (
        f"https://router.hereapi.com/v8/routes?"
        f"transportMode=scooter"
        f"&origin={origin_lat},{origin_lng}"
        f"&destination={dest_lat},{dest_lng}"
        f"&return=polyline,actions,instructions"
        f"&apiKey={HERE_API_KEY}"
    )
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "routes" in data and len(data["routes"]) > 0:
            return data["routes"][0]["sections"][0].get("actions", [])
    return []

# === Show image for each direction ===
def display_direction_image(direction):
    filename = f"{direction}.bmp"
    path = os.path.join(image_dir, filename)

    if os.path.exists(path):
        try:
            image = Image.open(path).convert("1")
            oled.image(image)
            oled.show()
            print(f"? Displayed image: {filename}")
        except Exception as e:
            print(f"? Error displaying image {filename}: {e}")
    else:
        print(f"? Image not found: {filename}")
        oled.fill(0)
        oled.show()

# === Main Execution ===
actions = get_route_directions(origin[0], origin[1], destination[0], destination[1])

if not actions:
    print("? No directions received from HERE API.")
else:
    for index, action in enumerate(actions):
        direction = action.get("direction", "forward")
        instruction = action.get("instruction", "No instruction")

        print(f"\n? Step {index + 1}")
        print(f"Direction: {direction}")
        print(f"Instruction: {instruction}")

        display_direction_image(direction)
        time.sleep(5)
