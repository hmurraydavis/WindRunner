#include <SoftwareSerial.h>
#include <Wire.h>


void setup() {
  // put your setup code here, to run once:
  Wire.begin();
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly: 
  Wire.beginTransmission(0X3D);
  char byte1=Wire.read();
  char byte2=Wire.read();
  char byte3=Wire.read();
  Wire.endTransmission();
  
  Serial.println('Transmission');
  Serial.println(byte1);
  Serial.println(byte2);
  Serial.println(byte3);
  
}
