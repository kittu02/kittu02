import time
from smbus2 import SMBus
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont

# MPU9250 on I2C1 (GPIO 2=SDA1, GPIO 3=SCL1)
bus_mpu = SMBus(1)
MPU_ADDR = 0x68
bus_mpu.write_byte_data(MPU_ADDR, 0x6B, 0)  # Wake up MPU9250

# OLED on I2C0 (GPIO 0=SDA0, GPIO 1=SCL0)
serial = i2c(port=0, address=0x3C)  # port=0 ? I2C0
device = ssd1306(serial)

# Optional: Custom font
# font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
font = ImageFont.load_default()

def read_raw(bus, addr):
    high = bus.read_byte_data(MPU_ADDR, addr)
    low = bus.read_byte_data(MPU_ADDR, addr + 1)
    value = (high << 8) | low
    if value > 32768:
        value -= 65536
    return value

def get_acceleration():
    acc_x = read_raw(bus_mpu, 0x3B) / 16384.0
    acc_y = read_raw(bus_mpu, 0x3D) / 16384.0
    acc_z = read_raw(bus_mpu, 0x3F) / 16384.0
    return acc_x, acc_y, acc_z

while True:
    acc_x, acc_y, acc_z = get_acceleration()
    total_acc = (acc_x**2 + acc_y**2 + acc_z**2)**0.5

    with canvas(device) as draw:
        draw.text((0, 0), "MPU9250 Status", font=font, fill=255)
        draw.text((0, 15), f"Accel: {total_acc:.2f}g", font=font, fill=255)

        if total_acc > 2.5:
            draw.text((0, 35), "?? Accident Detected!", font=font, fill=255)
            print("?? Accident Detected!")
        else:
            draw.text((0, 35), "Normal Movement", font=font, fill=255)

    time.sleep(0.3)
