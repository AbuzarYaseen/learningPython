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

    @staticmethod
    def update():
        with open(Bank.dataBase, 'w') as fs:
            fs.write(json.dumps(Bank.data))


    def CreateAccount(self):
        info = {
            "name" : input("Enter your name:- "),
            "age" : int(input("Enter your age:- ")),
            "email" : input("Enter your email:- "),
            "pin" : int(input("Enter your 4 digits pin:- ")),
            "accountNumber" : 1234,
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
            Bank.update()

    def DepositAccount(self):
        pass


user = Bank()

print(f"Press 1 for creating an account. ")
print(f"Press 2 for deposit money in the bank. ")
print(f"Press 3 for withdraw money. ")
print(f"Press 4 for checking the details. ")
print(f"Press 5 for updating the details. ")
print(f"Press 6 for deleting the account. ")

check = int(input("Tell your response : "))

if check == 1:
    user.CreateAccount()

if check == 2:
    user.DepositAccount()
