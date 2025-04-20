import serial
import pynmea2

# Open serial connection
port = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)

while True:
    try:
        data = port.readline().decode('ascii', errors='replace')
        if data.startswith('$GPGGA') or data.startswith('$GPRMC'):
            msg = pynmea2.parse(data)
            print(f"Timestamp: {msg.timestamp}")
            print(f"Latitude: {msg.latitude} {msg.lat_dir}")
            print(f"Longitude: {msg.longitude} {msg.lon_dir}")
            print(f"Satellites: {getattr(msg, 'num_sats', 'N/A')}")
            print("-" * 30)
    except pynmea2.ParseError:
        continue
    except KeyboardInterrupt:
        print("Exiting...")
        break
