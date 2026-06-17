from pathlib import Path
import os

def readFileAndFolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")



def createFile():
    try:
        readFileAndFolder()
        name = input("Tell your file name : ")
        p = Path(name)
        if not p.exists():
            with open(p, 'w') as fs:
                data = input("What you want to write ? :")
                fs.write(data)

            print("File creted...")
        else:
            print("This file already exists.")

    except Exception as err:
        print(f"An error occured as {err}")

def readFile():
    try:
        readFileAndFolder()
        name = input("Which file you wants to read : ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)

            print("File Read Successfully")

        else:
            print("File does not exists...")
    except Exception as err:
        print(f"An error occured as {err}")

def updateFile():
    try:
        readFileAndFolder()
        name = input("Enter file name to update it : ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing the file name :- ")
            print("Press 2 for overwriting the file data :- ")
            print("Press 3 for append the content of file :- ")

            res = int(input("Tell your response :- "))

            if res == 1:
                newName = input("Tell your new name :- ")
                newPath = Path(newName)
                p.rename(newPath)

            if res ==2:
                with open(p, 'w') as fs:
                    data = input("Tell what you want to write. This will overwrite the file:- ")
                    fs.write(data)

            if res == 3:
                with open(p, 'a') as fs:
                    data = input("Tell what you want to append:- ")
                    fs.write(" "+data)
        else:
            print("File does not exists...")
            
    except Exception as err:
        print(f"An error occured as {err}")

def deleteFile():
    try:
        readFileAndFolder()
        name = input("Enter file name to delete :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)

            print("File removed successfully")
        else: 
            print("No such file exists.")
            
    except Exception as err:
                print(f"An error occured as {err}")


print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deletion a file")

check = int(input("Tell your response : "))

if check == 1:
    createFile()
if check == 2:
    readFile()
if check == 3:
    updateFile()
if check == 4:
    deleteFile()