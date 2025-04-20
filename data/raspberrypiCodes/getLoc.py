import serial
import time
import pynmea2

port = "/dev/ttyAMA0"
ser = serial.Serial(port, baudrate=9600, timeout=0.5)

while True:
    newdata = ser.readline().decode('ascii', errors='ignore').strip()
    
    if newdata.startswith("$GPRMC"):  # Check if it's a GPRMC sentence
        try:
            newmsg = pynmea2.parse(newdata)
            lat = newmsg.latitude
            lng = newmsg.longitude
            gps = f"Latitude={lat} and Longitude={lng}"
            print(gps)
        except pynmea2.ParseError:
            print("Error parsing GPS data")
    
    time.sleep(0.5)  # Add a delay to prevent excessive CPU usage
