<h1 align="center">Password_Encryption_And_Decryption</h1>

<p align="center">
  <a href="#project-description">Project description</a>   |   
  <a href="#your-task">Your Task</a>   |  
  <a href="#requirements">Requirements</a>   |  
  <a href="#checkered_flag-starting">Starting</a>
</p>

<br>

## Project description

Privacy is an important topic since the internet exist, and one of the simplest ways to protect it and lower the risks of people to access it is to use a different password in each account. But it is often hard to not get lost between all those passwords and remember there all, and this is when Passwords Managers come to save us !!! And those Passwords Managers often use Encryption and Decryption methods to make their software more secure for the user data. In this project the goal is to propose multiple Encryption and Decryption functions and test them.

## Your Task

In this project, we already created a simple Encryption and Decryption function using Caesar cipher with a right shift of the length of the word encrypted/decrypted. Your task is to propose and code other functions. The function has to take only one string argument and has to return a string, we count on you to be creative.

## Requirements

Before starting 🏁, you need to have [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) installed.

## Starting

```bash
# Start a Git repository
git init

# Track repository, do not enter subdirectory
git remote add -f origin https://github.com/openmindsclub/H4ckT0b3rF3st-2k21/

# Enable the tree check feature
git config core.sparseCheckout true

# Create a file in the path: .git/info/sparse-checkout
# That is inside the hidden .git directory that was created
# by running the command: git init
# And inside it enter the name of the sub directory you only want to clone
echo 'projects/password_encryption_and_decryption' >> .git/info/sparse-checkout

## Download with pull, not clone
git pull origin master

#go to the functions.py file and create your function under the "Create your function here" comment

```

```Python
#After finishing creating your function go to the FunctionSelector function and copy paste the elif comment
# uncomment it and give it a key name and put your functions in the appropriate variables for exemple :

elif choice == "MyFunctions": #key name
    e = lambda str : MyEncryptionFunction(str)
    d = lambda str : MyDecryptionFunction(str)

#All what is left to do is to add your key name on the list in the ReturnFunctionsList function like this

def ReturnFunctionsList():
    return ["Default", "MyFunctions"] #key name added

#You can then test your function by running the Main.py file, once the UI shows up
# click on the Encryption/Decryption Mod button to select your key name so he program will use your function

```

<p align="center">
<a href="#top">Back to top</a>
</p>
