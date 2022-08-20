import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
from env import api_key, base_url
import requests

reader = SimpleMFRC522()

def validate_id(id):
    parameters = {
        "api_key": api_key,
        "key": id,
    }

    response = requests.get(base_url, params=parameters)
    print(response.text)

try:
    while True:
        id = reader.read_id()
        print(id)
        validate_id(id)
        time.sleep(1)

except KeyboardInterrupt:
    print("Goodbye!")

finally:
    GPIO.cleanup()
