int red=6;
int green=5;
int blue=3;
String MyColor;
String msg="What colour do you want? : ";
String msg2="(red, green, blue, aqua,yellow, cyan, magenta, pink?)";
void setup() {
  Serial.begin(9600);
  pinMode(red,OUTPUT);
  pinMode(green,OUTPUT);
  pinMode(blue,OUTPUT);
  digitalWrite(red,HIGH);
  digitalWrite(green,HIGH);
  digitalWrite(blue,HIGH);
}

void loop() {

  Serial.println(msg);
  Serial.println(msg2);
  while(Serial.available()==0){
    
  }
  MyColor = Serial.readString();

 if(MyColor=="red"){
  digitalWrite(red,LOW);
  digitalWrite(green,HIGH);
  digitalWrite(blue,HIGH);
 }
  if(MyColor=="green"){
  digitalWrite(red,HIGH);
  digitalWrite(green,LOW);
  digitalWrite(blue,HIGH);
 }
  if(MyColor=="blue"){
  digitalWrite(red,HIGH);
  digitalWrite(green,HIGH);
  digitalWrite(blue,LOW);
 }
  if(MyColor=="off"){
  digitalWrite(red,HIGH);
  digitalWrite(green,HIGH);
  digitalWrite(blue,HIGH);
 }
  if(MyColor=="aqua"){
  analogWrite(red,255);
  analogWrite(green,0);
  analogWrite(blue,(255-80));
 }
  if(MyColor=="yellow"){
  analogWrite(red,0);
  analogWrite(green,255-100);
  analogWrite(blue,255);
 }
  if(MyColor=="cyan"){
  analogWrite(red,255);
  analogWrite(green,255-255);
  analogWrite(blue,255-255);
 }
  if(MyColor=="magenta"){
  analogWrite(red,255-255);
  analogWrite(green,255-0);
  analogWrite(blue,255-255);
 }
  if(MyColor=="pink"){
  analogWrite(red,255-255);
  analogWrite(green,255-105);
  analogWrite(blue,255-180);
 }
}
