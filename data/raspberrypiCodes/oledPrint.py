from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from time import sleep
from PIL import Image

def main():
    # Initialize OLED display
    serial = i2c(port=1, address=0x3C)
    device = ssd1306(serial)

    # Get OLED display resolution
    width, height = device.size  # Ensure correct resolution (e.g., 128x64)

    # List of direction images
    images = [
        "forward.jpg",
        "left.jpg",
        "right.jpg",
        "uturn.jpg",
        "location.jpg"
    ]
    
    while True:
        for img_path in images:
            try:
                img = Image.open(img_path).convert("1")  # Convert to 1-bit monochrome
                img = img.resize((width, height))  # Ensure the image matches the OLED size

                # Debugging: Print image size to verify match
                print(f"Displaying: {img_path}, Image Size: {img.size}, OLED Size: {device.size}")

                device.display(img)  # Display image on OLED
                sleep(1.5)  # Show each image for 1.5 seconds
            except Exception as e:
                print(f"Error displaying {img_path}: {e}")  # Handle missing or incorrect images

if __name__ == "__main__":
    main()
