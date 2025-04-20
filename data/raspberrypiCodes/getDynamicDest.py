import firebase_admin
from firebase_admin import credentials, firestore
import serial
import time
import pynmea2
import requests

# Initialize Firebase Admin SDK
cred = credentials.Certificate("/home/kirtan/helmet-d508c-firebase-adminsdk-fbsvc-e149af3635.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# HERE API Credentials
HERE_API_KEY = "0c1Ca68_mhEPNQzRVgDMhu5AqmCry1ytvGdmv3YCwzA"

# GPS module configuration
# port = "/dev/ttyAMA0"
# ser = serial.Serial(port, baudrate=9600, timeout=0.5)

# Global variable for searched location
destination_coords = {"latitude": 0.0, "longitude": 0.0}

# Firebase Real-time Listener
def on_snapshot(doc_snapshot, changes, read_time):
    global destination_coords
    for doc in doc_snapshot:
        data = doc.to_dict()
        if "searchedLocation" in data:
            destination_coords = data["searchedLocation"]
            print(f"? New Destination Received: {destination_coords}")

# Set up real-time listener on the "devices" collection
doc_ref = db.collection("locations").document("A1m2c4n88")
doc_ref.on_snapshot(on_snapshot)

print("Listening for real-time updates and GPS location...")

def get_directions(lat, lng):
    """Fetches turn-by-turn directions from HERE API."""
    dest_lat, dest_lng = destination_coords["latitude"], destination_coords["longitude"]

    if dest_lat == 0.0 and dest_lng == 0.0:
        return ["?? No destination set yet!"]

    url = f"https://router.hereapi.com/v8/routes?transportMode=scooter&origin={lat},{lng}&destination={dest_lat},{dest_lng}&return=polyline,actions,instructions&apiKey={HERE_API_KEY}"
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
            return ["No routes found."]
    return ["API request failed."]

while True:
#    newdata = ser.readline().decode('ascii', errors='ignore').strip()

#    if newdata.startswith("$GPRMC"):
        try:
#            newmsg = pynmea2.parse(newdata)
#            lat, lng = newmsg.latitude, newmsg.longitude
#            print(f"? Current Location: Latitude={lat}, Longitude={lng}")

            # Fetch and display turn-by-turn navigation
            directions = get_directions(22.3674523,70.7974323)
            for i, step in enumerate(directions):
                print(f" Step {i+1}: {step}")

        except pynmea2.ParseError:
            print("?? Error parsing GPS data")

        time.sleep(5)  # Update every 5 seconds
