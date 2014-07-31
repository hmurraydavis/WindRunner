//Include libraries:
#include <SoftwareSerial.h>
#include <Wire.h>

//define globals
int gyroAddress=0x68; //from I2C scanner

void setup() {
  // put your setup code here, to run once:
  Wire.begin();
  Serial.begin(9600);
}

int readFromGyro(int readFromAddress){
  Wire.beginTransmission(gyroAddress);
  Wire.write(readFromAddress);
  Wire.endTransmission();
  
  Wire.requestFrom(gyroAddress, 1);
  int readIn=Wire.read();
}

void writeToGyro(int writeToAddress, int writeValue){
  Wire.beginTransmission(gyroAddress);
  Wire.write(writeToAddress);
  Wire.endTransmission();
  
  Wire.beginTransmission(gyroAddress);
  Wire.write(writeValue);
  Wire.endTransmission();
}

void loop() { 
  //Gyro:
    int tempL=66;
    int whoAmI=117;
    int pwrMgmt1=107;
      int valueNoSleepPwrMgmt1=B00000000; //disables sleep (6) and cycle (5)
    int pwrMgmt2=108;
      int activateYaxisPwrMgmt2=B10111100;
    
  int readInWhoAmI=readFromGyro(whoAmI);
  Serial.println(readInWhoAmI);
 
  Serial.println("Transmission");
  
  delay (9); 
}
