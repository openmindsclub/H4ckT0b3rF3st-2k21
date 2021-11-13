#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <SoftwareSerial.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);



void setup() {
  Serial.begin(9600);
  
  pinMode(8, OUTPUT);
  digitalWrite(8, HIGH);

  lcd.init();
  lcd.backlight();
  Wire.begin();

  lcd.setCursor(0, 0);
  lcd.print("ELECTRO Scientific Club");
  delay(1500);
  for (int positionCounter = 0; positionCounter < 23; positionCounter++) {
    lcd.scrollDisplayLeft();
    delay(500);
  }
  lcd.clear();
  lcd.setCursor(1, 0);
  lcd.print("Electro  Club");
  for (int i = 0; i < 3; i++) {
    lcd.noDisplay();
    delay(700);
    lcd.display();
    delay(700);
  }

  lcd.setCursor(2, 1);
  lcd.print("@electro.sc");
  delay(2000);

}

void loop(){
  if (Serial.available() > 0) {
    int data = Serial.read();
    if (data == '1') {
      digitalWrite(8, LOW);

      lcd.clear();
      lcd.setCursor(3, 0);
      lcd.print("LED IS ON!");
      lcd.setCursor(2,1);
      lcd.print("ELECTRO  SC");
      delay(1500);
      lcd.clear();
      lcd.setCursor(2, 0);
      lcd.print("LED Control");
      lcd.setCursor(2, 1);
      lcd.print("ELECTRO  SC");



    } else if (data == '0') {
      digitalWrite(8, HIGH);


      lcd.clear();
      lcd.setCursor(3, 0);
      lcd.print("LED IS OFF!");
      lcd.setCursor(2,1);
      lcd.print("ELECTRO  SC");
      delay(1500);
      lcd.clear();
      lcd.setCursor(2, 0);
      lcd.print("LED Control");
      lcd.setCursor(2, 1);
      lcd.print("ELECTRO  SC");

    }
    
  }
}
