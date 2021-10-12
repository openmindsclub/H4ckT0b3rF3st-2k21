/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package bankmanagement;

import java.io.IOException;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.stage.StageStyle;

/**
 *
 * @author INTEL
 */
public class BankManagement extends Application {
    
    @Override
    public void start(Stage primaryStage) throws IOException {
         Parent root = FXMLLoader.load(getClass().getResource("/tableView/tableViewBank.fxml"));
        Scene scene = new Scene(root);
        //primaryStage.initStyle(StageStyle.UTILITY);
        primaryStage.initStyle(StageStyle.UNDECORATED);
        //primaryStage.setTitle("Hello World!");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        launch(args);
    }
    
}
