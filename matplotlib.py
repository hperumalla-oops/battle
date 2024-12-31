import Adafruit_DHT
import matplotlib.pyplot as plt
import time


sensor = Adafruit_DHT.DHT11
pin = 4
a = 10

temperature_data = []
humidity_data = []

while a:
    humidity, temperature = Adafruit_DHT.read(sensor, pin)
    temperature_data.append(temperature)
    humidity_data.append(humidity)
    time.sleep(5)
    a -= 1

plt.plot(temperature_data, 'r')
plt.xlabel('No of Iterations')
plt.ylabel('Temperature')
plt.title('Temperature Graph')
plt.show()

plt.bar(range(len(humidity_data)), humidity_data)
plt.xlabel('No of Iterations')
plt.ylabel('Humidity')
plt.title('Humidity Graph')
plt.show()