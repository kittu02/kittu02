import RPi.GPIO as GPIO
import time

# Define GPIO pins
SERVO_PIN = 23       # Servo control pin
BUTTON_PIN = 24      # Button input pin

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Pull-down logic

# Initialize PWM
servo = GPIO.PWM(SERVO_PIN, 50)  # 50Hz for servo
servo.start(0)

current_angle = 0  # Start at 0 degrees

def set_angle(angle):
    duty = 2 + (angle / 18)  # Convert angle to duty cycle
    servo.ChangeDutyCycle(duty)
    time.sleep(0.4)
    servo.ChangeDutyCycle(0)

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            current_angle += 15
            if current_angle > 90:
                current_angle = 0
            set_angle(current_angle)
            print(f"Angle set to {current_angle}")
            time.sleep(0.5)  # Debounce delay to avoid multiple triggers

except KeyboardInterrupt:
    print("Exiting...")

finally:
    servo.stop()
    GPIO.cleanup()
