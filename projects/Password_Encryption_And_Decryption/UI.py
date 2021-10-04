from tkinter import *
import functions as fun

#Declaration of global variable for the UI
root = None
ModListWindow = None
password = None
EncryptedPassword = None

#Declaration of global variable that will contain the encryption/decripion functions
encrypt = lambda str : fun.DefaultEncryption(str)
decrypt = lambda str : fun.DefaultDecryption(str)

#Function that will allow the user to choose encryption/decripion function he want to use
def FunctionSelection(name):
    e, d = fun.FunctionSelector(name)
    global encrypt
    global decrypt 
    encrypt = lambda str : e(str)
    decrypt = lambda str : d(str)
    ModListWindow.destroy()
    ModListWindow.update()

#Function that opens the list encryption/decripion functions available and that the user can select
def openModList():
    global ModListWindow
    ModListWindow = Toplevel(root)

    ModListWindow.title("New Window")

    ModList = fun.ReturnFunctionsList()
    for mod in ModList:
        button = Button(ModListWindow, text=mod, width = "50", command = lambda: FunctionSelection(mod))
        button.pack()

#The function that encrypt the password and display the result on the UI
def encryption():
    EncryptedPassword.delete(0, END)
    EncryptedPassword.insert(0, encrypt(password.get()))

#The function that decrypt the password and display the result on the UI
def decryption():
    password.delete(0, END)
    password.insert(0, decrypt(EncryptedPassword.get()))

#The function that starts the project by creating the UI
def Start():
    global root
    global password
    global EncryptedPassword 
    
    root = Tk()
    root.geometry("800x500")
    root.title("Password Encryption & Decryption")

    Label(root, text = "Password Encryption & Decryption Project", font = ("Calibri", 20)).place(x=180, y=50)
    Label(root, text = "Encrypted Password", font = ("Calibri", 15)).place(x=310, y=280)
    Label(root, text = "Password", font = ("Calibri", 15)).place(x=350, y=120)

    Button(root, text = "Encrypt", command = encryption).place(x=280, y=220)
    Button(root, text = "Decrypt", command = decryption).place(x=460, y=220)
    Button(root, text = "Encryption/Decryption Mod", command = openModList).place(x=320, y=380)

    password = Entry(root, width = "50")
    password.place(x=250, y=160)
    EncryptedPassword = Entry(root, width = "50")
    EncryptedPassword.place(x=250, y=320)

    root.mainloop()

