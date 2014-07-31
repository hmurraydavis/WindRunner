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
     int gyroYH=69;
     int gyroYL=70;
    
  int readInWhoAmI=readFromGyro(whoAmI);
  Serial.println("Who am I: "+String(readInWhoAmI));
  
  writeToGyro(pwrMgmt1,valueNoSleepPwrMgmt1);
  writeToGyro(pwrMgmt2,activateYaxisPwrMgmt2);
  int pwr1St=readFromGyro(pwrMgmt1);
  Serial.println("pwr1St"+String(pwr1St));
  int pwr2St=readFromGyro(pwrMgmt2);
  Serial.println("pwr2St"+String(pwr2St));
  
  int readInYGyroL=readFromGyro(gyroYL);
  Serial.println("Y axis Gyro low value"+String(gyroYL));
  
  int readInYGyroH=readFromGyro(gyroYH);
  Serial.println("Y axis Gyro high value"+String(gyroYH));
  
  Serial.println("Transmission");
  
  delay (9); 
}
