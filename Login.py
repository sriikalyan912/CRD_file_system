import os
from crud import FileSystem

class FileStorage(FileSystem):
    
    def fileOperations(self, userName):
        try:

            while True:

                print("\n"+("-"*100))

                print("1. Create\n2. Read\n3. Read All\n4. Update\n5. Delete\n6. Exit\n")

                Userchoise = int(input("Enter you'r choise: "))

                if(Userchoise == 1):

                    print("\n-------CREATE--------\n")
                    user = {}
                    
                    user["Name"] = input("Name: ")
                    user["Phone"] = input("Phone No.: ")
                    user["Email"] = input("Email: ")

                    self.create(user, userName)

                elif(Userchoise == 2):

                    print("\n-------READ-------\n")
                    
                    userId = int(input("User ID: "))

                    self.read(userId, userName)

                elif(Userchoise == 3):

                    print("\n-------READ ALL-------\n")
                    
                    self.readAll(userName)

                elif(Userchoise == 4):
                    
                    print("\n-------UPDATE-------\n")

                    userId = int(input("User ID: "))

                    flag = int(input("You want to update\n1. Name\n2. Phone\n3. Email\nYour choise: "))

                    if flag == 1:
                        value = input("Name: ")
                    elif flag == 2:
                        value = input("Phone: ")
                    elif flag == 3:
                        value = input("Email: ")

                    self.update(userId, flag, value, userName)

                elif(Userchoise == 5):
                    
                    print("\n-------DELETE-------\n")

                    userId = int(input("User ID: "))

                    self.delete(userId, userName)

                elif(Userchoise == 6):
                    
                    return

                else:
                    print("\nPlease enter correct input\n")

                    return self.fileOperations(userName)

        except:
            
            print("\nENTER A VALID INPUT!!!\n")
            
            self.fileOperations(userName)
  

class Login:
    
    global SLASH

    def __init__(self):
        
        
        if not os.path.isfile(SLASH.join([os.getcwd(), "logins.txt"])):
            
            file = open("logins.txt", 'w')
            file.close()

    def __validateUser(self, userName, userPswd):
        
        credentials = []
        
        with open("logins.txt", "r") as logins:
            credentials = logins.readlines()

        for user in credentials:

            data = eval(user.replace("\n", ""))

            if data['userName'] == userName:
                if data['userPswd'] == userPswd:
                    return True
                
                else:
                    return False

        return False

    def __isNameAvailable(self, userName):
        credentials = []
        
        with open("logins.txt", "r") as logins:
            credentials = logins.readlines()

        for user in credentials:

            data = eval(user.replace("\n", ""))

            if data['userName'] == userName:
                return False
        return True

    def signIn(self):

        print("\nSIGN IN----------------|\n")

        userName = input("User Name: ")
        userPswd = input("User PassWord: ")

        if self.__validateUser(userName, userPswd):
            if os.path.isdir(SLASH.join([os.getcwd(), userName])):
                os.chdir(SLASH.join([os.getcwd(), userName]))

            else:
                os.mkdir(SLASH.join([os.getcwd(), userName]))
                os.chdir(SLASH.join([os.getcwd(), userName]))

            fileStorage = FileStorage()

            fileStorage.fileOperations(userName)

            os.chdir("..")
        
        else:
            print("User Name or Password are Invalide!\n")

            return
 
    def signUp(self):
        
        print("\nSIGN UP----------------|\n")

        userLogins = dict()
        
        userLogins["userName"] = input("Create User Name: ")

        if self.__isNameAvailable(userLogins["userName"]):
            
            userLogins["userPswd"] = input("Create PassWord: ")

            with open("logins.txt", 'a') as logins:
                logins.write("".join([str(userLogins), "\n"]))

            print(f"New Account for user {userLogins['userName']} is Sucessfully created!\n")

            return
        
        else:
            print(f"\nUser name { userLogins['userName'] } is not available!")
            return self.signUp()

    def signOut(self):
        pass


SLASH = ""

if os.name == 'nt':
    SLASH = "\\"
else:
    SLASH = "/"

if os.path.isdir(SLASH.join([os.getcwd(),"save"])):
    os.chdir(SLASH.join([os.getcwd(),"save"]))

else:
    os.makedirs("save")
    os.chdir(SLASH.join([os.getcwd(),"save"]))
    
print(os.getcwd())

while True:

    try:
    
        login = Login()
        
        print("-"*10+"Login Page"+"-"*10)

        choise = int(input("1. SignIn\n2. SignUp\nYour Choise: "))

        if choise == 1:
            login.signIn()

        elif choise == 2:
            login.signUp()

        elif choise == 3:
            exit()
        
        else:
            print("\nPlease! Enter Valid Input!\n")

        print("-"*100)

    except:
        print("\nPlease! Enter Valid Input!\n")

        continue
