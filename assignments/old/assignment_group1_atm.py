#!/usr/bin/env python
# Group assignment
# Date: March 9, 2022
# Group 1: Lucas, Aneri, Johannes, Lina
#######

import sys

class User:
    def __init__(self, name, account_number, balance, pin):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.pin = pin
        self.remainingTries = 3
        
        self.validPin = False

    def setPinValidity(self, valid):
        self.validPin = valid         

    def authenticate(self):
        while self.remainingTries > 0:
            inputPin = int(input("Please enter your pin: "))
            if inputPin == 1234:
                self.setPinValidity(True)
                return True
            else:
                self.remainingTries = self.remainingTries - 1
                print(f"Pin is wrong. Enter your pin again. You have {self.remainingTries} attempts left.")
        
        print("Maximum number of attempts reached. Login failed")
        self.setPinValidity(False)
        return False
    
class ATM_SESSION: #User
    def __init__(self, user):
        self.remainingTries = 3
        self.user = user

    def withdraw(self):
        withdraw_amount = int(input(f"Hi {self.name}!\nType the amount you wish to withdraw: "))

        if withdraw_amount > self.user.balance:
            print(f"You canot withdraw {withdraw_amount}. You current available funds are: {self.user.balance} Euro.")
            return False
        else:
            self.user.balance = self.user.balance - withdraw_amount
            print(f"Your current available funds are: {self.user.balance} Euro.")
            return True
        
    def checkBalance(self):
        print(f"Your current available funds are: {self.user.balance} Euro.")
        return True

    def changePin(self):
        pin1 = input("Type your new pin: ")
        pin2 = input("Type again your new pin: ")

        if (pin1 == pin2):
            self.user.pin = pin1
            print("PIN change succesfull!")
            return True
        else:
            print("Pin numbers do not match. Nothing changed!")
            return False

    def makeDeposit(self):
        depositAmount = int(input("Enter the amount you want to deposit: "))

        self.user.balance = self.user.balance + depositAmount
        print(f"Your new balance is {self.user.balance} Euro.")
        return True
    
    def exit(self):
        print("Thank you for choosing ABC bank! Bye!")
        sys.exit(0)
    
    def start_session(self):
        operationMenu = {
            "1": { 
                "title": "Withdraw",
                "message": "How much would you like to withdraw today?",
                "function": self.withdraw
            },
            "2": { 
                "title": "Check Balance",
                "message": "You have requested to see your balance",            
                "function": self.checkBalance
            },
            "3": {
                "title": "Change Pin",
                "message": "Please enter your new pin.",
                "function": self.changePin
            },
            "4": {
                "title": "Make Deposit",
                "message": "How much would you like to deposit today?",
                "function": self.makeDeposit                
            },
            "5": {
                "title": "Exit",
                "message": "Thank you for your choosing ABC Bank. Bye!",
                "function": self.exit,
            }
        }

        
        if self.user.authenticate():
            while(True):
                print()
                for option in operationMenu:
                    print(f"Choose {option} for operation '{operationMenu[option]['title']}'")
    
                print()
                chosen_option = input("Type the number of the operation you wish to perform: ")
                try:
                    print(operationMenu[chosen_option]['message'])
                    result = operationMenu[chosen_option]['function']()
                except KeyError:
                    print("Option not recognized.")
                    continue

                if result:
                    print("Operation successful!")
                else:
                    print("Operation failed!")
        else:
            self.exit()

    
def main():
    u1 = User(name="Tom", account_number=4566, balance=9999, pin=1234)
    atm1 = ATM_SESSION(u1)
    atm1.start_session()

if __name__ == '__main__':
    sys.exit(main())  