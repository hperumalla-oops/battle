#inlcude "config.h"             //parses the config files into huma-readable language
#include <Adafruit_SSD1306.h>  ///for oled
#include <Wire.h>              /// to communicate with I2C devices
#include<Adafruit_Sensor.h>   ///for DHT sensor



#define DHT_PIN 4
#define DHTTYPE DHT11
DHT dht(DHT_PIN, DHTTYPE);


Adafruit_SSD1306 oled(128,32, &Wire);


void setup() 
{
  Serial.begin(115200);
  
  oled.begin(SSD136_SWITCHCAPVCC, 0X3C);
  oled.display();
  oled.setTextSize(1);
  oled.setTextColor(WHITE);
  oled.clearDisplay();
  
}

void loop() 
{
  float t = dht.readTemperature();
  float h = dht.readHumidity();
  
  Serial.print("Temp: ");
  Serial.println(t);
  Serial.print("Humi: ");
  Serial.println(h);

  oled.clearDisplay();
  
  oled.setCursor(0,0);
  oled.print("Temp: ");
  oled.println(t);
  oled.print("Humi: ");
  oled.println(h);
  
  oled.display();
  
  delay(5000);

}
