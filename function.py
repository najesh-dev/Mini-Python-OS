#IMPORTS
from datetime import datetime as now
import os
# Calculator for the System
def calculator():
    user_input=input(">>")
    allowed_char='0123456789/*+-.() '
    try:
        if all(char in allowed_char for char in user_input):
            result=eval(user_input, { "__builtins__":None}, {})
            print(result)
        else:
            print("characters used not allowed!")
    except ZeroDivisionError:
        print("cannot divide by zero")
    except(SyntaxError, NameError):
        print("sorry! something went wrong")

# Shows date
def show_date():
    print(f"The date is {now.now().strftime("%d/%m/%y")}")

# shows time
def show_time():
     print(f"The time is {now.now().strftime("%H:%M:%S")}")

# clears screen
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')