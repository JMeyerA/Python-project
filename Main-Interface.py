# Final Python Project Word editor
# Jack Meyer
# Date: 2024-04-05
# File Reader/editor
'''start of setup code'''
import os #imports os library
import platform #imports platform to check the OS platform for Combatibilty
osCheck = platform.system().lower()
if osCheck != "windows":
    while True:
        print("You are not running a Windows")
        input("Please Run this code on a Windows machine")

validAnswers = {} # dictonary of acepted answers 
validAnswers["no"] = ["no","n"] #adding a list to the dictonary
validAnswers["yes"] = ["yes","y","ye"] #adding a list to the dictonary
validAnswers["all"] = ["no","n","yes","y","ye"]

def userConfermation(info): #confirms that the data they entered is correct feed in users inputed data to function place inside of user input loop
    while validate not in validAnswers["all"]: # begining of loop Info Validate 
        print(info)  
        validate = input("Is the information correct? Yes/No ").strip().lower() #asks user if inputs are correct
        
        if validate in validAnswers["yes"]:  #checks if user input is in list of yesAnswers then breaks Info validate loop
            print ("Input Accepted\n ")
            break
        elif validate in validAnswers["no"]:      #if user input is in list of noAnswers breaks info validate loop and send user to begining of Info Input loop
            print ("Please enter info again\n ")
            break
        else:       # if not a Y or N raises value error
            print("Value Error Enter a yes or no\n ")
            continue
#code to be used with userconfermation function
''' code below to be entered outside of the function
    # if validateInfo() in yesAnswers: #if yes was answered continues Order loop
    #    break
    #else:                   #if no was answered breaks order loop
    #   continue
    #
     #end of Info validate loop
'''
     
''' end of setup code'''

#sign in page code starts here

#class that handles if account exists and creating an account
# also stores new account in accounts.txt
class accountCreate:

    #initialize and define self accounts file
    def __init__(self, accountFile="accounts.txt"):
        self.accountFile = accountFile

    #account creation
    def createAccount(self, username, password):
        #function for account creation
        
        #input: user input for username and password

        #output: writes account info to file for storage and referencing th

        #account already exists by calling account exists function
        if self.accountExists(username):
            return "Account already exists."
        else:
            #creating account and writing to text file
            with open(self.accountFile, "a") as file:
                file.write(f"{username},{password}\n")
            return "Account created successfully."

    #account already exists
    def accountExists(self, username):
        #input username
        #output check if account exists
        #function checks if account already exists
        try:
            #here check if username is already in use
            with open(self.accountFile, "r") as file:
                #check each line for correct username
                for line in file:
                    if line.split(",")[0] == username:
                        return True
            return False
        except FileNotFoundError:
            return False

class LoginManager:
#class for managing login
    
    #initialize class to define account file name
    def __init__(self, accountFile="accounts.txt"):
        self.accountFile = accountFile

    #login 
    def login(self, username, password):
        #input user name and password
        #output user logs in
        #include error checking
        try:
            with open(self.accountFile, "r") as file:
                #loop checking file for input matching stored data and login return invalid if no data matching
                for line in file:
                    user, passw = line.strip().split(",")
                    if user == username and passw == password:
                        return "Login successful."
            return "Invalid username or password."
        except FileNotFoundError:
            return "Account file not found."

# Main program that directs user to create account or login
def main():
    #main function that handles if an account will be made or user logs in

    #define classes for referencing
    account_manager = accountCreate()
    login_manager = LoginManager()

    #prompt user to see if they'd like to log in or create an account
    while True:
        print("Welcome to the python text editor!")
        choice = input("Do you want to login or create an account? (login/create): ").lower()
        #user chooses login then have user login
        if choice == "login":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            print(login_manager.login(username, password))
            #if user chooses create, have them create account
        elif choice == "create":
            username = input("Choose a username: ")
            password = input("Choose a password: ")
            print(account_manager.createAccount(username, password))
            #make sure user inputs valid choice
        else:
            print("Invalid choice. Please type 'login' or 'create'.")
        
        #here program ends if they do nt want to continue
        if input("Do you want to continue? (yes/no): ").lower() == "no":
            break
#call main function so user can login or create account
main()

#end of Sign in page code



#file selector functions starts here


'''for the file selector if the entire thing could be in a big function so it can be called again for the user to select another file :)'''




#end of file selector functions

#Text editor code starts here
#Text editor functions
selectedFile = (r"user-Docs\test.txt") #used for testing before file selector is done
def readFile(): #reads the file out to the user
    file = open(f"{selectedFile}","r") #opens the file
    print(f"\n{file.read()}") #prints out the file into the cmd for the user to read
    file.close()
def editFile():
    print("Opening Notepad")
    os.system(f"notepad {selectedFile}") #opens the selected file in notepad.exe
def openFile(): #used to ask user if they want to edit or read the file
    while True:
        try:
            validResponses = ["1","2","read","edit"]
            print("Would you like \n1) Read \n2) Edit") #asks user if they would like to edit or read
            userResponse = input("Enter your response: ").strip().lower() #gets user to input
            if userResponse in validResponses: #checks if response is valid
                break #if response is valid loops
            else: #if response is not valid
                raise ValueError #if not valid raises valueError            
        except ValueError: #value error tells user to unput a valid input then continues the loop
            print("Please Enter a Valid Response") 
            continue #continues loop
    if userResponse == "1" or userResponse == "read": #if user selected read
        userediting = False
        readFile()
    if userResponse == "2" or userResponse == "edit": #if user selected edit
        userediting = True
        editFile()
    return userediting
def restartCode():
    restart = ""
    while restart not in validAnswers["all"]:
        print("Would You Like to Select a Diffrent File")
        print("\nPlease Enter Valid Response of Yes/No\n ")
        restart = input(": ").strip().lower()
        return restart
'''end of text editor functions'''
   
#code starts here     
while True:
    print(f"You have selected {selectedFile}")
    userediting = openFile() #runs the edit function
    if userediting == True:
        input("Please Hit enter once the file is done being edited") #if the user is in notepad waits for user to hit enter before continuing
    restart = restartCode() #runs restart code function to see if the user wants to pick a new file
        
    if restart in validAnswers["no"]:
        continue
    elif restart in validAnswers["yes"]:
        print("")