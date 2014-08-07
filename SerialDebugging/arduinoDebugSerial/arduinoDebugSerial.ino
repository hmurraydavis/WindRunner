#include <SoftwareSerial.h>

//Declare globals:
char current_line[8]; // allocate some space for the string

void setup(){
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

void windDirection(){
	Serial.print("$d45\n");
}

void compassRead(){
	Serial.println("$c66");
}

void loop() {  
    
    //Serial.println(current_line);
    //Serial.println("$hoi");   
	read_line(current_line);
    int amount;

    switch (current_line[0]){
        case 'c': // compass 
        	compassRead();
        	break;
        case 'd':
        	windDirection();
        	break;
        case '/n':
        	break;
	}
}
