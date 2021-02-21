from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

while True:
    options = menu.get_items()
    order = input(f"What would you like? ({options}): ")
    if order == "stop":
        break
        
    elif order == "report":
        coffee.report()
        money.report()

    else:
        drink = menu.find_drink(order)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)
