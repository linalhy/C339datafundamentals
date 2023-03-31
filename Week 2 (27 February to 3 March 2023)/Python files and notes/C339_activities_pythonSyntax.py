# Activity 1
## display the text in quotation marks to an output block
Print("Python is fun!")
print("Python is fun!") #solution

## Display the text in quotation marks to an output block 
## without moving any of the existing acode to a different line
print("Python is fun!") print("Python is also easy.")
print("Python is fun", "Python is also easy.") #solution

## Display the text in quotation marks to an output block 
## without moving any of the existing code to a different line
print 
("Python is fun!")
print("Python", "is", "fun!", sep = '\n') #solution

## Change each variable name to an appropriate name for Python. 
## Do not use the same variable name more than one time.
1-name = "Rebecca" # first name
&_name = "Roberts" # last name
firstName = "Rebecca" #solution
lastName = "Roberts" #solution

## After changing the variable names, update the code below 
## to print out each name.
print(firstName)
print(lastName)

# Activity 2
# Add a new line of code that displays the text in quotation marks 
# to an output block without repeating the text in quotation marks.
output = "I love Python!"
 
# your code below this line
print(output)

# Display only the text Python is fun! to an output block 
# without deleting any of the existing code
print("Python is fun!")

print("Python is also easy!")

# Activity 3
# Create a script that prompts the user for the name of the state where they were born 
# and the name of the state where they live now. 
# Save each value in its own variable and display the input values to the user.

stateBorn = input("Which state were you born in?")
currentState = input("Which state are you currently living in?")
print("")

print("You were born in", stateBorn, "?! Nice!")
print(currentState + " is such a nice place!" )