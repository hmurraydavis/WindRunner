#include <Wire.h>
#include <Servo.h>
#include <SoftwareSerial.h>


//Declare globals:
char current_line[8]; // allocate some space for the string

//declare steering servo:
Servo steerServo;
//Declare sail Servo:
Servo sailServo;

void setup() {
    Serial.begin(9600);
    
    //attach servos:
    steerServo.attach(11);
    sailServo.attach(9);
    steerServo.write(45);
    sailServo.write(90);
    
    //Serial.println("Ready when you are!");
}


//Sensor & actuator read/write functions:
void compassRead(){
	int compassRead=88;
	Serial.println("$c"+String(compassRead));
}

void irRead(){
    int irSensor = 32; //IR sensor is on Arduino Analog pin 0
    int irReading=analogRead(irSensor);
    
    Serial.println("$i"+String(irReading));
}

void gyroscopeRead(){
	//TODO: Add in I2C read gyro code
	int gyroReading=77;
	Serial.println("$g"+String(gyroReading));
}

String windRead(){
	int windDirection=50; //TODO: actually read in wind direction
	Serial.println("$d"+String(windDirection));
}

void steerServoSet(int steerServoHeading){ 
    steerServo.write(steerServoHeading);
}

void sailServoSet(int winch_amount){
    sailServo.write(winch_amount);
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
    String windDirction;
    
    //Serial.println(current_line);
    
    //Serial.println("in loop!");
    switch (current_line[0]){
        case 'c': // compass:
          compassRead();
          break;
        case 'i': // infrared:
          irRead();
          break;
        case 'g': // gyro
          gyroscopeRead();
          break;
        case 'd': // wind direction
          //Serial.println("got a d, reading wind direction");
          windRead();
          break;
        case 's': // steer actuator - expects "s1232" or some other number after 's'
          amount = get_amount(current_line);
          //Serial.println("ss"+String(amount));
          steerServoSet(amount);
          break;
        case 'w': // winch actuator - expects a string with the same format as stear aervo  
          amount = get_amount(current_line);
          //Serial.print("got a w, setting sail winch to ");
          //Serial.println("sw"+String(amount));
          sailServoSet(amount); //sailServo.write(amount);
          break;
        case 'h':
          Serial.println("$hoi");          
    }
}
