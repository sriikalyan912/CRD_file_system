from re import search
from os import mkdir,path
from json import load, loads, dump
from time import time


def findUser(UserName, Path):
    
    if not path.isdir(Path):
        mkdir(Path)

    if UserName == 'Data':

        if path.isfile(Path+'/Data.json'):

            with open(Path+'/Data.json', 'r+') as f:
                dataS = f.read()
                try:
                    data = load(f)
                    fileSize = len(str(data).encode('utf-8'))
                    
                except:
                    data = {}
                    fileSize = 0
           
        else:

            with open(Path+'/Data.json', 'w') as f:

                f.write('{}')
                data = {}
                fileSize = 0
                

    else:

        if path.isfile(Path+'/'+UserName+'.json'):

            with open(Path+'/'+UserName+'.json', 'r') as f:

                dataS = f.read()
                try:
                    data = loads(dataS)
                    fileSize = len(str(data).encode('utf-8'))
                    
                except:
                    data = {}
                    fileSize = 0
            

        else:

            with open(Path+'/'+UserName+'.json', 'w') as f:

                f.write('{}')
                data = {}
                fileSize = 0
    
    return(data,fileSize)

def create(Path,UserName = 'Data'):

    data,fileSize = findUser(UserName, Path)

    while True:

        while True:

            key = input('\nKey:\t')

            if not key.isalpha():
                print('\nKey can\'t be nothing or should not contains Space, Numbers, SpecialCharacters!')
                continue

            else:
                break

        if len(key) < 32:         

            if key in data:
                print('\nThe given Key is already Exist.\nTry giving another Key.')
                continue

            else:
                break
                
        else:
            print('\nOMG! the given key is too long. length(key) > 32char')

    print('\n(values)')

    value = {}
        
    while True:

        EmployeName = input('\nName:\t')

        if not EmployeName.isalpha():
            print('\nName should not contains Space, Numbers, or SpecialCharacters!')
            continue

        else:
            value['Name'] = EmployeName
            break

    while True:

        EmployePhone = input('\nPhone:\t')

        if (not EmployePhone.isnumeric()) or len(EmployePhone)!=10:
                print('\nPhone No. should only contains Numbers and 10 Digits.')
                continue

        else:
            value['Phone'] = EmployePhone
            break
        
    while True:

        EmployeEmail = input('\nEm@il:\t')

        emailFormat = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        
        if not search(emailFormat,EmployeEmail):
            print('\nPlease! Enter a valid Email ID.')
            continue

        else:
            value['Email'] = EmployeEmail
            break
        
    while True:

        timelimite = input('\nTime Limite (sec):\t')

        if timelimite == '':
            value['TimeLimit'] = None
            break

        elif timelimite.isalpha() or not timelimite.isnumeric():
            print('\nTime limite must be a Integer or decimal.')
            continue

        else:
            value['TimeLimit'] = (int(timelimite))+time()
            break
    
    if len(str(value).encode('utf-8')) > (16*1024):
        print('\nOMG! The given value is too large to store. size(values) > 16Kb')
        return

    newFileSize = fileSize + len(str({key:value}).encode('utf-8'))

    if newFileSize < (1024**3):
        
        data[key] = value

        fileSize = newFileSize

        with open(Path+'/'+UserName+'.json', 'w+') as f:
            dump(data, f, indent=2)

        print('\nNew Value added Successfully!')
    else:

        print("\nSorry! File size limit exceeded.")

def read(Path,UserName = 'Data'):

    data = findUser(UserName, Path)[0]

    if len(data) == 0:
        print('\nyou can\'t perform this Operations. The DataStore is EMPTY!')
        return
    
    while True:
        
        key = input('\nEmployeID to Search:\t')

        with open(Path+'/'+UserName+'.json','r') as f:
            data = load(f)

        if len(data) == 0:
            print('\nNo data has found!')
            return

        values = data.get(key)
        
        if values:
            
            if values.get('TimeLimit') != None and values.get('TimeLimit') < time():
                print('\nSorry! Time has Expired to perform this operation.')
                
            else:
                return values
        else:
            print('\nSorry! Data not Found.')

        return None

def delete(Path,UserName = 'Data'):

    data,fileSize = findUser(UserName,Path)

    with open(Path+'/'+UserName+'.json','r') as f:
        data = load(f)

    while True:

        if len(data) == 0:
            print('\nyou can\'t perform this Operations. The DataStore is already EMPTY!')
            return

        else:
            while True:
                
                key = input('\nEmployeID to Delete:\t')

                if key in data:

                    timelimit = data.get(key).get('TimeLimit')

                    if timelimit == None or timelimit > time():

                        fileSize = fileSize - len(str(data[key]).encode('utf-8'))
                        del data[key]

                        with  open(Path+'/'+UserName+'.json', 'w') as f:
                            dump(data, f, indent=2)
                        print('\nValue Deleted Successfully!')
                        break
                    
                    else:
                        print('\nSorry! Time has Expired to performe this Operation.')
                        break
                else:
                    print('\nOops! The key dose not Exist in DataStore.')
                    break
        return None
        
