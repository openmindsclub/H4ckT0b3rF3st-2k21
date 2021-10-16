int a;
void setup(){
  size(800,800);
  background(255);
}

void draw(){
  
  
  noStroke();
  fill(#E4E82A);
  ellipse(400,420,350,600);
  
  fill(0);
  circle(320,310,80);
  fill(#E4E82A);
  circle(320,330,100);
  
  fill(255);
  ellipse(320,320,60,45);
  fill(0);
  circle(320,320,20);
  fill(255);
  circle(325,325,7);

  fill(0);
  circle(470,310,80);
  fill(#E4E82A);
  circle(470,330,100);
  
  fill(255);
  ellipse(470,330,60,45);
  fill(0);
  circle(470,330,20);
  fill(255);
  circle(475,325,7);
  
  fill(255,0,0);
  ellipse(400,520,70,250);
  fill(#F74A2F);
  ellipse(400,540,150,25);
  circle(400,520,130);
  fill(#E4E82A);
  circle(400,500,150);
  
  
  
  
  
  fill(#B4B71C);
  ellipse(400,420,50,100);
  fill(0);
  circle(390,455,10);
  circle(410,455,10);
  
  fill(0);
  rotate(50);
  ellipse(300,290,290,80);
  
  rotate(-50);
  fill(#F5912C);
  stroke(3);
  fill(#F5912C);
  rect(200,190,400,10);
  arc(400,190,250,360,radians(180),radians(360));
  
  
  fill(#0EA0C6);
  textSize(20);
  text("By Mohamed Yanis Hiou",550,780);
  
  fill(#9C28B4);
  textSize(20);
  text("@hacktoberfest",20,700);
  fill(255,0,0);
  textSize(20);
  text("@OpenMindsClub <3",20,725);
}
