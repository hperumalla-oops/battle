#include "config.h"
#include <Adafruit_SSD1306.h>
#include <SPI.h>


#define BUZZER_PIN 2
#define ECHO_PIN 14
#define TRIGGER_PIN 12
#define SDA_PIN 4
#define SCL_PIN 5
#define DISTANCE_THRESHOLD 10

long duration;
float distance;

// OLED display and I2C address
Adafruit_SSD1306 oled(128,32,&Wire)

void setup() {
  // Initialize OLED display
  oled.begin(SSD1306_SWITCHCAPVCC, 0x3c);
  oled.display();
  oled.setColor(WHITE);
  oled.setTextSize(1);
  oled.clearDisplay();

  Serial.begin(115200);

  // Initialize ultrasonic sensor pins
  pinMode(TRIGGER_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
}

void loop() {
  // Send a pulse to the trigger pin
  digitalWrite(TRIGGER_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIGGER_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGGER_PIN, LOW);
  
  // Measure the duration of the pulse on the echo pin
  duration = pulseIn(ECHO_PIN, HIGH);

  // Calculate the distance in centimeters using the speed of sound
  distance = duration / 58.2;

  Serial.print("Duration:");
  Serial.print(duration);
  Serial.println(" sec");
  Serial.print("Distance:");
  Serial.print(distance);
  Serial.println(" cm");
  
  // If the distance is below the threshold, turn on the buzzer
  if (distance < DISTANCE_THRESHOLD)
    tone(BUZZER_PIN,1000);
  else 
    noTone(BUZZER_PIN);

  // Display the distance on the OLED display
  oled.clearDisplay();
  oled.setCursor(0,0);
  oled.print("Distance:");
  oled.print(distance);
  oled.println(" cm");
  oled.display();


  delay(5000);
}
