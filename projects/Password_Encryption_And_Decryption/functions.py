#The Default Encryption function used in the project 
#Base on Caesar cipher with a right shift of the length of the word encrypted 
def DefaultEncryption(str):
    result = ""
    s = len(str)
    for i in range(len(str)):
        char = str[i]
        
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        elif (char.islower()):
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += chr((ord(char) + s))
        
    return result

#The Default Decryption function used in the project 
def DefaultDecryption(str):
    result = ""
    s = len(str)
    for i in range(len(str)):
        c = (ord(str[i]) - s)

        if (str[i].isupper()):
            if c<65 :
                result += chr(c+26)
            else:
                result += chr(c)
        elif (str[i].islower()):
            if c<97 :
                result += chr(c+26)
            else:
                result += chr(c)
        else:
            result += chr(c)
        
    return result

#Create your function here

"""
    Your Code
                """

#A function that will allow the user choosing the encryption/decripion function he want to use
#Once you finish your method give it a key name and put all the neccessary info in an elif condition
def FunctionSelector(choice):
    e = None
    d = None

    if choice == "Default":
        e = lambda str : DefaultEncryption(str)
        d = lambda str : DefaultDecryption(str)
    # elif choice == "":
    #     e = lambda str : 
    #     d = lambda str : 

    return e, d

#Put the key name of your encryption/decripion function in the list so it will appear on the UI
def ReturnFunctionsList():
    return ["Default"]

