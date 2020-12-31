*********CRD Filesystem**********

A file-based key-value data store that supports the basic 
CRD (create, read, and delete) operations. This data will store in the local storage.

Files: main.py, operations.py 

System Requirements:
*******************************
* OS	Windows 10/8/7, Linux *
* Python 3.6 or more	      *
*******************************

main.py ---->

 It’s an application which allows each user to have an individual data-store to store data. 
 If he/she is a new user than it create a new data store file.   
 Note: In this app I used Employee data.
 This application can perform three main operations create, read, delete. These operations are defined and declared in operations.py file.

operations.py ---->

create ()
 This function creates a new key-value and stores into a local file with the user’s name.
 If the file doesn’t exist then then is creates a new file with the user’s name and stores into that file.

 Conditions:
 1. It won’t store the data into a file if the file size exceeded 1GB.
 2. It’s won’t accept if the key chars greater than 32 chars.
 3. It’s won’t accept if the value size greater than 16kb.

read ()
 It’s gets key from user and fetch its value and return it.
 Conditions:
 1.It returns ’None’ value if the key is not present.
 2.It won’t return the value if the time limit exceeded.  

delete ()
 It’s gets key from user and remove the value from the datastore.
 Conditions:
 1. It won’t delete the key-value if the time limit exceeded.
 2. It won’t delete in the key not available.


