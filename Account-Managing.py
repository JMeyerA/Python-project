#Evan Belrose 7627953 final assignment
#login portion of assignment
#4/10/2024
#this file logins in or creates an account and also checks to see if account is already existing


#class that handles if account exists and creating an account
# also stores new account in accounts.txt
class accountCreate:
    #name of text file stored as variable in the class
    


    #initialize and define self accounts file
    def __init__(self, accountFile='accounts.txt'):
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
            with open(self.accountFile, 'a') as file:
                file.write(f"{username},{password}\n")
            return "Account created successfully."

    #account already exists
    def accountExists(self, username):
        #input username
        #output check if account exists
        #function checks if account already exists
        try:
            #here check if username is already in use
            with open(self.accountFile, 'r') as file:
                #check each line for correct username
                for line in file:
                    if line.split(',')[0] == username:
                        return True
            return False
        except FileNotFoundError:
            return False

class LoginManager:
#class for managing login
    
    #initialize class to define account file name
    def __init__(self, accountFile='accounts.txt'):
        self.accountFile = accountFile

    #login 
    def login(self, username, password):
        #input user name and password
        #output user logs in
        #include error checking
        try:
            with open(self.accountFile, 'r') as file:
                #loop checking file for input matching stored data and login return invalid if no data matching
                for line in file:
                    user, passw = line.strip().split(',')
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
        choice = input("Do you want to login or create an account? (login/create): ").lower()
        #user chooses login then have user login
        if choice == 'login':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            print(login_manager.login(username, password))
            #if user chooses create, have them create account
        elif choice == 'create':
            username = input("Choose a username: ")
            password = input("Choose a password: ")
            print(account_manager.createAccount(username, password))
            #make sure user inputs valid choice
        else:
            print("Invalid choice. Please type 'login' or 'create'.")
        
        #here program ends if they do nt want to continue
        if input("Do you want to continue? (yes/no): ").lower() == 'no':
            break
#call main function so user can login or create account
main()