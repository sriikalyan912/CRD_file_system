from operations import create, read, delete
from os import mkdir,path

print('\nxxxxx A File based key-value data store that supports CRD operations. xxxxx')
    
while True:
    
    UserName = input('\nUserName:\t')
    
    if path.isdir('Save'):
        if path.isfile('Save/'+UserName+'.json'):
            print('\nWelcome '+UserName)
        else:
            print('\nWelcome new User '+UserName)
    else:
        mkdir('Save')
        
    while True:
        choise = input('\n[1] Create\n[2] Read\n[3] Delete\n[4] Logout\n\nEnter you\'re choise:\t')
                
        if choise == '1':
            create(UserName)

        elif choise == '2':
            values = read(UserName)
            
            if values != None:
                print()
                keys = list(values.keys())[:-1]
                vals = list(values.values())[:-1]
                for i,j in zip(keys,vals):
                    print(i+' ----> '+j)

        elif choise == '3':
            delete(UserName)

        elif choise == '4':
            break

        else:
            print('\nEnter a valid choise.')
            continue

    print('\n###Logout Successful###')

    while True:
        redo = input('\nWant to continue [y/n]?\t').lower()

        if redo == 'n':
            quit()
        elif redo == 'y':
            break
        else:
            print('\nPick a valid Options!')
