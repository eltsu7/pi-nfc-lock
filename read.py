import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

reader = SimpleMFRC522()

try:
    while True:
        id = reader.read_id()
        print(id)
        # requests
        time.sleep(1)

finally:
    GPIO.cleanup()
