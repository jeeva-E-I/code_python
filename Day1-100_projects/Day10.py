#SIMPLE CALCULATOR PROGRAM
import os

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |   
| |_________________| | 
|  ___ ___ ___   ___  | 
| | 7 | 8 | 9 | | + | | 
| |___|___|___| |___| | 
| | 4 | 5 | 6 | | - | | 
| |___|___|___| |___| | 
| | 1 | 2 | 3 | | x | | 
| |___|___|___| |___| | 
| | . | 0 | = | | / | | 
| |___|___|___| |___| |  
|_____________________|
"""

logo2 = """
.----------------.  .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. || .--------------. |
| |     ______   | || |      __      | || |   _____      | || |     ______   | |
| |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
.'----------------'  '----------------'  '----------------'  '----------------'. 
"""
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
        
def add(n1,n2):
    ''' Adds the two argument and returns tha value'''
    return n1 + n2
def sub(n1,n2):
    ''' subtract the two arguments and return the value'''
    return n1 - n2
def multi(n1,n2):
    ''' Multipy the two arguments and return the value'''
    return n1 * n2
def divide(n1,n2):
    '''divide the values of two arguments and return the values'''
    return n1 / n2

def calculator():
    """ simple calculator performs addition, subtractions, multiplication and division"""
    operations = {
    '+': add,
    '-': sub,
    '*': multi,
    '/': divide,
    }
    num1 = float(input("Enter the First Number: "))

    for i in operations:
        print(i)
    inp = 'y'
    while inp == 'y': 
        symbol = input("pick an operation : ")
        num2 = float(input("Enter the Second number: "))
        calculation_symbol = operations[symbol] # to get the name of the operation to call the function Ex: if user enter '+' , calculation_symbol = add
        result = calculation_symbol(num1,num2) # function call to perform mathematical operation
        print(f"{num1} {symbol} {num2} = {result}")
        num1 = result
        inp = input(f"Type 'Y' to continue calculating with{result}, or type 'N' to start a new calculation: ").lower()
        if inp == 'n':
            clear()
            calculator() # recurssive call
            
calculator()    # function trigger  