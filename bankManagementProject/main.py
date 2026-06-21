# Features List
# 1-Bank Account
# 2-Deposit Money
# 3-Withdraw Money
# 4-Details
# 5-Update Details
# 6-Delete Account

import json
import random
import string
from pathlib import Path


class Bank:
    dataBase = Path(__file__).with_name("data.json")
    data = []

    try:
        if Path(dataBase).exists():
            with open(dataBase, 'r') as fs:
                file_data = fs.read().strip()
                data = json.loads(file_data) if file_data else []
        else:
            print("No such file exists.")
    except Exception as err:
        print(f"an exception occured as {err}")

    @classmethod
    def __update(cls):
        with open(cls.dataBase, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountGenerate(cls):
        alphabets = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*",k=1)

        id = alphabets+num+spchar
        random.shuffle(id)
        return "".join(id)
        



    def createAccount(self):
        info = {
            "name" : input("Enter your name:- "),
            "age" : int(input("Enter your age:- ")),
            "email" : input("Enter your email:- "),
            "pin" : int(input("Enter your 4 digits pin:- ")),
            "accountNumber" : Bank.__accountGenerate(),
            "balance" : 0
        }
        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry you cannot create your account.")
        else:
            print("Account has been created successfully!")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account number.")
            Bank.data.append(info)
            Bank.__update()

    def depositMoney(self):
        accNo = input("Enter your account number:- ")
        pin = int(input("Enter your pin:- "))

        userData = [i for i in Bank.data if i['accountNumber'] == accNo and i['pin'] == pin]
        if userData == False:
            print("Sorry no data found")
        else:
            amount = int(input("How much amount you wants to deposit "))
            if amount > 10000 or amount < 0:
                print("Amount is too much. Deposit less than 10,000 and above 0")
            else:
                userData[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully!")

    def withdrawMoney(self):
        accNo = input("Enter your account number:- ")
        pin = int(input("Enter your pin:- "))

        userData = [i for i in Bank.data if i['accountNumber'] == accNo and i['pin'] == pin]
        if userData == False:
            print("Sorry no data found")
        else:
            amount = int(input("How much amount you wants to withdraw "))
            if userData[0]['balance'] < amount:
                print("Sorry you don't have enough money.")
            else:
                userData[0]['balance'] -= amount
                Bank.__update()
                print("Amount withdrew successfully!")
                
    def showDetails(self):
        accNo = input("Enter your account number:- ")
        pin = int(input("Enter your pin:- "))

        userData = [i for i in Bank.data if i['accountNumber'] == accNo and i['pin'] == pin]
        print("Your Info is below \n\n")

        for i in userData[0]: 
            print(f"{i} : {userData[0][i]}")
            

    def updateDetails(self):
        accNo = input("Enter your account number:- ")
        pin = int(input("Enter your pin:- "))

        userData = [i for i in Bank.data if i['accountNumber'] == accNo and i['pin'] == pin]
        if userData == False:
            print("Sorry no data found")
        else:
            print("You cannot change age, account number, balance.")
            print("Fill the details for change or leave it to empty if no change.")

            newData = {
                "name" : input("Enter your new name or press enter to skip: "),
                "email" : input("Enter your new email or press enter to skip: "),
                "pin" : input("Enter new pin or press enter to skip: ")
            }

            if newData["name"] == "":
                newData["name"] = userData[0]["name"]
            if newData["email"] == "":
                newData["email"] = userData[0]["email"] 
            if newData["pin"] == "":
                newData["pin"] = userData[0]["pin"]

            newData['age'] = userData[0]["age"]
            newData['balance'] = userData[0]["balance"]
            newData['accountNumber'] = userData[0]["accountNumber"]

            if type(newData['pin']) == str:
                newData['pin'] = int(newData['pin'])

            for i in newData:
                if newData[i] == userData[0][i]:
                    continue
                else:
                    userData[0][i] = newData[i]
            
            Bank.__update()

            print("Details updated successfully!")

    def deleteAccount(self):
        accNo = input("Enter your account number:- ")
        pin = int(input("Enter your pin:- "))

        userData = [i for i in Bank.data if i['accountNumber'] == accNo and i['pin'] == pin]
        if userData == False:
            print("Sorry no data found")
        else:
            check = input("Press y if you wants to delete the account. Or press n")

            if check == 'n' or check == 'N':
                pass
            else:
                index = Bank.data.index(userData[0])
                Bank.data.pop(index)

                print("Account deleted successfully!")
                Bank.__update()

user = Bank()

print(f"Press 1 for creating an account. ")
print(f"Press 2 for deposit money in the bank. ")
print(f"Press 3 for withdraw money. ")
print(f"Press 4 for checking the details. ")
print(f"Press 5 for updating the details. ")
print(f"Press 6 for deleting the account. ")

check = int(input("Tell your response : "))

if check == 1:
    user.createAccount()

if check == 2:
    user.depositMoney()

if check == 3:
    user.withdrawMoney()

if check == 4:
    user.showDetails()

if check == 5:
    user.updateDetails()

if check == 6:
    user.deleteAccount()