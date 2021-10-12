/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package DbConnection;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 *
 * @author INTEL
 */
public class DbConnection {

    public static Connection getConnection() {
        Connection connection;
        // Pour éviter les messages d'erreurs lorsqu'il y a des problemes de connection
        try {
            // Charger le driver mysql
            Class.forName("com.mysql.cj.jdbc.Driver");
            // Créer la connection
            connection = DriverManager.getConnection("jdbc:mysql://localhost/bankdb", "root", "");
            //System.out.println("connected");
            return connection;
        } catch (ClassNotFoundException | SQLException ex) {
            System.out.println("ERROR : " + ex.getMessage());
            return null;
        }
    }
}
