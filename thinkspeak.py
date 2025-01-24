import requests
import time
import board
import adafruit_dht

api_key = "J6WDF39BE27DX1H"
sensor = adafruit_dht.DHT11(board.D4)  ##for GPIO4

a = 10

while a:
    temperature = sensor.temperature
    humidity = sensor.humidity
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
