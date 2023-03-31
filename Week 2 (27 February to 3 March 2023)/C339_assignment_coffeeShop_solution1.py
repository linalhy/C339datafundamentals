# Name: Lina Lau
# Date: March 6, 2023
# Title: Assignment - Coffee Shop


def inputCheck(userInput, validValues):
    lc_userInput = userInput.lower()
    if lc_userInput in validValues:
        return lc_userInput
    else:
        print(f"{userInput} not recognized.")
        return None
                

def askQuestion(msg, options):
    while True:
        answer = input(msg)
        if inputCheck(answer, options):
            break
    return answer

coffeeSize = askQuestion(
    "Cup size? \n You can choose from either small, medium, or large.", 
    ("small", "medium", "large"))
coffeeType = askQuestion(
    "Coffee type? \n We have brewed, espresso, and cold press.", 
    ("brewed", "espresso", "cold press"))
coffeeFlavour = askQuestion(
    "Any flavouring? \n Choose between none, hazelnut, vanilla, and caramel. ", 
    ("none", "hazelnut", "vanilla", "caramel"))

def cost(coffeeSize, coffeeType, coffeeFlavour):
    if coffeeSize == "small":
        basePrice = 2.00
    elif coffeeSize == "medium":
        basePrice = 3.00
    else:
        basePrice = 4.00

    if coffeeType == "espresso":
        addPrice = basePrice + 0.50
    elif coffeeType == "cold brew":
        addPrice = basePrice + 1.00
    else:
        addPrice = basePrice + 0.00

    if coffeeFlavour == "none":
        finalPrice = addPrice + 0.00
    else:
        finalPrice = addPrice + 0.50

    return finalPrice 

coffeeCost = cost(coffeeSize, coffeeType, coffeeFlavour)

print(f"You chose a {coffeeSize} {coffeeType} coffee with {coffeeFlavour} flavouring")
print(f"Your cup of coffee costs {coffeeCost} EUR")
print(f"The total price with a tip is {round(coffeeCost*1.15, 2)} EUR")