#include <SoftwareSerial.h>
#include <Wire.h>


void setup() {
  // put your setup code here, to run once:
  Wire.begin();
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly: 
  int gyroAddress=0x68; //from I2C scanner
  int whoAmIReg=117;
  Wire.beginTransmission(gyroAddress);
  Wire.write(whoAmIReg);
  //char byte1=Wire.read();
  //char byte2=Wire.read();
  //char byte3=Wire.read();
  Wire.endTransmission();
  
  Wire.requestFrom(gyroAddress, 1);
  Serial.println(Wire.read());
 
  
  Serial.println("Transmission");
  //Serial.println(String(byte1));
  //Serial.println(byte2);
  //Serial.println(byte3);
  
  delay (9); 
}
