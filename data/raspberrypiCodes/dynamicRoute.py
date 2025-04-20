import firebase_admin
from firebase_admin import credentials, firestore
import time
import requests

import board
import busio
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw, ImageFont

# -------------------- Firebase Setup --------------------
cred = credentials.Certificate("/home/kirtan/helmet-d508c-firebase-adminsdk-fbsvc-e149af3635.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Firebase document reference
doc_ref = db.collection("locations").document("A1m2c4n88")

# -------------------- HERE API Setup --------------------
HERE_API_KEY = "0c1Ca68_mhEPNQzRVgDMhu5AqmCry1ytvGdmv3YCwzA"

# -------------------- OLED Setup --------------------
i2c = busio.I2C(board.SCL, board.SDA)
oled = SSD1306_I2C(128, 64, i2c)
font = ImageFont.load_default()

def display_on_oled(text):
    """Displays text on the OLED screen."""
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, font=font, fill=255)
    
    oled.fill(0)
    oled.image(image)
    oled.show()

# -------------------- HERE Directions Fetch --------------------
def get_directions(origin_lat, origin_lng, dest_lat, dest_lng):
    """Fetch turn-by-turn directions from HERE API."""
    if dest_lat == 0.0 and dest_lng == 0.0:
        return ["? No destination set yet!"]

    url = f"https://router.hereapi.com/v8/routes?transportMode=scooter&origin={origin_lat},{origin_lng}&destination={dest_lat},{dest_lng}&return=polyline,actions,instructions&apiKey={HERE_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "routes" in data and len(data["routes"]) > 0:
            steps = data["routes"][0]["sections"]
            instructions = []
            for section in steps:
                if "actions" in section:
                    for action in section["actions"]:
                        instruction = action.get("instruction", "Continue riding")
                        street_name = action.get("roadName", "")
                        direction = f"? {instruction} on {street_name}" if street_name else f"? {instruction}"
                        instructions.append(direction)
            return instructions
        else:
            return ["? No routes found."]
    return ["? API request failed."]

# -------------------- Main Loop --------------------
print("? Listening to Firebase for location updates...")

while True:
    try:
        doc = doc_ref.get()
        data = doc.to_dict()

        if "currentLocation" in data and "searchedLocation" in data:
            current = data["currentLocation"]
            destination = data["searchedLocation"]

            lat, lng = current["latitude"], current["longitude"]
            dest_lat, dest_lng = destination["latitude"], destination["longitude"]

            print(f"? Current: {lat},{lng} -> Destination: {dest_lat},{dest_lng}")

            directions = get_directions(lat, lng, dest_lat, dest_lng)

            if directions:
                step_1 = directions[0]
                print(f"OLED >> {step_1}")
                display_on_oled(step_1)
            else:
                display_on_oled("No step available.")

        else:
            print("? Missing current/searched location in Firebase.")
            display_on_oled("Waiting for location...")

        time.sleep(5)

    except Exception as e:
        print(f"? Error: {e}")
        display_on_oled("Error occurred.")
        time.sleep(5)
