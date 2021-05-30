import getpass
import random
import pyperclip

class User:
     """class"""

     userList =[]

def __init__(self, username, password):
        
        " magic  constructor method "

        self.username = username
        self.password = password
        self.isLoggedin = False


def CreateUser(username,password):

    """method"""

    newUser = User(username,password)
    return newUser

def login(self):
    print("logged in successfully")

def saveUser(self):
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
    def verify_user (cls,username,password):

        aUser =""
        for user in User.userList:
            if(user.username == username and user.password == password):
                aUser == user.username
                return aUser

    def __init__(self, account, username, password):
        """
            cedentials to be stored
        """
        self.account  = account
        self.userName = userName
        self.password = password

    def save_details(self):

        Credentials.credentials_list.append(self)

    def delete_credentials(self):

        Credentials.credentials_list.remove(self)


    @classmethod

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

    def if_credential_exist(cls, account):

        "checks if the credential exists from the list"

        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False

        @classmethod
        def display_credentials(Cls):
            "returns all credentials in the list"
            return cls.credentials_list

        def generatePassword(stringLength=8):
            "generates a random password "

            password = string.ascii_uppercase + strinng.ascii_lowercase + string.digits + "!@#$%^&*"
            return '',join(random.choice(password) for i in range (stringLength))

      
        def copypassword(parameter_list):
             """
             method that allows copying of password to keyboard
             """
             pass



def main():

    isTrue = True

    print("Welcome to password Locker.Here you manage your passwords and even generate new passwords.")
    while isTrue == True:

        print(
            "Please enter one to proceed:\n\n 1. ca for Create new Account\n 2. lg for login\n 3. ex for Exit" )
        shortCode = input("").lower().strip()
        if shortCode == "ca":
            print("Sign Up Account")
            print("*"*20)
            print("Username:")
            username = input()
            while True:
                print("1. Type TP s to type your own password:\n  or \n 2. GP for generating random password")
                passwordOption = input().lower().strip()

                if passwordOption == 'tp':
                    print("Enter Your Password")
                    password = input("password\n")

                    break
                elif passwordOption == 'gp':
                    password = generatePassword()
                    break
                else:
                    print("invalid pasword")

            CreateUser=User.createUser(username, password)
            User.saveUser(createUser)
            print("\n")
    
            print(f"Hi {username}, your account has been created successfully! \n Your password is: {password}")
            
    
        elif shortCode  == 'lg':
             print("*"*50)
             print("Enter your username and password")
             print("*"*50)

             print("Username")
             username = input()
             print("password")
             password = input()

             for user in User.userList:
                 if username ==user.username:
                    if user.password == password:
                        print(user.login())
                    else:
                        print("password invalid")
                        break
                 else:
                     print("username invalid")
                     break
                 break

        elif shortCode =='ex':

            print("See you later!!")
            break
        else:
            print("invalid shortcode\n")




        
main()