#COFFEE MACHINE USING CLASSES AND OBJECTS
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

can_make = True

money_machine.report()
coffee_maker.report()

while can_make:
    options = menu.get_items()
    choice = input(f"what would you like? ({options})")
    if choice == "off":
        can_make = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        