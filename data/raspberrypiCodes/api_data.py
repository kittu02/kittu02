
import serial
import time
import pynmea2
import requests

# HERE API Credentials (Replace with your actual API key)
HERE_API_KEY = "0c1Ca68_mhEPNQzRVgDMhu5AqmCry1ytvGdmv3YCwzA"

# Set your fixed destination coordinates (update as needed)
DEST_LAT, DEST_LNG = 21.9532623, 70.7869017  # Example: To Dasi Jivan

# GPS module configuration
port = "/dev/ttyAMA0"
ser = serial.Serial(port, baudrate=9600, timeout=0.5)

def get_directions(lat, lng):
    """Fetches turn-by-turn directions from HERE API for a scooter."""
    url = f"https://router.hereapi.com/v8/routes?transportMode=scooter&origin={lat},{lng}&destination={DEST_LAT},{DEST_LNG}&return=polyline,actions,instructions&apiKey={HERE_API_KEY}"
    
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
            return ["Error: No routes found"]
    
    return ["Error: API request failed"]

while True:
    newdata = ser.readline().decode('ascii', errors='ignore').strip()

    if newdata.startswith("$GPRMC"):  # Process only GPRMC sentences
        try:
            newmsg = pynmea2.parse(newdata)
            lat, lng = newmsg.latitude, newmsg.longitude
            print(f"? Current Location: Latitude={lat}, Longitude={lng}")

            # Fetch turn-by-turn scooter navigation
            directions = get_directions(lat, lng)
            for i, step in enumerate(directions):
                print(f"? Step {i+1}: {step}")

        except pynmea2.ParseError:
            print("Error parsing GPS data")

    time.sleep(5)  # Update every 5 seconds
