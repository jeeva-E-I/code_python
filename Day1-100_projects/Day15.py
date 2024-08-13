#COFFEE MACHINE PROGRAM
import os

def clear():
    if os.name =='nt':
        _ = os.system("cls")
Menu = {
    "espresso":{
        "ingredients": {
        "water": 50,
        "coffee": 18,
    },
    "cost": 1.5,
},
"latte": {
    "ingredients": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
    },
    "cost": 2.5,
},
"cappuccino": {
    "ingredients": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
    },
    "cost": 3.0,
}
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
def report():
    print(f"Water: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: ${money}")
money = 0
def working():
    global money
    user_input = input("What would you like to have: (espresso/latte/cappuccino)").lower()
    if user_input == 'report':
            report()
            working()

    if user_input in Menu:
        drink = Menu[user_input]["ingredients"]
        can_make = True
        for item in drink:
            if resources[item] < drink[item]:
                print(f"Sorry,there is not enough {item}.")
                can_make = False
                break
        if can_make:
            print("please insert your coins.")
            quarter = int(input("How many Quarters?:"))
            dimes   = int(input("How many dimes?:"))
            nickles = int(input("How many nickles?:"))
            pennies = int(input("How many pennies?:"))
            total = quarter * 0.25 + dimes *0.10 + nickles *0.05 + pennies * 0.01
            
            if total > Menu[user_input]['cost']:
                change = total - Menu[user_input]['cost']
                print(f"Here is your change ${round(change,2)} in change.")
                print(f"Enjoy your {user_input}")
                money += total
                working()
            else:
                print("Sorry that's not enough money. Money refunded")
                working()
    else:
        clear()
        print("Wrong input")
        working()
working()