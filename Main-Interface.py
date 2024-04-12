# Final Python Project Word editor
# Jack Meyer Evan Belrose
# Date: 2024-04-05
# File Reader/editor
'''start of setup code'''
import os #imports os library
import platform #imports platform to check the OS platform for Combatibilty
osCheck = platform.system().lower()
if osCheck != "windows": #if os is not windows
    while True: #run loop to prevent crash on non windows system
        print("You are not running a Winodws OS")
        input("Please Run this code on a Windows machine")

validAnswers = {} # dictonary of acepted answers 
validAnswers["no"] = ["no","n"] #adding a list to the dictonary
validAnswers["yes"] = ["yes","y","ye"] #adding a list to the dictonary
validAnswers["all"] = ["no","n","yes","y","ye"]
username = ""
     
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
        except ValueError:
            return "Invalid Credentials Entered"
# Main program that directs user to create account or login
def main():
    #main function that handles if an account will be made or user logs in

    #define classes for referencing
    account_manager = accountCreate()
    login_manager = LoginManager()

    #prompt user to see if they'd like to log in or create an account
    while True:
        loginDone = ""
        print("Welcome to the python text editor!")
        choice = input("Do you want to login or create an account? (login/create): ").lower().strip()
        #user chooses login then have user login
        if choice == "login":
            while True:
                try:
                    username = input("Enter your username: ").strip()
                    password = input("Enter your password: ").strip()
                    print(f"is {username} {password} Correct?")
                    if input("Yes/No: ") in validAnswers["yes"]:
                        print("testing credentials")
                    else:
                        continue
                except:
                    print("Error Please enter info again")
                    continue
                accountCheck = (login_manager.login(username, password))
                print(accountCheck)
                if accountCheck == "Invalid Credentials Entered":
                    print("please Try again")
                    continue
                else:
                    break
            #if user chooses create, have them create account
        elif choice == "create":
            username = input("Choose a username: ").strip()
            password = input("Choose a password: ").strip()
            os.mkdir(f"user-Docs\\{username}")
            print(account_manager.createAccount(username, password))
            #make sure user inputs valid choice
        else:
            print("Invalid choice. Please type 'login' or 'create'.")
            continue
        #here program ends if they do not want to continue
        while loginDone not in validAnswers["all"]:
            loginDone = input("Do you want to continue? (yes/no): ").lower()
        break    
    return loginDone,username
#call main function so user can login or create account


#end of Sign in page code



#file selector functions starts here

def listTextFiles(directory):
    
    # List all text files in a given directory.
    textFiles = []
    for filename in os.listdir(directory):
        filePath = os.path.join(directory, filename)
        if os.path.isfile(filePath):
            textFiles.append(filePath)
            makeFile = ""
            while makeFile not in validAnswers["all"]: #asks user if they want to make a new file
                makeFile = input("Would you like to create a file yes/no: ").lower().strip()
            if makeFile in validAnswers["no"]:
                while True:
                    print(textFiles)
                    selectedFile = input("Please Enter the name of the file you want with out .txt: ") #asks user to name a to open file
                    selectedFile = (f"user-Docs\\{username}\\{selectedFile}.txt")
                    print(f"you have selected {selectedFile}")
                    if selectedFile in textFiles:
                        break
                    else:
                        print("Please enter a valid file name\n")
                        continue
                break
            if makeFile in validAnswers["yes"]: #makes new file from user input
                filename = input("enter the your file name: ")
                filename = open(f"user-Docs\\{username}\\{filename}.txt","x")
                print(f"{filename} Succesfully Created")
                break
    return textFiles

def selectOperationalFile(directory):
    
    # Select a text file from a given directory.
    textFiles = listTextFiles(directory)
    if textFiles:
        return textFiles[0]  # Return the first text file found
    else:
        return None




#end of file selector functions

                                                                                                    #code starts HERE
loginDone,username = main()
if loginDone in validAnswers["yes"]:
    print("Continuing to file selector\n")
    selectedFile = listTextFiles(f"user-Docs\\{username}")
elif loginDone in validAnswers["no"]:
    print("Quitting Program............")
    os._exit(0)

                                                                                                    #Text editor code starts here
#Text editor functions
def readFile(): #reads the file out to the user
    
    #selected file goes into function
    #opens the file
    #prints contents of file to user for viewing4
    
    file = open(f"{selectedFile}","r") #opens the file
    print(f"\n{file.read()}") #prints out the file into the cmd for the user to read
    file.close()
def editFile():
    #takes selected file 
    #opens file in notepad
    print("Opening Notepad")
    os.system(f"notepad {selectedFile}") #opens the selected file in notepad.exe
def openFile(): #used to ask user if they want to edit or read the file
    #asks the user what they would like to do with the selected file
    #returns the users choice to the main code
    while True:
        try:
            validResponses = ["1","2","read","edit"]
            print("Would you like to \n1) Read \n2) Edit") #asks user if they would like to edit or read
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
    #asks the user if they would like to restart their code
    #checks if user input is a valid answer and if it is breaks loop
    #if users says yes then code returns true restart value
    restart = ""
    while restart not in validAnswers["all"]: #will loop until a valid answer is inputed 
        print("Would You Like to Select a Diffrent File")
        print("\nPlease Enter Valid Response of Yes/No\n ")
        restart = input(": ").strip().lower()
    return restart #returns value to main code
'''end of text editor functions'''
   
#code starts here     
while True:
    print(f"You have selected {selectedFile}") #tells user what file is selected
    userediting = openFile() #runs the edit function
    if userediting == True: #if the user selected editing 
        input("Please Hit enter once the file is done being edited") #if the user is in notepad waits for user to hit enter before continuing
    restart = restartCode() #runs restart code function to see if the user wants to pick a new file
        
    if restart in validAnswers["no"]:
        if input("Would you like to quit the program? ") in validAnswers["yes"]:
            os._exit(0)
        continue
    elif restart in validAnswers["yes"]:
        selectedFile = listTextFiles(f"user-Docs\\{username}")