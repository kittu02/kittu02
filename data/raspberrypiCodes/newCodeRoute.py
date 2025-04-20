import time
import requests
from PIL import Image
import firebase_admin
from firebase_admin import credentials, firestore
import board
import busio
import adafruit_ssd1306
import os

# === OLED Setup ===
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.show()

# === Firebase Setup ===
cred = credentials.Certificate("/home/kirtan/helmet-d508c-firebase-adminsdk-fbsvc-e149af3635.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# === HERE API Key ===
HERE_API_KEY = "0c1Ca68_mhEPNQzRVgDMhu5AqmCry1ytvGdmv3YCwzA"

# === Global Variables ===
destination_coords = {"latitude": 0.0, "longitude": 0.0}
current_coords = {"latitude": 0.0, "longitude": 0.0}
image_dir = "/home/kirtan/images"

# === Firebase Realtime Listener for Destination ===
def on_snapshot(doc_snapshot, changes, read_time):
    global destination_coords
    for doc in doc_snapshot:
        data = doc.to_dict()
        if "searchedLocation" in data:
            destination_coords = data["searchedLocation"]
            print(f"New Destination: {destination_coords}")

doc_ref = db.collection("locations").document("A1m2c4n88")
doc_ref.on_snapshot(on_snapshot)

print("Listening for location and navigation updates...")

# === HERE API Route Fetch ===
def get_direction_from_here_api(current_lat, current_lng, dest_lat, dest_lng):
    url = (
        f"https://router.hereapi.com/v8/routes?"
        f"transportMode=scooter"
        f"&origin={current_lat},{current_lng}"
        f"&destination={dest_lat},{dest_lng}"
        f"&return=polyline,actions,instructions"
        f"&apiKey={HERE_API_KEY}"
    )

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "routes" in data and len(data["routes"]) > 0:
            actions = data["routes"][0]["sections"][0].get("actions", [])
            if actions:
                direction = actions[0].get("direction", "forward")
                print(f"Next Direction: {direction}")
                return direction
    print("No direction found.")
    return None

# === Display image on OLED based on direction ===
def display_direction_image(direction):
    filename = f"{direction}.bmp"
    path = os.path.join(image_dir, filename)

    if os.path.exists(path):
        try:
            image = Image.open(path).convert("1")
            oled.image(image)
            oled.show()
        except Exception as e:
            print(f"Error displaying {filename}: {e}")
    else:
        print(f"Image not found: {filename}")
        oled.fill(0)
        oled.show()

# === Main Loop ===
while True:
    try:
        doc = db.collection("locations").document("A1m2c4n88").get()
        data = doc.to_dict()
        if "currentLocation" in data:
            current_coords = data["currentLocation"]

        dest_lat = destination_coords["latitude"]
        dest_lng = destination_coords["longitude"]
        cur_lat = current_coords["latitude"]
        cur_lng = current_coords["longitude"]

        if dest_lat != 0.0 and dest_lng != 0.0:
            direction = get_direction_from_here_api(cur_lat, cur_lng, dest_lat, dest_lng)
            if direction:
                display_direction_image(direction)

    except Exception as e:
        print(f"Error in main loop: {e}")

    time.sleep(5)  # Update every 5 seconds
