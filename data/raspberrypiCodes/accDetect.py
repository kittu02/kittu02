from smbus2 import SMBus
import time

MPU9250_ADDR = 0x68
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B

def read_raw_data(bus, addr):
    high = bus.read_byte_data(MPU9250_ADDR, addr)
    low = bus.read_byte_data(MPU9250_ADDR, addr+1)
    value = (high << 8) | low
    if value > 32768:
        value -= 65536
    return value

with SMBus(1) as bus:  # I2C1
    # Wake up MPU9250
    bus.write_byte_data(MPU9250_ADDR, PWR_MGMT_1, 0)
    print("MPU9250 initialized.")

    while True:
        accel_x = read_raw_data(bus, ACCEL_XOUT_H) / 16384.0
        accel_y = read_raw_data(bus, ACCEL_XOUT_H+2) / 16384.0
        accel_z = read_raw_data(bus, ACCEL_XOUT_H+4) / 16384.0
        
        total_acc = (accel_x**2 + accel_y**2 + accel_z**2)**0.5

        print(f"Acceleration: {total_acc:.2f}g")

        if total_acc > 2.5:  # Adjust threshold as needed
            print("?? Accident Detected!")

        time.sleep(0.2)
