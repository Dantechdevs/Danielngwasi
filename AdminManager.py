from Parent import User
import re


class AdminManager(User):
    def addInfo(self, fullname, password):
        with open('AMUser.txt', 'a+') as file:
            file.write(f"(username: {fullname}),(password:{password})\n")

    def deleteInfo(self, username):
        with open('AMUser.txt', 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if username in line:
                    file.truncate()

    def searchingInfo(self, info):
        with open('AMUser.txt', 'r') as file:
            if str(info) in file.read():
                print(f"{info} exists in the system")
            else:
                print(f"{info} doesnt exist in the system")

    def viewInfo(self):
        with open('AMUser.txt', 'r') as file:
            for i in file.readlines():
                print(i, "\n")

    def addRecord(self, fullname, age, address, account_id, password, email, phoneNo, schedule, user_type):
        with open("AMRecords.txt", "a+") as file:
            file.write(
                f'''"fullname": {fullname},"age": {age},"address": {address},"account_id": {account_id},"password": {password},"email": {email},"phoneNo": {phoneNo},"schedule": {schedule}"user_type": {user_type}\n''')

    def deleteRecord(self, account_id):
        with open('AMRecords.txt', 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if account_id in line:
                    file.truncate()

    def searchRecord(self, account_id):
        with open("AMRecords.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if str(account_id) in line:
                    print(line)
                    return line
            print("record doesnt exist")

    def printAllRecords(self):
        with open("AMRecords.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)

    def addPackage(self, id, package, price):
        with open("AMPackages_Prices.txt", "a+") as file:
            file.write(f'''id: {id}, package: {package},price: {price}\n''')

    def deletePackage(self, package):
        with open('AMPackages_Prices.txt', 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if package in line:
                    file.truncate()

    def searchPackage(self, id):
        with open("AMPackages_Prices.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if str(id) in line:
                    print(f'package -> {line}')
                    return
            print("package does not exist")

    def printAllPackage(self):
        with open("AMPackages_Prices.txt", "r") as file:
            for line in file.readlines():
                print(line)

    def viewAllUsernames(self):
        with open("AMUser.txt", "r+") as file:
            regex = re.compile(r'\s\w+\s\w+')
            for line in file.readlines():
                mo = regex.search(str(line))
                print(mo.group())
