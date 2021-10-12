float ballX=width/2; 
float ballY=height/2;
int speedX=3;
int speedY=3;
int rectX=20;
int rectY=200;
void setup(){
  size(700,700);
  

  speedX =2;
  speedY =3;

}

void draw(){
  background(0);
  
  fill(#FF0000);
  circle(ballX, ballY,50);
  
  fill(255);
  rect(rectX,rectY,30,100);
  
  if (ballX > width - 25){
    speedX = -speedX;
  }
  
  
  if(ballY > height -25){
    speedY = -speedY;
  }
  else if(ballY < 25){
    speedY = -speedY;
  }
  
  if(keyPressed && keyCode == UP){
    rectY -= 4;
  }
  if(keyPressed && keyCode ==DOWN){
    rectY += 4;
  }
  
  if(ballX - 25 < rectX + 15 && ballY - 25 < rectY + 100 && ballY + 25 > rectY - 100){
    speedX = -speedX;
  }
  
  if(ballX <=10){
    ballX =width/2;
    ballY = height/2;
  }
  

ballX = ballX +speedX;
ballY = ballY +speedY;
  
}
