/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tableView;

import static DbConnection.DbConnection.getConnection;
import com.jfoenix.controls.JFXButton;
import java.net.URL;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ResourceBundle;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.collections.transformation.FilteredList;
import javafx.collections.transformation.SortedList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.geometry.Pos;
import javafx.scene.Node;
import javafx.scene.control.Alert;
import javafx.scene.control.Label;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.stage.Stage;
import models.Bank;
import org.controlsfx.control.Notifications;

/**
 * FXML Controller class
 *
 * @author INTEL
 */
public class TableViewBankController implements Initializable {

    @FXML
    private JFXButton btn_insert;
    @FXML
    private JFXButton btn_update;
    @FXML
    private JFXButton btn_delete;
    @FXML
    private TextField tf_filter;
    @FXML
    private TableView<Bank> bankTable;
    @FXML
    private TableColumn<Bank, Integer> bankNumCol;
    @FXML
    private TableColumn<Bank, String> nameCol;
    @FXML
    private TableColumn<Bank, Integer> DAAccountNumCol;
    @FXML
    private TableColumn<Bank, Integer> EuroAccountNumCol;
    @FXML
    private TextField tf_nbanque;
    @FXML
    private TextField tf_nomBanque;
    @FXML
    private TextField tf_ncompteEuro;
    @FXML
    private TextField tf_ncompteDA;
    @FXML
    private Label total;

    /**
     * Initializes the controller class.
     */
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        showBanks();
        search();
    }

    @FXML
    private void handleButtonAction(ActionEvent event) {
        if (event.getSource() == btn_insert) {
            if ((tf_nbanque.getText()).isEmpty() || (tf_nomBanque.getText()).isEmpty() || (tf_ncompteDA.getText()).isEmpty() || (tf_ncompteEuro.getText()).isEmpty()) {
                Alert alert = new Alert(Alert.AlertType.ERROR);
                alert.setHeaderText(null);
                alert.setContentText("Please fill all data");
                alert.showAndWait();
            } else {
                insertBank();
                Image image = new Image("/images/save.png");
                Notifications notificationBuilder = Notifications.create()
                        .title("Bank's Information")
                        .text("Data Saved ...")
                        .graphic(new ImageView(image))
                        .position(Pos.BASELINE_RIGHT)
                        .darkStyle();

                notificationBuilder.show();

            }
        } else if (event.getSource() == btn_update) {
            if ((tf_nbanque.getText()).isEmpty() || (tf_nomBanque.getText()).isEmpty() || (tf_ncompteDA.getText()).isEmpty() || (tf_ncompteEuro.getText()).isEmpty()) {
                Alert alert = new Alert(Alert.AlertType.ERROR);
                alert.setHeaderText(null);
                alert.setContentText("Please fill all data");
                alert.showAndWait();
            } else {
                updateBank();
                 Image image = new Image("/images/update.png");
                Notifications notificationBuilder = Notifications.create()
                        .title("Bank's Information")
                        .text("Data Updated ...")
                        .graphic(new ImageView(image))
                        .position(Pos.BASELINE_RIGHT)
                        .darkStyle();

                notificationBuilder.show();
            }
        } else if (event.getSource() == btn_delete) {
            deleteBank();
            
             Image image = new Image("/images/delete.png");
                Notifications notificationBuilder = Notifications.create()
                        .title("Bank's Information")
                        .text("Data Deleted ...")
                        .graphic(new ImageView(image))
                        .position(Pos.BASELINE_RIGHT)
                        .darkStyle();

                notificationBuilder.show();
        }
    }

    public ObservableList<Bank> getBanksList() {
        ObservableList<Bank> BankList = FXCollections.observableArrayList();
        Connection con = getConnection();
        String query = "SELECT * FROM bank";
        Statement st;
        ResultSet rs;
        try {
            st = con.createStatement();
            rs = st.executeQuery(query);
            Bank bank;
            while (rs.next()) {
                bank = new Bank(rs.getInt("Bank_Num"), rs.getString("Name"), rs.getInt("DA_Account_Num"), rs.getInt("Euro_Account_Num"));
                BankList.add(bank);
            }
        } catch (SQLException ex) {
            System.out.println("ERROR : " + ex.getMessage());
        }
        return BankList;
    }

    public void showBanks() {
        ObservableList<Bank> list = getBanksList();
        bankNumCol.setCellValueFactory(new PropertyValueFactory<Bank, Integer>("Bank_Num"));
        nameCol.setCellValueFactory(new PropertyValueFactory<Bank, String>("Name"));
        DAAccountNumCol.setCellValueFactory(new PropertyValueFactory<Bank, Integer>("DA_Account_Num"));
        EuroAccountNumCol.setCellValueFactory(new PropertyValueFactory<Bank, Integer>("Euro_Account_Num"));
        bankTable.setItems(list);
    }
    //Rq : gère les exeption sql

    private void insertBank() {

        String query = "INSERT INTO bank VALUES (" + tf_nbanque.getText() + ",'" + tf_nomBanque.getText() + "'," + tf_ncompteDA.getText() + "," + tf_ncompteEuro.getText() + ")";
        executeQuery(query);
        showBanks();
        search();
    }

    private void updateBank() {
        String query = "UPDATE bank SET DA_Account_Num = " + tf_ncompteDA.getText() + ", Name = '" + tf_nomBanque.getText() + "', Euro_Account_Num  = " + tf_ncompteEuro.getText() + " WHERE Bank_Num = " + tf_nbanque.getText();
        executeQuery(query);
        showBanks();
        search();
    }

    private void deleteBank() {
        String query = "DELETE FROM bank WHERE Bank_Num = " + tf_nbanque.getText();
        executeQuery(query);
        showBanks();
        search();
    }

    private void total() {
        String query = "SELECT COUNT(Bank_Num) FROM bank";
        System.err.println(query);
        executeQuery(query);
        total.setText("" + query);
    }

    private void executeQuery(String query) {
        Connection con = getConnection();
        Statement st;

        try {
            st = con.createStatement();
            st.executeUpdate(query);
        } catch (SQLException ex) {
            System.out.println("ERROR : " + ex.getMessage());
            Alert alert = new Alert(Alert.AlertType.WARNING);
            alert.setHeaderText(null);
            alert.setContentText("Data entered errone. Try again ?");
            alert.showAndWait();
        }
    }

    public void search() {
        ObservableList<Bank> dataList = getBanksList();
        bankNumCol.setCellValueFactory(new PropertyValueFactory<Bank, Integer>("Bank_Num"));
        nameCol.setCellValueFactory(new PropertyValueFactory<Bank, String>("Name"));
        DAAccountNumCol.setCellValueFactory(new PropertyValueFactory<Bank, Integer>("DA_Account_Num"));
        EuroAccountNumCol.setCellValueFactory(new PropertyValueFactory<Bank, Integer>("Euro_Account_Num"));
        bankTable.setItems(dataList);
        FilteredList<Bank> filteredData = new FilteredList<>(dataList, b -> true);
        tf_filter.textProperty().addListener((observable, oldValue, newValue) -> {
            filteredData.setPredicate(bank -> {
                if (newValue == null || newValue.isEmpty()) {
                    return true;
                }
                String lowerCaseFilter = newValue.toLowerCase();

                if (String.valueOf(bank.getBank_Num()).toLowerCase().indexOf(lowerCaseFilter) != -1) {
                    return true;
                } else if (String.valueOf(bank.getName()).toLowerCase().indexOf(lowerCaseFilter) != -1) {
                    return true;
                } else if (String.valueOf(bank.getDA_Account_Num()).toLowerCase().indexOf(lowerCaseFilter) != -1) {
                    return true;
                } else if (String.valueOf(bank.getEuro_Account_Num()).toLowerCase().indexOf(lowerCaseFilter) != -1) {
                    return true;
                } else {
                    return false;
                }
            });

        });
        SortedList<Bank> sortedData = new SortedList<>(filteredData);
        sortedData.comparatorProperty().bind(bankTable.comparatorProperty());
        bankTable.setItems(sortedData);
    }

    @FXML
    private void handleMouseAction(MouseEvent event) {
        Bank bank = bankTable.getSelectionModel().getSelectedItem();
        /**
         * System.out.println("N°banque " + banque.getN_Banque());
         * System.out.println("N°compteDA " + banque.getN_CompteDA());
         * System.out.println("N°compteEuro " + banque.getN_CompteEuro());
         *
         */
        tf_nbanque.setText("" + bank.getBank_Num());
        tf_nomBanque.setText(bank.getName());
        tf_ncompteDA.setText("" + bank.getDA_Account_Num());
        tf_ncompteEuro.setText("" + bank.getEuro_Account_Num());

    }

    /*@FXML
    private void getAddView(MouseEvent event) {
        try {
            Parent parent = FXMLLoader.load(getClass().getResource("/tableView/bankDetail.fxml"));
            Scene scene = new Scene(parent);
            Stage stage = new Stage();
            stage.setScene(scene);
            stage.initStyle(StageStyle.UTILITY);
            stage.show();
        } catch (IOException ex) {
            Logger.getLogger(TableViewBankController.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }*/
    @FXML
    private void close(MouseEvent event) {
        Stage stage = (Stage) ((Node) event.getSource()).getScene().getWindow();
        stage.close();
    }

}
