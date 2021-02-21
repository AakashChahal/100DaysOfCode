MENU = {
    "espresso": {
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
}

print("""
    .oooooo.     .oooooo.   oooooooooooo oooooooooooo oooooooooooo oooooooooooo
 d8P'  `Y8b   d8P'  `Y8b  `888'     `8 `888'     `8 `888'     `8 `888'     `8
888          888      888  888          888          888          888
888          888      888  888oooo8     888oooo8     888oooo8     888oooo8
888          888      888  888    "     888    "     888    "     888    "
`88b    ooo  `88b    d88'  888          888          888       o  888       o
 `Y8bood8P'   `Y8bood8P'  o888o        o888o        o888ooooood8 o888ooooood8

 ooo        ooooo       .o.         .oooooo.   ooooo   ooooo ooooo ooooo      ooo oooooooooooo
`88.       .888'      .888.       d8P'  `Y8b  `888'   `888' `888' `888b.     `8' `888'     `8
 888b     d'888      .8"888.     888           888     888   888   8 `88b.    8   888
 8 Y88. .P  888     .8' `888.    888           888ooooo888   888   8   `88b.  8   888oooo8
 8  `888'   888    .88ooo8888.   888           888     888   888   8     `88b.8   888    "
 8    Y     888   .8'     `888.  `88b    ooo   888     888   888   8       `888   888       o
o8o        o888o o88o     o8888o  `Y8bood8P'  o888o   o888o o888o o8o        `8  o888ooooood8
""")

money = 0


def check_resources():
    """
    Function is used to check if there are enough resources available to make
    the coffe user asked for.
    returns False if not enough resources available, and
    returns True if there resources are enough to make Coffee.
    """
    global resources
    if resources["water"] < MENU[user_input]["ingredients"]["water"]:
        return False
    elif resources["coffee"] < MENU[user_input]["ingredients"]["coffee"]:
        return False
    elif resources["milk"] < MENU[user_input]["ingredients"]["coffee"] and not user_input == "espresso":
        return False
    return True


def make_coffee():
    """
    make_coffee() function is used to ask user the coffee they want
    and money they have.
    makes the Coffee if there are enough resources and enough Money
    entered by user.
    refunds the money to user if they gave less amount of Money.
    gives feedback if there are enough resources for the Coffee user want.
    """
    global money
    if check_resources():
        print("Please insert coins.")
        quarters = float(input("How many quarters?: ")) * 0.25
        dimes = float(input("How many dimes?: ")) * 0.10
        nickles = float(input("How many nickles?: ")) * 0.05
        pennies = float(input("How many pennies?: ")) * 0.01
        user_money = quarters + dimes + nickles + pennies
        if user_money < MENU[user_input]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            money += MENU[user_input]['cost']
            resources["water"] -= MENU[user_input]["ingredients"]["water"]
            resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
            if not user_input == "espresso":
                resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
            print(f"Here is your {user_input} ☕️Enjoy!")
            print(f"Here is ${round(user_money - MENU[user_input]['cost'], 2)}")

    else:
        print("There is not enough resources.")


while True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")

    elif user_input == "stop":
        break

    elif user_input in MENU:
        make_coffee()

    else:
        print("Wrong Entry!!!")
