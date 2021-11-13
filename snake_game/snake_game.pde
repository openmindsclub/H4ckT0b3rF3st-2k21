ArrayList<Integer> x = new ArrayList<Integer>(),  y = new ArrayList<Integer>();
int w = 30, h = 30, bs = 20, dir = 2, foodx = 10, foody = 10, score = 0;
int[] dx = {0,0,1,-1}, dy = {1,-1,0,0};
boolean gameOver = false;

void setup()
{  
    size(600, 600);
    x.add(5);
    y.add(5);
}


void draw()
{
    if(!gameOver)
    {
        background(255);
        fill(0);
        textAlign(LEFT);
        text(score, 70, 20);
        rect(foodx*bs, foody*bs, bs, bs);
        for(int i = 0; i<x.size(); i++){
            noStroke();
            fill(0,255,0);
            rect(x.get(i)*bs, y.get(i)*bs, bs, bs);
        }
        
        if(frameCount%5 == 0)
        {
            x.add(0,x.get(0)+dx[dir]);
            y.add(0,y.get(0)+dy[dir]);
            if(foodx == x.get(0) && foody == y.get(0)){ 
                score += 5;
                foodx = (int)random(0,w);
                foody = (int)random(0,h);
            }
            else{
                x.remove(x.size()-1);
                y.remove(y.size()-1);
            }
        }
        if(x.get(0) < 0 || x.get(0) >= w || y.get(0) <0 || y.get(0) >=h)
            {
                delay(2000);
                gameOver = true;
                score = 0;
            }
        for(int i = 1; i < x.size()-1; i++)
        {
          if(x.get(i) == x.get(0) && y.get(i) == y.get(0))
          {
              delay(2000);
              gameOver = true;
              score = 0;
          }
        }
    }
    else{
          background(0);
          textSize(20);
          textAlign(CENTER);
          text("GAME OVER! \nPRESS SPACE TO PLAY AGAIN OR ESC TO EXIT)", width/2, height/3);
          if(keyPressed && key == ' ')
          {
              x.clear();
              y.clear();
              x.add(5);
              y.add(5);
              gameOver = false;
          }
     }
}


void keyPressed()
{
    int newDir;
    if(key == CODED)
    {
        switch(keyCode){
            case DOWN: newDir = 0; break;
            case UP: newDir = 1; break;
            case RIGHT: newDir = 2; break;
            case LEFT: newDir = 3; break;
            default: newDir = -1; break;
        }//end switch
    }//end if
    else
    {
        switch(key){
            case 's': newDir = 0; break;
            case 'w': newDir = 1; break;
            case 'd': newDir = 2; break;
            case 'a': newDir = 3; break;
            default: newDir = -1; break;
        }//end switch
    }//end else
    
    switch(newDir){
        case 0: {
                    if(dy[dir] == -1)
                    {
                        break;
                    }else {
                              dir = newDir;
                              break;
                    }//end if/else
        }//end case0
        case 1: {
                    if(dy[dir] == 1)
                    {
                      break;
                    }else {
                              dir = newDir;
                              break;
                    }//end if/else
        }//end case1
        case 2: {
                    if(dx[dir] == -1)
                    {
                      break;
                    }else {
                              dir = newDir;
                              break;
                    }//end if/else
        }//end case2
        case 3: {
                    if(dx[dir] == 1)
                    {
                      break;
                    }else {
                              dir = newDir;
                              break;
                    }//end if/else
        }//end case3
    }//end switch
    
}
