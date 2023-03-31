# Date: March 10, 2023.
# %%
try :  
    #print(1/0)   # failure codnition code can be written here
    raise RuntimeError("you are wrong")

except ZeroDivisionError as error:   # only when you get an error
    print("an error occured",error)
except Exception as ex:   # only when you get an error
    print("from exception",ex)

finally:  # these is always getting executed
    print("hi how are ayoposadjklasndksanknd")
    print("I am god")

# %%
# CREATING CUSTOM ERRORS
# Anything can be an error.

class customError(Exception):
    # this section can be replaced with 'pass'    
    def __init__(self, message):
        self.message = message

    def __str__(self) -> str:
        return f"{type(self).__name__}: {self.message} written by Lina."
    
print("Welcome to the program!")
#raise customError("Welcome to your first custom error in Python!")

# if you want to break the flow of your code, place 'raise SystemExit' at the exact point you want your code to stop executing.
# %%

class customError(Exception):
    pass

print("Welcome to the program!")
#raise customError("Welcome to your first custom error in Python!")
# %%
# CREATING CUSTOM EXCEPTIONS
class CustomException(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code
    def __str__(self) -> str:
        return f"{self.code} : {self.message}"

print("Hello!")
raise CustomException("This is a custom exception message for class C339", 123454)

# %%
# REGULAR EXPRESSIONS (REGEX) IN PYTHON



