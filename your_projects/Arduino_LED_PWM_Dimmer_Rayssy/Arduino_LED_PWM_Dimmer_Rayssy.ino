int potPin=A0;
int redPin=6;
int potVal;
int LedVal;
void setup() {
  // put your setup code here, to run once:
  pinMode(potPin,INPUT);
  pinMode(redPin,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  potVal = analogRead(potPin);
  LedVal= potVal * (255./1023.);
  analogWrite(redPin,LedVal);
}
