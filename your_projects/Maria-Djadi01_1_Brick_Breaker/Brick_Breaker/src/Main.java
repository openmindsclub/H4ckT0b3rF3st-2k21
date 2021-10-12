import java.awt.Color;
import java.awt.Graphics;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class Main {

	public static void main(String[] args) {
		
		JFrame obj = new JFrame();
		GamePlay gplay = new GamePlay();
		obj.setBounds(10, 10, 700, 600);
		obj.setName("Brick breaker");
		obj.setResizable(false);  //We can't resize the window
		obj.setVisible(true);
		obj.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);  //When we press the boutton close of the window 
		obj.add(gplay);
	}

}
