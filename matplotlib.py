import adafruit_DHT
import matplotlib.pyplot as plt
import time
import board


sensor = adafruit_DHT.DHT11(board.D4)
a = 10

temperature_data = []
humidity_data = []

while a:
    T = sensor.temperature
    H = sensor.humidity
    temperature_data.append(T)
    humidity_data.append(H)
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
