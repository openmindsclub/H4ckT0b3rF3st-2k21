

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;


import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.Timer;
public class GamePlay extends JPanel implements KeyListener,ActionListener{
	
	private boolean play = false; 
	private int score = 0;  //initial score
	private int bricksNumber = 21;  //total of bricks
	private Timer timer;
	private int delay = 8;
	
	private int playerX = 310;
	
	private int ballposX = 120;
	private int ballposY = 350;
	private int ballXdirection = -1;
	private int ballYdirection = -2;
	
	private MapGenerator map;
	
	public GamePlay() {
		map = new MapGenerator(3,7);
		addKeyListener(this);
		setFocusable(true);
		setFocusTraversalKeysEnabled(false);
		timer = new Timer(delay,this);
		timer.start();
	}
	
	public void paint(Graphics g) {
		g.setColor(Color.white);
		g.fillRect(1, 1, 692, 592);  //BackGround
		
		map.draw((Graphics2D)g);
		
		g.setColor(Color.yellow);  // Borders
		g.fillRect(0, 0, 3, 592); //Left border
	    g.fillRect(0, 0, 692, 3); //Top border
		g.fillRect(680, 0, 3, 592); //Right border
		
		g.setColor(Color.blue);
		g.fillRect(playerX, 550, 100, 8); //Pedal position
		
		g.setColor(Color.green);
		g.fillOval(ballposX, ballposY, 20, 20); //Ball position
		
		g.dispose();
	}
	@Override
	public void keyTyped(KeyEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void keyPressed(KeyEvent e) {
		if(e.getKeyCode() == KeyEvent.VK_RIGHT) {
			if(playerX >= 600) {
				playerX = 600;
			}
			else moveRight();
		}
		if(e.getKeyCode() == KeyEvent.VK_LEFT) {
			if(playerX < 10) {
				playerX = 10;
			}
			else moveLeft();
		}
	}
	
	public void moveRight() {
		play = true;
		playerX += 20;
	}
	public void moveLeft() {
		play = true;
		playerX -= 20;
	}
	@Override
	public void keyReleased(KeyEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		timer.start();
		if(play) {
			if(new Rectangle(ballposX, ballposY, 20, 20).intersects(new Rectangle(playerX, 550, 100, 8))) {
				ballYdirection = -ballYdirection;
			}
			//The movement of the ball
			ballposX += ballXdirection;
			ballposY += ballYdirection;
			
			if(ballposX < 0) ballXdirection = -ballXdirection; //When the ball hits the right wall
			if(ballposY < 0) ballYdirection = -ballYdirection; //When the ball hits the top
			
			if(ballposX > 670) ballXdirection = -ballXdirection; //When the ball hits the left wall
		}
		repaint();
	}
}

