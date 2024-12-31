import requests
import time
import Adafruit_DHT

api_key = "J6WDF39BE27DX1H"

pin = 4
sensor = Adafruit_DHT.DHT11

i = 10

while a:
    humidity, temperature = Adafruit_DHT.read(sensor, pin)
    payload = {'api_key': api_key, 
               'field1': str(temperature),
                'field2': str(humidity)}
    req = requests.post("https://api.thingspeak.com/update?-api_key=J6WDF39BE27DX1H&field1=0", params=payload)
    if req.status_code == requests.codes.ok:
        print("Data successfully updated")
    else:
        print("Error in the code")
    a=a-1
    time.sleep(10)