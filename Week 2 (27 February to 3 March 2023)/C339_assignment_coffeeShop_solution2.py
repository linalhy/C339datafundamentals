#!/usr/bin/env python
import sys

def inputCheck(userInput, validValues):
    # lc_userInput is a local variable
    #      - This means, the variable only exists within the function (in this case, inputCheck)
    #      - This is also referred to as "the scope of the variable"
    lc_userInput = userInput.lower()
    if lc_userInput in validValues:
        return lc_userInput
    else:
        print(f"{userInput} not recognized.")
        return None
               

def askQuestion(msg, options):
    while True:
        answer = input(msg + "\n")
        if inputCheck(answer, options):
            break
    return answer

def cost(coffeeSize, coffeeType, coffeeFlavour):
    price_db = {
        "size": { 
            "small" : 2.00, 
            "medium" : 3.00, 
            "large": 4.00,
        },
        "type": { 
            "brewed": 0, 
            "espresso": 0.5, 
            "cold brew": 1,
        },
        "flavour": {
            "none": 0,
            "hazelnut": 0.5, 
            "vanilla": 0.5, 
            "caramel": 0.5,
        },
    }

    return price_db['size'][coffeeSize] + price_db['type'][coffeeType] + price_db['flavour'][coffeeFlavour]

def main():
    coffeeSize = askQuestion(
        "Cup size? \n You can choose from either small, medium, or large.", 
        ("small", "medium", "large"))
    coffeeType = askQuestion(
        "Coffee type? \n We have brewed, espresso, and cold press.", 
        ("brewed", "espresso", "cold press"))
    coffeeFlavour = askQuestion(
        "Any flavouring? \n Choose between none, hazelnut, vanilla, and caramel. ", 
        ("none", "hazelnut", "vanilla", "caramel"))

    coffeeCost = cost(coffeeSize, coffeeType, coffeeFlavour)

    print(f"You chose a {coffeeSize} {coffeeType} coffee with {coffeeFlavour} flavouring")
    print(f"Your cup of coffee costs {coffeeCost} EUR")
    print(f"The total price with a tip is {round(coffeeCost*1.15, 2)} EUR")

    return 0


if __name__ == '__main__':
    sys.exit(main())