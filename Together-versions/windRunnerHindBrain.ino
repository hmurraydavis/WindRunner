#include <Servo.h>
#include <SoftwareSerial.h>

//Declare globals:
char current_line[8]; // allocate some space for the string

//Steering servo:
Servo steerServo;
int steerPos=45;

//Sail Servo
Servo sailServo;
int sailPos=90;

//Sensor & actuator read/write functions:
String compassRead(){}

String irRead(){
    int irSensor = 0; //IR sensor is on Arduino Analog pin 0
    int irReading=analogRead(irSensor);
    return "IR"+String(irReading);
    
    //attach servos:
    steerServo.attach(10);
    sailServo.attach(11);
}

String gyroscopeRead(){}

String windRead(){}

String steerServoSet(int steerServoHeading){
  Serial.print("setting steering servo to ");
  Serial.println(steerServoHeading);
}

String sailServoSet(int winch_amount){}

void setup() {
  Serial.begin(9600);
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
    switch (current_line[0]){
        case 'c': // compass
          Serial.println("Got a c");
          compassRead();
          break;
        case 'i': // infrared
          irRead();
          break;
        case 'g': // gyro
          gyroscopeRead();
          break;
        case 'd': // direction
          windRead();
          break;
        case 's': // steer actuator - expects "s1232" or some other number after 's'
          amount = get_amount(current_line);
          steerServoSet(amount);
          break;
        case 'w': // winch actuator - expects a string with the same format of s  
          amount = get_amount(current_line);
          sailServoSet(amount);
          break;
    }
}
