from os import mkdir,path
from json import load, loads, dump
from time import time
from re import search


def findUser(UserName):

    if not path.isdir('Save'):
        mkdir('Save')

    if UserName == 'Data':

        if path.isfile('Save/Data.json'):

            with open('Save/Data.json', 'r+') as f:
                dataS = f.read()
                try:
                    data = load(f)
                    fileSize = len(str(data).encode('utf-8'))
                    
                except:
                    data = {}
                    fileSize = 0
           
        else:

            with open('Save/Data.json', 'w') as f:

                f.write('{}')
                data = {}
                fileSize = 0
                

    else:

        if path.isfile('Save/'+UserName+'.json'):

            with open('Save/'+UserName+'.json', 'r') as f:

                dataS = f.read()
                try:
                    data = loads(dataS)
                    fileSize = len(str(data).encode('utf-8'))
                    
                except:
                    data = {}
                    fileSize = 0
            

        else:

            with open('Save/'+UserName+'.json', 'w') as f:

                f.write('{}')
                data = {}
                fileSize = 0
    
    return(data,fileSize)

def create(UserName = 'Data'):

    data,fileSize = findUser(UserName)

    while True:

        while True:

            key = input('\nEmployee Id (Key):\t')

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

        timelimite = input('\nTime Limite [sec] (optional):\t')

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

        with open('Save/'+UserName+'.json', 'w+') as f:
            dump(data, f, indent=2)

        print('\nNew Value added Successfully!')
    else:

        print("\nSorry! File size limit exceeded.")

def read(UserName = 'Data'):

    data = findUser(UserName)[0]

    if len(data) == 0:
        print('\Unable to performe this operations. The DataStore is EMPTY!')
        return
    
    while True:
        
        key = input('\nEmployeID to Search:\t')

        with open('Save/'+UserName+'.json','r') as f:
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

def delete(UserName = 'Data'):

    data,fileSize = findUser(UserName)

    with open('Save/'+UserName+'.json','r') as f:
        data = load(f)

    while True:

        if len(data) == 0:
            print('\nUnable to perform this Operations. The DataStore is already EMPTY!')
            return

        else:
            while True:
                
                key = input('\nEmployeID to Delete:\t')

                if key in data:

                    timelimit = data.get(key).get('TimeLimit')

                    if timelimit == None or timelimit > time():

                        fileSize = fileSize - len(str(data[key]).encode('utf-8'))
                        del data[key]

                        with  open('Save/'+UserName+'.json', 'w') as f:
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
        
