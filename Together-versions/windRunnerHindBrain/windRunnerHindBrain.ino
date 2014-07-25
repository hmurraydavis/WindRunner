#include <Wire.h>
#include <Servo.h>
#include <SoftwareSerial.h>


//Declare globals:
char current_line[8]; // allocate some space for the string

//Steering servo:
Servo steerServo;
//Sail Servo
Servo sailServo;


//Sensor & actuator read/write functions:
String compassRead(){}

String irRead(){
    int irSensor = 0; //IR sensor is on Arduino Analog pin 0
    int irReading=analogRead(irSensor);
    
    return "IR"+String(irReading);
}

String gyroscopeRead(){}

void scanAddresses(){
  /*Scanns all I2C addresses and if the value read 
  in from a register (declared inside the function)
  is not negative one, prints the address and what 
  data was read in.*/
  
  int regista=0x47;
  for(int deviceName=0;deviceName<257;deviceName++){
    Wire.beginTransmission(deviceName);
    Wire.write(regista);
    Wire.endTransmission();
    
    Wire.requestFrom(deviceName, 1);
    int byteG=Wire.read();
    
    if (byteG!=-1) {
      Serial.println("Success with I2C!!!");
      Serial.print("Address was: ");
      Serial.println(deviceName);
      Serial.print("Byte read was: ");
      Serial.println(byteG);
    }
  }
}

void scanRegisters(){
  int deviceName=237;
  for(int regista=0;regista<257;regista++){
    Wire.beginTransmission(deviceName);
    Wire.write(regista);
    Wire.endTransmission();
    
    Wire.requestFrom(deviceName, 1);
    int byteG=Wire.read();
    
    delay(5);
        
    Wire.beginTransmission(deviceName);
    Wire.write(regista);
    Wire.endTransmission();
    
    Wire.requestFrom(deviceName, 1);
    int byteG2=Wire.read();
    
    if (byteG!=byteG2) {
      Serial.println("Success with I2C!!!");
      Serial.print("Address was: ");
      Serial.println(deviceName);
      Serial.print("Byte 1 read was: ");
      Serial.println(byteG);
      Serial.print("Byte 2 read was: ");
      Serial.println(byteG2);
    }
  }
  Serial.println("Done scanning registers.");
}

void scanAllI2C(){
  /*Scans all I2C registers and devices. Returns the 
  device address and register if the data read back 
  changes. */
  
    for(int deviceName=0; deviceName<256;deviceName++){
        for (int regista=0;regista<256;regista++){
           
            Wire.beginTransmission(deviceName);
            Wire.write(regista);
            Wire.endTransmission();
            
            Wire.requestFrom(deviceName, 1);
            int byteG=Wire.read();
            
            delay(5);
            //Serial.println("aft del");
            
            Wire.beginTransmission(deviceName);
            Wire.write(regista);
            Wire.endTransmission();
            
            Wire.requestFrom(deviceName, 1);
            int byteG2=Wire.read();
            
            //Serial.println("b4lp");
            if ( (byteG!=byteG2) ) {
                Serial.println("SUCCESS WITH I2C!!!!!!!!!!!!!");
                Serial.print("Device name was: ");
                Serial.println(deviceName);
                Serial.print("register was: ");
                Serial.println(regista);
                //Serial.println("Hi, Louis!");
                Serial.println(byteG);
    
            
            }
        }
         if (deviceName%9==0){
          Serial.println("Still scanning...");
        }
    }
    Serial.println("Done I2C ing.");
    //Serial.print("Gyroscope reading: ");
    //Serial.println(byteG);
}

String windRead(){}

String steerServoSet(int steerServoHeading){ 
     
    steerServo.write(steerServoHeading);
}

String sailServoSet(int winch_amount){
    sailServo.write(winch_amount);
    Serial.println(winch_amount);
    //sailServo.writeMicroseconds(780);
    delay(10);
    //sailServo.writeMicroseconds(1500);
}

void setup() {
    Serial.begin(9600);
    
    //attach servos:
    steerServo.attach(11);
    sailServo.attach(9);
    steerServo.write(0);
    sailServo.write(0);
    
    Serial.println("Ready when you are!");
}

void read_line(char *line) {
    // read characters from serial into line until a newline character
    char c;
    int index;
    for (index = 0; index < 5; index++) {
        // wait until there is a character
        while (Serial.available() == 0);
        // read a character
        c = Serial.read();
        if (c == '\n') {
            break;
        } else {
            line[index] = c;
        }
    }
    // terminate the string
    line[index] = '\0';
}

int get_amount(char *line) {
    // return the number in a string such as "r1200" as an int
    int amount;
    amount = (int) strtol(line+1, NULL, 10);
    return amount;
}

void loop() {
    read_line(current_line);
    int amount;
    String irReading;
    String gyroReading;
    Serial.println("in loop!");
    switch (current_line[0]){
        case 'c': // compass
          Serial.println("Got a c, reading from compass");
          compassRead();
          break;
        case 'i': // infrared
          Serial.println("Got an i, reading from IR range 1");
          irReading = irRead();
          break;
        case 'g': // gyro
          Serial.println("Got a g, reading from gyroscope");
          gyroReading=gyroscopeRead();
          break;
        case 'd': // wind direction
          Serial.println("got a d, reading wind direction");
          windRead();
          break;
        case 's': // steer actuator - expects "s1232" or some other number after 's'
          amount = get_amount(current_line);
          Serial.print("Got a s, setting stearing servo to ");
          Serial.println(amount);
          steerServoSet(amount);
          break;
        case 'w': // winch actuator - expects a string with the same format of s  
          amount = get_amount(current_line);
          Serial.print("got a w, setting sail winch to ");
          Serial.println(amount);
          sailServo.write(amount);
          break;
        case 'h':
          Serial.print("help mode");
          //scanAddresses();
          scanRegisters();
          
    }
}
