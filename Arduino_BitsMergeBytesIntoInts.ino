#include <SoftwareSerial.h>


//Tested to work on 8/1/2014:


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly: 
  int bigNo=674;
  byte readInYGyroL=lowByte(bigNo);
  byte readInYGyroH=highByte(bigNo);
  int gyroYReading=(int)(readInYGyroL+(readInYGyroH<<8));
  
  Serial.println("Big no is: " + String(bigNo));
  Serial.println("Big reconstructed is: "+String(gyroYReading));
}
