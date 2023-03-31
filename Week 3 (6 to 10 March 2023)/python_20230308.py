# Python 
# Date: March 8, 2023

#%%
# Composition
class Author:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        return f"{self.firstName} {self.lastName}"



class Book:
    def __init__(self, title, price, author = None):
        self.title = title
        self.price = price
        self.author = author
        self.chapters = []

    def addChapters(self, name, pages):
        self.chapters.append((name, pages))

a1 = Author("Leo", "Tolstoy")

b1 = Book("War and peace", 15.00, a1)
b1.addChapters("Chapter 1", 5)
b1.addChapters("Chapter 2", 12)
b1.addChapters("Chapter 3", 20)

b2 = Book("Gone with the Wind", 19.90, a1)

print(b1.__dict__)
print(b1.author)
    
# %%
# Importing packages 
from author import Author

class Book:
    def __init__(self, title, price, author = None):
        self.title = title
        self.price = price
        self.author = author
        self.chapters = []

    def addChapters(self, name, pages):
        self.chapters.append((name, pages))

a1 = Author("Leo", "Tolstoy")

b1 = Book("War and peace", 15.00, a1)
b1.addChapters("Chapter 1", 5)
b1.addChapters("Chapter 2", 12)
b1.addChapters("Chapter 3", 20)

b2 = Book("Gone with the Wind", 19.90, a1)

print(b1.__dict__)
print(b1.author)


# %%
class Book:
    def __init__(self,title,author,pages,price):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages
        self.discount = 0.1

    def __str__(self):
        return f"{self.title} by {self.author} costs {self.price}"

    def __getattribute__(self, name: str) :
        if (name == "price"):
            p = super().__getattribute__("price")
            d = super().__getattribute__("discount")
            return p -(p * d)
        return super().__getattribute__(name)
    
    def __setattr__(self,name: str, value: str):
        if name =='price':
            if type(value) is not float:
                raise ValueError("The 'price' attribute must be float!")
        return super().__setattr__(name,value)
    
    def __getattr__(self,name):
        return f"'{name}' is not a variable in book class!"
    
b1 = Book("War and Peace","Leo Tolstoy", 185, 50.00)
b2 = Book("The Potato Tales","Spuddy McSpudderson", 254, 30.00)

print(b1)
print(b2)

b1.price = 38 # -> returns a ValueError
b1.price=float(40)
print(b1)

print(b1.randomprop) # -> returns an error: 'randomprop' is not a variable in Book class!

# %%
# Call function '__call__' allows an instance of a class to be called as a function.


class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author} costs {self.price}"
    
    def __call__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
    
b1 = Book("War and Peace","Leo Tolstoy", 185, 50.00)
b2 = Book("The Potato Tales","Spuddy McSpudderson", 254, 30.00)

print(b1)
print(b2)

# Here we call the instance of the class as a function and change the values of the instance
# __call__ method is called
# Now, lets say we want to change the properties of b1, we can do it this way:
b1("War and Potatoes","Leo Potato", 115, 45.50) 

# Instead of this way:
b1 = Book("War and Potato","Leo Potato", 115, 45.89)
print(b1)

# Without __call__, an error happens: TypeError: 'Book' object is not callable

# %%

class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author} costs {self.price}"
    
    # Defines behaviour for greater-than-or-equal-to operator
    # Here we are comparing book prices
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Cannot compare 'Book' with non-'Book'")
        return self.price >= value.price
    
    # Defines behaviour for less-than behaviour 
    # Here we are comparing book prices   
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Cannot compare 'Book' with non-'Book'")
        return self.price < value.price
    
b1 = Book("War and Peace","Leo Tolstoy", 185, 50.00)
b2 = Book("The Potato Tales","Spuddy McSpudderson", 254, 30.00)
b3 = Book("Peaches and Potatoes","Apple Tree", 125, 35.98)
b4 = Book("The Wandering Snail","Coffee Cup", 256, 12.49)

# Here, the 1st parameter is 'self' and the 2nd parameter is 'value' in __gt__ and __lt__ functions
print(b2 >= b1)
print(b2 < b1)
print(b4 == b1)

print(type(b1)) # -> <class '__main__.Book'>


book_list = [b1,b4,b3,b2]
print([book.__dict__ for book in book_list])

book_list.sort() # Sorting books by price in ascending order
print([book.pages for book in book_list])


#%%

# POLYMORPHISM
# Polymorphism is an ability in OOP to use a common interface for multiple forms (data types) 
#

class Parrot:
    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:
    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)


# %%
class Person:
      def __init__(self, firstname='Jinesh', lastname='Ranawat', age=96, country='England', city='London'):
            self.firstname = firstname
            self.lastname = lastname
            self.age = age
            self.country = country
            self.city = city
            self.skills = [] #list

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      
      def add_skill(self, skill):
            self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('Python')
p1.add_skill('MATLAB')
p1.add_skill('R')
p2 = Person('Ben', 'Doe', 30, 'Finland', 'Tampere')
print(p2.person_info())
print(p1.skills)
print(p2.skills)

class Student(Person):
    def __init__ (self, firstname='Jinesh', lastname='Ranawat',age=96, country='England', city='London', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
        
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Arthur', 'Curry', 33, 'England', 'London','male')
s2 = Student('Emily', 'Carter', 28, 'England', 'Manchester','female')
print(s1.person_info())
s1.add_skill('HTML')
s1.add_skill('CSS')
s1.add_skill('JavaScript')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

#%%
# Polymorphism with Inheritance: Overriding (or Method Overriding)
# Overriding is the process of redefining methods inherited from the parent class in the child class.
# It it called overriding because a method added to the child class will override a method with the same name
# in the parent class. 

# TODO Example:

class Company:
    def __init__(self, companyName, companyID):
        self.companyName = companyName
        self.companyID = companyID

    def getDetails(self):
        print(f"{self.companyName} is identified as {self.companyID}")

class Department(Company):
    def __init__(self, deptName, deptID, location, country):
        self.deptName = deptName
        self.deptID = deptID
        self.location = location
        self.country = country
    
    # Here, we override the 'getDetails' method in the parent class (i.e. 'Company') to return more information.
    def getDetails(self):
        print(f"{self.deptName} (Department ID: {self.deptID}) is located in {self.location}, {self.country}")
        

dept = Department("Procurement", "234F2", "Berlin", "Germany")
dept.getDetails()

# %%
# Polymorphism with Class Methods.
# Polymorphism is the ability to take different forms. 
# Polymorphism in Python allows the user to define methods in the child class with the same name as defined in their parent class. 




# %%
# ENCAPSULATION
# Encapsulation is a concept of bundling data and mathods within a single unit. 
# For example, when a class is created, encapsulation is being implemented.
# A class is an example of encapsulation, because it binds all data members (instance variables) and methods
# into a single unit.

# TODO Example:
# TODO In this example, we are implementing encapsulation by creating an 'Employee' class consisting of
# TODO instance variables (i.e.'firstName', 'lastName', 'salary', and 'project'), 
# TODO as well as methods (i.e 'showEmployee' and 'showWork')

class Employee:
    def __init__(self, firstName, lastName, salary, project):
        # name, salary, and project are data members (aka instance variables)
        self.firstName = firstName  
        self.lastName = lastName      
        self.salary = salary
        self.project = project 
    
    # method to show employee information:
    def showEmployee(self):
        # accessing public data members 'firstName', 'lastName', and 'salary'
        print(f"{self.firstName} {self.lastName}'s salary is {self.salary}")
    
    # method to show employee's work:
    def showWork(self):
        print(f"{self.firstName} {self.lastName} is working on project '{self.project}'")

# Creating an object of the 'Employee' class:
emp = Employee("Potato", "Wedges", 50000, "Muffins")

# Calling public method of 'Employee' class:
emp.showEmployee()
emp.showWork()

# %%
# Using encapsulation, we can hide an object's internal representation from outside.
# This is called information hiding.

# Encapsulation is a way to restrict access to methods and variables from outside the class.
# When working with sensitive information, providing access to all variables within the class
# is not a good idea.

# Encapsulation offers a way to access the required variable without providing the program
# full-fledged  access to all variables in a class. This mechanism is used to protect the data
# of an object from other objects.

# Encapsulation can be achieved by declaring the instance variables and methods of a class as private or 
# protected.
# In Python, we use single underscore (_) and double underscores (__) to achieve this.

# Access modifiers limit access to variables and methods of a class. 
# Python provides three types of access modifiers: private, public, and protected.

# Public member: Accessible anywhere from outside class.
# Private member: Accesible within class
# Protected member: Accesible within class and its sub-classes.

# TODO Example:
class Employee:
    def __init__(self, name, salary):
        self.name = name        # Public instances (accessible within/outside of 'Employee' class)
        self.project = project  # Protected instances (accessible within 'Employee' class and its sub-classes)
        self.salary = salary    # Private instances (accessible only within 'Employee' class)

# TODO Public Member example:
class Product:
    def __init__(self, name, price):
        # public instances
        self.name = name
        self.price = price
    
    # Public instance methods
    def showProduct(self):
        # accessing public instances
        print(f"Product name: {self.name} , Price of {self.name}: {self.price}")

# Creating an object of 'Product' class
product1 = Product("Potato", 1.49)

# Accessing public instances (i.e. name and price)
print(f"Product name: {product1.name} , Price of {product1.name}: {product1.price}")

# Calling a public method
product1.showProduct()

# %%
# TODO Private member example:

class Product:
    def __init__(self, name, id, costPrice):
        self.name = name             # Public instance variable
        self.id = id                 # Public instance variable
        self.__costPrice = costPrice # Private instance variable, only accessible within 'Product' class.

product2 = Product("Private potato", "123ABC", 2.45)

print(f"Price of {product2.name} is {product2.__costPrice}") 
# -> AttributeError: 'Product' object has no attribute '__costPrice'
# In the above example, the salary is a private variable. 
# We can’t access the private variable from the outside of that class.

# We can access private variables from outside a class using:
## Create public method to access private variables
## Use name mangling

# TODO Creating public method to access private variables
class Product:
    def __init__(self, name, id, costPrice):
        self.name = name            
        self.id = id                 
        self.__costPrice = costPrice 

    # ! We can access private variables using public instance methods
    def showDetails(self):
        print(f"The cost price of {self.name} is {self.__costPrice}")

product2 = Product("Private potato", "123ABC", 2.45)

product2.showDetails() # Output: The cost price of Private potato is 2.45

# TODO Name mangling to access private variables
class Product:
    def __init__(self, name, id, costPrice):
        self.name = name            
        self.id = id                 
        self.__costPrice = costPrice # Private variable

product3 = Product("Private potato 2", "1234ABCD", 3.14)

print(f"Name of product is '{product3.name}'")

# Direct access to private variable using name mangling (e.g. objectName._Class__privateVariable)
print(f"The cost price of {product3.name} is {product3._Product__costPrice}")


# %%
# Protected data members are used when implementing inheritance, while allowing access of data members to child classes.
# TODO Protected member example:

class Company:
    def __init__(self):
        self._project = "Muffins" # Protected member

# Child class
class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)
    
    def display(self):
        print(f"Employee name: {self.name}\n Assigned to {self._project} project")

emp2 = Employee("Mushroom")
emp2.display()

print(f"Project: {emp2._project}")

# %%

# GETTERS AND SETTERS IN PYTHON
# In order to implement proper encapsulation in python, we need to use getters and setters.
# Getter method accesses data variables.
# Setter method modifies data variables.

# Getters and setters are often used to avoid direct access to private variables, and
# to add validation logic for setting a value.

# TODO Getter and Setter Example:
class Student:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.__age = age

    # Getter method:
    def get_age(self):
        return(self.__age)
    
    # Setter method:
    def set_age(self,age):
        self.__age = age

student1 = Student("Lina", "Lau", 25)

# Retreiving age using getter:
print(f"Name: {student1.firstName} {student1.lastName}, Age: {student1.get_age()}")

# Changing age using setter:
student1.set_age(28)

# Retreiving age using getter after setting the age with 'set_age()':
print(f"Name: {student1.firstName} {student1.lastName}, Age: {student1.get_age()}")

# %%

# TODO Using encapsulation to implement information hiding and apply additional validation before 
# TODO changing values of instance variables

class Student:
    def __init__(self, firstName, lastName, age, id):
        # Private instance variable
        self.firstName = firstName
        self.lastName = lastName
        # Restricting access to private instance variable