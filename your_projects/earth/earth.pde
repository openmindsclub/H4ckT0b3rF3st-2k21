import ddf.minim.*;

Minim minim;
AudioPlayer a,b,c,carsound;

PImage ert,car;
float rt;

void setup(){
  
size(1000,900);
background(0);
  
  ert=loadImage("earth.png");
  car=loadImage("car.png");

  
}
void draw(){

  imageMode(CENTER); 

  noStroke();
  fill(0,5);
  rect(0,0, width, height);
  
  fill(250);
  ellipse(random(width), random(height), 5,5);
  pushMatrix();
 translate(width/2,1200);
 rotate(rt);
 rt+=.01;
 image(ert,0,0);
 popMatrix();
 image(car,width/2,462);
  }
