# Python object-oriented programming

class Book: 
    # title is an instance variable, for that we would define bothget an set methods
    def __init__(self, title, pages, author, price):
        # Instance variables:
        self.title = title
        self.pages = pages
        self.author = author
        self.price = price
        self.__secret = "This book refers to content from another book"

    # Optional attribute

    def __str__(self):
        return f"{self.title} {self.pages} {self.author} {self.price}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.title}, {self.pages}, {self.author}, {self.price}, {self.version})"

    # !IMPORTANT! There are different methods (e.g. ge -> "greater than" and lt -> "lower than")
    # __eq__ is a special method defined in a class that allows us to compare two objects or that class for equality
    # For example, here we compare title and author only.
    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Cannot compare a non book object to a book object")
        else:
            return(self.title == value.title and self.author == value.author and self.title == value.title)
    
    def setDiscount(self, amount):
        self._discount = amount # an underscore is used when if you don't want an attribute 
        # to be defined as default in an init method.

    def display(self):
        print(" title %s \n pages %s \n author %s \n price %d \n " 
              %(self.title, self.pages, self.author, self.price))

    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
     # If we want to access an attribute, we need a method to do so:
    def getTitle(self): # getter method
        return self.title
    
    # If we want to set the title, then set title method
    def setTitle(self, title): # Setter method
        self.title = title

# Creating class car:
class Car:
    def __init__(self, name):
        self.name = name
    def __eq__(self, __o: object) -> bool:
        print("call from Car")
        return False


    
# TODO Create book instance variable b1 and b2    
b1 = Book("Title1", "234", "Lina Lau", 15.00)
b2 = Book("Title2", 135, "Good Potato", 20.00)
b3 = Book("Title3", "234", "Star Fruit", 15.00)

print(b1.title) # bad practice as we are directly accessing variable
b1.setTitle("NewTitle")
print(b1.getTitle())

# Using the optional discount constructor
print(b1.getPrice())
b1.setDiscount(0.10)
print(b3.getPrice())

print(b1)
b1.display() # print not needed here as it is already declared in the display constructor
print(b2)

# How to access secret variable: instanceVar._className__secretVar
print(b1.__secret)
print(b1._Book__secret)

# Deleting a particular attribute from the instance variable.
del b1.price

# Deleting the object itself.
del b1

# Comparison
print("Comparison is ", b1 == b2)
print("Comparison is ", b1 == b3)

# comparing objects from two different classes
car1 = Car("Toyota")
print("error example:", car1 == b1)
print("error example:", b1 == car1)  

b2 = Book("Title2")
print(b2.title)
b2.setTitle("NewTitle2")
print(b2.title) # Prints new title after running the above command
print(b2.getPrice())

my_list = list(range(1, 10, 3))
print(repr(my_list)) # -> [1,4,7]
print(my_list.__str__())

#%%

class Book:
    def __init__(self, title):
        self.title = title
    
class Newspaper:
    def __init__(self, name):
        self.name = name

b1 = Book("The catcher in the rain")
b2 = Book("The Grapes of Wrath")
n1 = Newspaper("The washington times")
n2 = Newspaper("The new york times")

print(type(b1)) # -> <class '__main__.Book'>
print(type(b2)) # -> <class '__main__.Book'>

print(type(b1) == type(b2)) # -> True
print(type(n1) == type(n2)) # -> True

print(isinstance(b1, Book)) # -> True
print(isinstance(n1, Newspaper)) # -> True

print(isinstance(n2, object)) # -> True

# Parent class

#%%

# Complete class hierarchy

# Define 3 count variables and increment it in instance method, 
# static method and class method and print it.
class Book:
    # TODO properties defined at class level shared by all instance variables
    # class variables are static if named with double underscore at the start
    __COUNT = 0 # STATIC and constant
    BOOK_TYPES=("HARDCOVER", "PAPERBACK", "EBOOK") # STATIC constants
    BOOK_CLASSLEVEL_COUNT = 0 # STATIC constants

    # TODO __properties are hidden from other classes
    __booklist = None

    def __init__(self, title, bookType):
        self.title = title
        self.instance_count = 0
        if (not bookType in Book.BOOK_TYPES):
            raise ValueError(f"We do not support the geature you are asking: {bookType}")
        else:
            self.booktype = bookType

    @staticmethod
    def incrementCount(): # Not associated with b1 or b2. Associated with class 'Book'/
        Book.__COUNT = Book.__COUNT + 1
        return Book.__COUNT
    
    # static methods cannot access any class or instance arguments:
    @staticmethod
    def getBookList(arg1,arg2): # this method is sto set something at class level
      #  print(Book.BOOK_TYPES)
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist
    
    @classmethod #similar to getter and setter
    def getBookTypes(cls):
        return cls.BOOK_TYPES
    
    @classmethod
    def returnCount(cls):
        return cls.__COUNT

    def setTitle(self, newTitle):
        self.title = newTitle

    def setCount(self): # association with b1 instance variable. Not associated with 'Book' class.
        self.count = self.count + 1

#
print("Book Types:", Book.getBookTypes()) # -> Book Types: ('HARDCOVER', 'PAPERBACK', 'EBOOK')
b1 = Book("Title1", "HARDCOVER")
b1.setCount()
b2 = Book("Title2", "PAPERBACK")
b2.setCount()

theBook = Book.getBookList()
theBook.append(b1)
theBook.append(b2) 
print(theBook)

print(Book.incrementCount())
print(b1.count)
print(b2.count)
# %%
