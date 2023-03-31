# Python
# Date: March 9, 2023.

#%%

# DECORATORS
# Python decorators is a technique for changing the behavior of an
#  existing function, without changing actual code inside the function.

# what is the use :- 
# deposit money or withdraw money you can have a function call audit
# Here, the passed parameter can be a variable or function.
# However, this time its a function (i.e. 'my_function')

def my_decorator(my_function):

    def inner_decorator():
        print("this happend before")     # you add the balance
        my_function()    # when you call 'my_function', the 'my_decorated' function is executed   # here you do the audit function call
        print("this happened after")   # ensure database is updated
        print("This happend at end!!!!")  # drop a message on console
    return inner_decorator

@my_decorator
def my_decorated():
    print("welcome to first lecture of class")

# whenever you write a python file, the first function that gets invoked is the __main__ function
if __name__ == "__main__":    # these code check name of the function is it main
    my_decorated()

# %%

import datetime

def my_decorator(my_function):

    def inner_decorator():
        print("this happend before", datetime.datetime.utcnow())     # you add the balance
        my_function()    # when you call 'my_function', the 'my_decorated' function is executed   # here you do the audit function call
        print("this happened after", datetime.datetime.utcnow())   # ensure database is updated
        print("This happend at end!!!!")  # drop a message on console
    return inner_decorator

@my_decorator
def my_decorated():
    print("welcome to first lecture of class", datetime.datetime.utcnow())

#%%

## Decorator 2
import datetime
def my_decorator(inner):
    def inner_decorator(num_copy):
        print("this happend before", datetime.datetime.utcnow())  
        inner(int(num_copy) + 1)    
        print("this happened after", datetime.datetime.utcnow())   
        print("This happend at end!!!!")
    return inner_decorator

@my_decorator
def decorated(number):
    print("this happened: "+str(number)) # Without str(), print won't work as it would say int and string cannot be complied

if __name__ == "__main__":
    decorated(5)

# %%

# Error handling using 'try:', 'except:', and 'finally:'
try:
    print(1/0)
    print(1/2)

except Exception as ex: # only when an error happens
    print("You can't do this:", ex)

finally:# always executed
    print("I am in 'finally' and I will always be here!")

#%%
#from __future__ import print_function
def handle_exception(func_name):
    def inner(a, b):
        try:
            return func_name(a, b)
        except Exception as ex:
            print("We got following exception", ex)
    return inner

@handle_exception

def divide(x,y):
    return x/y

divide(8,0)

#%%
def op_exception(func_name):
    def inner(*args, **kwargs):
        try:
            return func_name(*args, **kwargs) #*args are arrays, *kwargs are key words
        except Exception as ex:
            print("Oh no! You can't do that: ", ex)
        finally:
            print(f"Yay! {func_name} was succesful!")
    return inner

@op_exception
def subtract(*args):
    s = 0
    for number in args:
        s -= number 
    return s

@op_exception
def addition(*args):
    all = 0
    for number in args:
        all += number
    return all

def kwDec(func):
    def inner(*args,**kwargs):
        if 'my_param' in kwargs:
            my_param =kwargs['my_param']
            print(f"my_param value: {my_param}")
        else:
            print("my_param is not found in kwargs")
    return inner

@kwDec
def my_function(*args,**kwargs):
    pass

#subtract(8, 1, 2, "abc")
subtract(8, 1, 2)

#addition(1, 4, 2, "def", 3)
addition(1, 4, 2, -3, 0.6)

addition(8, 0, 1, 2, 3, 5)

subtract(8, 0, 1, 2, 3, 5)


# %%

# Operator overloading
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
    #these function is created by me

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    
    def __sub__(self,other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)
    
    def multiply(self,other):
        x= self.x * other.x
        y = self.y * other.y 
        return Point(x,y)
    
    def dot(self, no):
        return self.x*no.x+self.y*no.y
    
p1 = Point(5, 6)
p2 = Point(2, 3)

print(p1-p2)    # 

p1.multiply(p2)

x=p1.dot(p2)  # 8
x
# %%
