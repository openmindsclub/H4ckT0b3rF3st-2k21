package models;

/**
 *
 * @author Nour Elhouda YOUCEFI
 */
public class Bank {
     public int Bank_Num;
     public String Name;
     public int  DA_Account_Num;
     public int Euro_Account_Num;
     
    public Bank(int Bank_Num, String Name, int DA_Account_Num, int Euro_Account_Num) {
        this.Bank_Num = Bank_Num;
        this.Name = Name;
        this.DA_Account_Num = DA_Account_Num;
        this.Euro_Account_Num = Euro_Account_Num;
    }

    public int getBank_Num() {
        return Bank_Num;
    }

    public void setBank_Num(int Bank_Num) {
        this.Bank_Num = Bank_Num;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public int getDA_Account_Num() {
        return DA_Account_Num;
    }

    public void setDA_Account_Num(int DA_Account_Num) {
        this.DA_Account_Num = DA_Account_Num;
    }

    public int getEuro_Account_Num() {
        return Euro_Account_Num;
    }

    public void setEuro_Account_Num(int Euro_Account_Num) {
        this.Euro_Account_Num = Euro_Account_Num;
    }
     
}
