#%%

class Temp:
    CLASS_VARIABLE_COUNT = 0 # Anything not specified using 'self' can be either a class or static variable
    def __init__(self, name):
        self.name = name

t1 = Temp("Lina")
t2 = Temp("Potato")
t1.CLASS_VARIABLE_COUNT = 5 
print(t1.CLASS_VARIABLE_COUNT)
print(t2.CLASS_VARIABLE_COUNT) # -> 0 # always use class name to set a static variable
# %%
class Temp:
    CLASS_VARIABLE_COUNT = 0 
    def __init__(self, name):
        self.name = name
        print("first")
    # When there are two identical constucts, the second one overrides the first one
    def __init__(self, name):
        self.name = name
        print("second")

t1 = Temp("Lina") # -> t1 = Temp("Lina") second
t2 = Temp("Potato") # -> t2 = Temp("Potato") second

# %%

class Employee:
    COMPANY_NAME = "Wiley"
    def __init__(self, firstName, lastName, age, emp_id):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.age = emp_id
    
    def get_email(self):
        return f"{self.firstName}.{self.lastName}@{Employee.COMPANY_NAME}.com"
    
    @classmethod
    def change_company(cls, newName):
        cls.newName = newName

# instance variable when accessed static variable scope would be limited to only
# that instance variable and global object. If you have to set static variable, always use className.staticmethod
#never change static variable by static variable

print(dir(Employee)) # returns all methods of a class

e1 = Employee("Lina", "Lau", 25, 123456)
e2 = Employee("Potato", "Chip", 30, 123457)
print(e1.COMPANY_NAME) # -> Wiley
print(Employee.__dict__)

#%%
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.
# A child class will inherit the data structure of the parent class, not the data values. 

#! WITHOUT INHERITANCE:
class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

class Magazine:
    def __init__(self, title, publisher, period, price):
        self.title = title
        self.publisher = publisher
        self.period = period
        self.price = price

class Newspaper:
    def __init_(self, title, publisher, period, price):
        self.title = title
        self.publisher = publisher
        self.period = period
        self.price = price

#! WITH INHERITANCE:
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    
class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

class Book(Publication):
    def __init__(self, title, author, price, pages):
        super().__init__(title, price)
        self.author = author
        self.pages = pages

class Magazine(Periodical):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price, period, publisher)

class Newspaper(Periodical):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price, period, publisher)

b1 = Book("Gone with the Potato", "Spud P", 14.90, 3)
m1 = Magazine("Potatoes", 5.90, "Monthly", "Earth Publishing") 
n1 = Newspaper("The Potato Times", 1.50, "Daily", "Earth Publishing")

print(b1.__dict__)
print(m1.__dict__)
print(n1.__dict__)

# Is Magazine a subclass of Publication?
print(issubclass(Magazine, Publication)) # -> True
# Is Book a subclass of Newspaper?
print(issubclass(Book, Newspaper))# -> False

#Is m1 an instance of Periodical?
print(isinstance(m1, Periodical)) # -> True
#Is m1 an instance of object?
print(isinstance(m1, object)) # -> True


# %%
# When a class does not have a parent to inherit from, it inherits from an object

class Restaurant:
    def __init__(self):
        super().__init__()
        self.supplier = "GoodVeg Co."
        self.name = "Potato Restaurant"

class Bar: 
    def __init__(self):
        super().__init__()
        self.supplier = "OkayDrinks Co."
        self.name = "The Old Potato Bar"

# With multiple inheritance, super keyword needs to be defined in all parents if needed in a child class

class RestaurantBar(Restaurant, Bar):
    def __init__(self):
        super().__init__()
    
    def showprops(self):
        print(self.supplier)
        print(self.name)

restaurantBar = RestaurantBar()
print(restaurantBar.showprops()) 
# Returns the restaurant and supplier name (i.e. Potato Restaurant and GoodVeg Co.) 
# because the 1st object to inherit from has higher priority.
# So when we switch the positions of Restaurant and Bar as below,

class RestaurantBar(Bar, Restaurant):
    def __init__(self):
        super().__init__()
    
    def showprops(self):
        print(self.supplier)
        print(self.name)

restaurantBar = RestaurantBar()
print(restaurantBar.showprops())

# the Bar and the Bar supplier names (i.e. The Old Potato Bar and OkayDrinks Co.) are printed)

# %%

class Parent1:
    def __init__(self, param1):       
        self.param1 = param1 # super keyword not required here  because already specified in Child class.


class Parent2:
    def __init__(self, param2):
        self.param2=param2

class Child(Parent1, Parent2):
    def __init__(self, param1, param2, param3):
        super().__init__(param1) 
        super(Parent1, self).__init__(param2) # find the next class after parent 1 (i.e. parent2)
        self.param3=param3
    
    def showprops(self):
        print(self.param1)
        print(self.param2)
        print(self.param3)

# Creating a 'Child' object
c = Child("123","456","789")

c.showprops()

#%%
# Use default value with dataclass. 
# Note that non-default arguments cannot follow default arguments

from dataclasses import dataclass, field
import random
def page_check(e):

    # TODO: Write code here to connect db or get input from cache,
    # TODO sql query to connect db, or get the output and push it back to
    # TODO default factory.
    return e + int(random.randrange(0,5))

# Immutable class you can specify '(frozen=True)' and no alteration can be made.
@dataclass(frozen=True)

# Defining the data class
class Book:
    title: str = "No Title" # defining default values
    author: str = "No Author" 
    pages: int = field (default_factory = lambda: page_check(5)) # lambda: enables the insertion of a parameter to the field function.
    price: float = field (default = 0)
    def __post_init__(self):
        self.description = f"{self.title} by {self.author}"

#b1 = Book("A book", "Lina Lau", 150, 19.90)
#b2 = Book("A book", "Lina Lau", 150, 19.90)

b1 = Book()
b2 = Book()

print(b1 == b2)
print(b1.__dict__)

# %%

@dataclass
class Company:
    COMPANY_NAME = "youtube"

class Employee(Company):    
        first_name: str = "No first name provided"
        last_name: str = "No last name provided"
        department: str = "No department provided"
        salary: float = field (default = 0)
        def __post_init__(self):
            self.email = (f"{self.first_name}.{self.last_name}@{Company.COMPANY_NAME}.com").lower()
            
e1 = Employee("LiNa", "lAu", "Sales", 50000)
print(e1.email)


# %%

from abc import ABC, abstractmethod

class GraphicShape(ABC): # base class
    def __init__(self):
        super().__init__()
    # abstract method is a method that has no (empty) body.
    # If the logic of the method is unknown, declary abstractmethod
    # then the class inherits the abstractmethod and implements it.
    # abstractmethod describes the template.
    @abstractmethod 
    def calcArea(self):
        pass

class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass

class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)

    def toJSON(self):
        return f"{{\"Circle\" :{str(self.calcArea())}}}"
    
class Square(GraphicShape, JSONify):
    def __init__(self, side1, side2):
        super().__init__()
        self.side1 = side1
        self.side2 = side2
    
    def calcArea(self):
        return self.side1 * self.side2
    
    def toJSON(self):
       return f"{{\"Square\" : {str(self.calcArea())}}}"

c = Circle(10)
print(c.calcArea())
print(c.toJSON())
c.toJSON()

s = Square(5, 3)
print(s.calcArea())
print(s.toJSON())
#%%
## abstractmethod Example 1:
## Scenario:

class Diapers: # base class
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def diaperSize(self):
        pass

    @abstractmethod
    def JSONify(self):
        pass

class AdultDiapers(Diapers):
    def __init__(self, thickness, length, height):
        super().__init__()
        self.thickness = thickness
        self.length = length
        self.height = height

    def diaperSize(self):
        return self.thickness * (0.5 * (self.length * self.height))
    
    def toJSON(self):
        return f""
        

adult_diapers = AdultDiapers(
    int(input("What is the thickness of your product in mm?")),
    int(input("What is the length of your product in mm?")),
    int(input("What is the height of your product in mm?"))
    )   

print(f"The adult diaper size will be {adult_diapers.diaperSize()} mm^3")

#%%
# As an example, you may a program that needs to write / read data in a variety of formats
# This would be a good use case for the abstract class

from abc import ABC, abstractmethod

class Reader(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def load_file(self, path):
        pass

    def content(self):
        return self.content


class XML_Reader(Reader):
    def __init__(self):
        super().__init__()
        
    def load_file(self, path):
        self.path = path
        sys.open(path) ....
    
    def content(self):
       return super().content()


class CSV_Reader(Reader):
    def __init__(self):
        super().__init__()
        
    def load_file(self, path):
        self.path = path
        sys.open(path) ....

    def content(self):
        return super().content()





# %%
# if the same function is defined in the child class, it overrides that of the parent.

class Animal:
    def speak(self):
        print("speaking")
    
class Dog(Animal):
    def speak(self):
        print("barking")

d = Dog()
d.speak
# %%

class Bank:
    def getInterestRate(self):
        return 0.05
    
class Barclays(Bank):
    def getInterestRate(self):
        return 0.07
    
class DeutscheBank(Bank):
    def getInterestRate(self):
        return super().getInterestRate() # returns interest rate specified in Bank
    
class HSBC(Bank):
    def getInterestRate(self):
        return 0.065
    
b1 = Barclays()
b2 = DeutscheBank()
b3 = HSBC()

print(b1.getInterestRate()) # -> 0.07
print(b2.getInterestRate()) # -> 0.05
print(b3.getInterestRate()) # -> 0.065

#%%

if you want to avoid the method overriding, use the super method

class Animal:
    def speak(self):
        print("speaking")
class Dog(Animal):
    def speak(self):
        super().speak()
        print("barking")

d =Dog()
d.speak()   

#speaking
barking