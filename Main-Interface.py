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