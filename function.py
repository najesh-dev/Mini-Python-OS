#IMPORTS
from datetime import datetime as now
import os
# Calculator for the System
def calculator():
    try:
        num1=float(input("Enter the first no. : "))
        num2=float(input("Enter the second no. : "))
        op=input("\nChoose the operand(+,-,*,/): ")

        if op=="+":
            print(f"The sum is {num1 + num2}")
        elif op=="-":
            print(f"The difference is { num1-num2}")
        elif op=="*":
            print(f"The product is {num1*num2}")
        elif op=="/":
            if num2!="0":
                print(f"The quotient is {num1/num2}")
            else:
                print("Sorry! cannot divide")
        else:
            print("Invalid Operand")
    except ValueError:
        print("Please enter a number!")

# Shows date
def show_date():
    print(f"The date is {now.now().strftime("%d/%m/%y")}")

# shows time
def show_time():
     print(f"The time is {now.now().strftime("%H:%M:%S")}")

# clears screen
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')