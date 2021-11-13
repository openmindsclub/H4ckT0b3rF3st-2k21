/*************************************************************
**   Controling LED using SERIAL MONITOR
*************************************************/

const int redPin = 8;
const int greenPin = 9;
const int bluePin = 10;

void setup() {

  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  Serial.begin(9600);
  Serial.println("type R - RED ON, G - GREEN ON, B -  BLUE ON, O - ALL is ON, X - ALL is OFF  ");
  Serial.print("choose the letter: ");
}

void loop() {

  if (Serial.available() > 0) {
      char comdata = char(Serial.read());
    if (comdata == 'R') {
      Serial.println("Red LED is ON");
      digitalWrite(redPin, HIGH);
    }
    else if (comdata == 'G' ) {
      Serial.println("Green LED is ON");
      digitalWrite(greenPin, HIGH);
    }
    else if (comdata == 'B') {
      Serial.println("Blue LED is ON");
      digitalWrite(bluePin, HIGH);
    }
    else if (comdata == 'O') {
      Serial.println("all LED is turn ON");
      digitalWrite(redPin, HIGH);
      digitalWrite(greenPin, HIGH);
      digitalWrite(bluePin, HIGH);
    }
    else if (comdata == 'X') {
      Serial.println("all LED is turn OFF");
      digitalWrite(redPin, LOW);
      digitalWrite(greenPin, LOW);
      digitalWrite(bluePin, LOW);
    }
  }
}
