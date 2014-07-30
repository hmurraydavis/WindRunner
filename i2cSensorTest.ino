#include <SoftwareSerial.h>
#include <Wire.h>


void setup() {
  // put your setup code here, to run once:
  Wire.begin();
  Serial.begin(9600);
}

void wakeUpGyroY(){
  //Tell the gyroscope we're talking to it and that 
  //we're going to change the pow_mgmt_2 register to
  //wake it up. 
  int gyroAddress=0x68;
  int powerMgmt2Address=0x6C;
  Wire.beginTransmission(gyroAddress);
  Wire.write(powerMgmt2Address);
  Wire.endTransmission();
  
  //Now time to write the new value to pow_mgmt_2 register
  //to wake the gyro y axis up
  int pwrMgmt2ValueForGyroY=B00000000;
  Wire.beginTransmission(gyroAddress);
  Wire.write(pwrMgmt2ValueForGyroY);
  Wire.endTransmission();
}

void bedTimeGyro(){
  //Tell the gyroscope we're talking to it and that 
  //we're going to change the pow_mgmt_2 register to
  //wake it up. 
  int gyroAddress=0x68;
  int powerMgmt2Address=0x6C;
  Wire.beginTransmission(gyroAddress);
  Wire.write(powerMgmt2Address);
  Wire.endTransmission();
  
  //Now time to write the new value to pow_mgmt_2 register
  //to wake the gyro y axis up
  int pwrMgmt2ValueForGyroY=B00000000;
  Wire.beginTransmission(gyroAddress);
  Wire.write(pwrMgmt2ValueForGyroY);
  Wire.endTransmission();
}

void loop() {
  // put your main code here, to run repeatedly: 
  int gyroAddress=0x68; //from I2C scanner
  int tempL=66;
  Wire.beginTransmission(gyroAddress);
  Wire.write(tempL);
  //char byte1=Wire.read();
  //char byte2=Wire.read();
  //char byte3=Wire.read();
  Wire.endTransmission();
  
  //wakeUpGyroY();//wake up the gyroscope before trying to read from it
  
  Wire.requestFrom(gyroAddress, 1);
  Serial.println(Wire.read());
 
  
  Serial.println("Transmission");
  //bedTimeGyro();
  
  //Serial.println(String(byte1));
  //Serial.println(byte2);
  //Serial.println(byte3);
  
  delay (9); 
}
