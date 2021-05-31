import getpass
import random
import string
import pyperclip


class User:
    """class"""

    userList = []


def __init__(self, username, password):

    " magic  constructor method "

    self.username = username
    self.password = password

    self.isLoggedin = False


def CreateUser(username, password):
    """method"""

    newUser = User(username, password)
    return newUser


def login(self):
    print("logged in successfully")


def saveUser(self, username, password):
    "method"

    User.userList.append(self)


@classmethod
def displayUser(cls):
    return cls.userList


def deleteUser(self):
    User.userList.remove(self)


class Credentials:

    credentials_list = []

    @classmethod
    def verify_user(cls, username, password):

        aUser = ""
        for user in User.userList:
            if (user.username == username and user.password == password):
                aUser == user.username
                return aUser

    def __init__(self, account, username, password):
        """
            cedentials to be stored
        """
        self.account = account
        self.username = username  #sjsjsj
        self.password = password

    def save_details(self):

        Credentials.credentials_list.append(self)

    def delete_credentials(self):

        Credentials.credentials_list.remove(self)

    @classmethod
    def createCredential(account,username, password):
        "creates new credential"
        newCredential = Credentials(username, password)
        return newCredential

    def save_credentials(account,username, password):
        "save credentials in the list"
        return Credentials.display_credentials()

    def find_credential(cls, account):
        "method that takes class name and returns the account name credential"
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
        print("There is no such account dear")

    @classmethod
    def copy_password(cls, account):
        found_credentials = Credentials.find_credentials(account)
        pyperclip.copy(found_credentials.password)

    @classmethod
    def credentialExist(cls, account):

        "checks if the credential exists from the list"

        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        "returns all credentials in the list"
        return cls.credentials_list

    def generatePassword(stringLength=8):
        "generates a random password "

        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#"
        return ''.join(random.choice(password) for i in range(stringLength))

    def copypassword(parameter_list):
        """
             method that allows copying of password to keyboard
             """
        pass


def main():

    # isTrue = True

    print(
        "Welcome to password Locker.Here you manage your passwords and even generate new passwords."
    )
    while isTrue == True:
        print(
                "Hi, your account has logged in successfully!"
                 )

        print(
            "Please enter one to proceed:\n\n 1. ca for Create new Account\n 2. lg for login\n 3. ex for Exit"
        )
        shortCode = input("").lower().strip()
        if shortCode == "ca":
            print("Sign Up Account")
            print("*" * 20)
            print("Username:")
            username = input()
            while True:
                print(
                    "1. Type TP s to type your own password:\n  or \n 2. GP for generating random password"
                )
                passwordOption = input().lower().strip()

                if passwordOption == 'tp':
                    print("Enter Your Password")
                    password = input("password\n")

                    break
                elif passwordOption == 'gp':
                     password = Credentials.generatePassword()
                     break
                else:
                    print("invalid pasword")

                User.CreateUser(username, password)
                User.saveUser(username, password)
                print("\n")

            print(
                f"Hi {username}, your account has been created successfully! \n Your password is: {password}"
            )

        elif shortCode == 'lg':
            print("*" * 50)
            print("Enter your username and password")
            print("*" * 50)

            print("Username")
            username = input()
            print("password")
            password = input()

            for user in User.userList:
                if username == user.username:
                    if user.password == password:
                        print(user.login())
                        
                else:
                        User.CreateUser(username, password)
                        User.saveUser(username, password)
                        print("\n")

                        print(
                                f"Hi {username}, your account has logged in successfully! \n Your password is: {password}"
                                )
                # else:
                #     print("username invalid")
                    # break
                

        # elif shortCode == 'ex':

        #     print("See you later!!")
        #     break
        # else:
        #     print("invalid! check your entry again \n")

    while True:
        print(
            "what do you want to do?\n  1. cc for create new credentials \n 2. ds for Display existing Credentials\n 3. fc for find a credential \n 4. dc for Delete an existing credential \n 5. ex-Exit application"
        )
        shortCode = input().lower().strip()

        if shortCode == 'cc':
            print("New Credential account")
            print("\n")

            print("Account Name example Instagram")
            account = input().lower()

            print("Account username: ")
            username = input()

            print("password")
            password=input()
            Credentials.save_credentials(account,username,password)
            print('/n')
            print(
                f"Account credential for: {account} - username: {username} - password:{password} created successfully"
               )
            print("/n")

            while True:
                print(
                    "1. TP- To type your password if already have an account:\n 2.GP-To generate random password"
                )
                passwordOption = input().lower().strip()
                if passwordOption == 'TP':
                    print("Account's Password :")
                    password = input().lower().strip()
            
                elif passwordOption == 'GP':
                    password = Credentials.generatePassword()
                    # break
                else:
                    print("invalid password please try again")

                
                # Credentials.createCredential(account, username, password)

                # Credentials.save_credentials(username,password)
                # print('/n')
                # print(
                #     f"Account credential for: {account} - username: {username} - password:{password} created successfully"
                # )
                # print("/n")

        elif shortCode == "ds":
            if display_credentials():
                print("Your credentials include: \n")
                for credential in Credentials.credentials_list:
                    account = account
                    username = username
                    password = password
                    print(
                        f"Account name: {account}\n Account username: {username}\n Account password: {password}\n"
                    )
                else:
                    print("You have no saved credentials\n")

        elif shortCode == "fc":
            print("Enter the Account Name you want to search for")
            account = input().lower().strip()
            if Credentials.credentialExist(account):
                searchAccount = Credentials.find_credential(cls, account)
                print(
                    f"Account name: {searchAccount} password :{searchAccount.password}"
                )
            else:
                print("credential does not exist\n")

        elif shortCode == 'dc':
            print("Account name you would like to delete?")
            account= input().lower().strip()
            if Credentials.credentialExist(account):
                Credentials.deleteCredential(account)
                print("Account Successfully deleted")

            else:
                print("No such an account name")

        elif shortCode == 'ex':
            print("See you later!")
            # isTrue = False

        else:
            print("invalid")


main()