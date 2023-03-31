#!/usr/bin/env python
# Name: Lina Lau
# Date: March 13, 2023.
# Assignment: Burger Shop
##########################

import sys
class FoodItem:
    def __init__(self, itemName, itemPrice):
        self.itemName = itemName
        self.itemPrice = itemPrice

class Burger(FoodItem):
    def __init__(self, itemName, itemPrice):
        super().__init__(itemName, itemPrice)

class Side(FoodItem):
    def __init__(self, itemName, itemPrice, itemSize):
        super().__init__(itemName, itemPrice)
        self.itemSize = itemSize

class Drink(FoodItem):
    def __init__(self, itemName, itemPrice, itemSize):
        super().__init__(itemName, itemPrice)
        self.itemSize = itemSize

class Combo(FoodItem):
    def __init__(self, itemName, itemPrice):
        super().__init__(itemName, itemPrice)

class Order: 
    ID = 1
    def __init__(self):
        self.id = Order.ID
        self.totalCost = 0
        self.continueOrdering = True
        Order.ID = Order.ID + 1

    def getOrderID(self):
        return self.id
    
    def greeting(self):
        customerFName = (input("Please enter your first name: ").capitalize())
        customerLName = (input("Please enter your last name: ").capitalize())
        print("")
        print("")
        customerName = print(f"Hello {customerFName} {customerLName} Welcome to Potato Burgers!")
        print("")
        return customerName 
    
    def mealCost(self): 
        orderDB = {
            "burger": {
                "chicken": 4.50,
                "beef" : 5.00,
                "veggie": 3.50,
            },
            "side":{
                "fries": 1.50,
                "salad": 2.00,
                "onion rings": 1.50,
                "potato wedges": 1.50,
            },
            "drink": {
                "coke": 2.50,
                "sprite": 2.50,
                "water": 1.50,
                "beer": 1.50,
            },
            "combo": {
                "small": 0.10,
                "medium": 0.15,
                "large": 0.20,
            }
        }
        
        cost = orderDB["burger"][self.burger] + orderDB["side"][self.side] + orderDB["drink"][self.drink] 
        finalCost = cost - (cost * (orderDB["combo"][self.combo]))
        return finalCost

    def startOrderSession(self):
        while self.continueOrdering:
            self.burger = askQuestion(
            "Which burger would you like? Choose between:\n Chicken\n Beef\n Veggie.", 
            ("chicken", "beef", "veggie"))
            self.side = askQuestion(
            "Would you like some sides?  Choose between:\n Fries\n Salad\n Onion rings\n Potato wedges.", 
            ("fries", "salad", "onion rings", "potato wedges"))
            self.drink = askQuestion(
            "Please choose your drink!  Choose between:\n Coke\n Sprite\n water\n beer. ", 
            ("coke", "sprite", "water", "beer"))
            self.combo = askQuestion(
            "Would you like to make that a combo meal?\nChoose between small, medium, and large. ",
            ("small", "medium", "large"))
            self.next = askQuestion(
            "Would you like to add anything else to your order?", ("yes", "no"))
        
            finalOrderCost = self.mealCost()
            self.totalCost = self.totalCost + finalOrderCost

            print(f"You chose a {self.burger} burger with {self.side} and a {self.drink} as part of a {self.combo} combo meal. The total accumulated cost is {self.totalCost}")

            if self.next == "no":
                self.continueOrdering = False

        print(f"Your order ID is {self.getOrderID():03d}.")
        print(f"Your order costs {round(self.totalCost, 3)} EUR.") #finalCost -> totalCost

def inputCheck(userInput, validValues):
    lc_userInput = userInput.lower()
    if lc_userInput in validValues:
        return lc_userInput
    else:
        print(f"{userInput} not recognized.")
        return None
               
def askQuestion(msg, options):
    while True:
        answer = input(msg + "\n").lower()
        if inputCheck(answer, options):
            break
    return answer

def main():
    while (True):
        order = Order()
        order.greeting()
        order.startOrderSession()

if __name__ == "__main__":
    sys.exit(main())
