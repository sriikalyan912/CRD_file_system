class FileSystem:

    id = 0

    def __init__(self):
        pass

    def FileNotFound(self):
        print("\nSorry! No Data Found! :(\n")

    def create(self, UserData, fileName = "index.txt"):

        UserData["Id"] = self.id

        with open(fileName, "a") as file:

            file.write(str(UserData)+"\n")

        self.id += 1
    
    def read(self, UserId, fileName = "index.txt"):

        try:        
            with open(fileName, "r") as file:

                data = eval(file.readlines()[UserId].replace("\n", ""))

                print("Id\t\tName\t\t\tPhone\t\t\tEmail")
                print("-"*100)

                print(str(data["Id"])+"\t\t"+data["Name"]+"\t\t\t"+data["Phone"]+"\t\t"+data["Email"])
        
        except FileNotFoundError:
            return self.FileNotFound()


    def readAll(self, fileName = "index.txt"):

        try:

            with open(fileName, "r") as file:
                print("Id\t\tName\t\t\tPhone\t\t\tEmail")
                print("-"*100)

                lines = file.readlines()

                for line in lines:
                    data = eval(line.replace("\n", ""))
                    print(str(data["Id"])+"\t\t"+data["Name"]+"\t\t\t"+data["Phone"]+"\t\t"+data["Email"])
        
        except FileNotFoundError:
            return self.FileNotFound()

    def update(self, UserId, updateFlag, updateValue, fileName = "index.txt"):

        try:

            file = open(fileName, "r")
            
            lines = file.readlines()
            
            file.close()

            with open(fileName, "w") as file:

                for line in lines:

                    data = eval(line.replace("\n", ""))

                    if data["Id"] == UserId:
                        
                        if updateFlag == 1:
                            data["Name"] = updateValue
                        elif updateFlag == 2:
                            data["Phone"] = updateValue
                        elif updateFlag == 3:
                            data["Email"] = updateValue

                    file.write(str(data)+"\n")
        
        except FileNotFoundError:
            return self.FileNotFound()

    
    def delete(self, UserId, fileName = "index.txt"):

        try:
        
            file = open(fileName, "r")
            lines = file.readlines()
            lines.remove(lines[UserId])
            file.close()

            flag = False

            with open(fileName, "w") as file:
                
                for line in lines:
                    
                    data = eval(line.replace("\n", ""))

                    if((data["Id"]-1) == UserId):
                        flag = True

                    if flag:
                        data["Id"] -= 1
                    
                    file.write(str(data)+"\n")

            self.id -= 1

        except FileNotFoundError:
            return self.FileNotFound()

