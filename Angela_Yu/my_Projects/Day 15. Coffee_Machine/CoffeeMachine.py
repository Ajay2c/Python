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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def insert_coin():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01

    total_coin = quarters + dimes + nickles + pennies
    return total_coin


def report():
    Water = str(resources["water"]) + "ml"
    Milk = str(resources["milk"]) + "ml"
    Coffee = str(resources["coffee"]) + "g"
    print(f"Water: {Water}")
    print(f"Milk: {Milk}")
    print(f"Coffee: {Coffee}")


def machine_stock(user_want):
    if user_want == "espresso":
        resources["water"] -= 50
        resources["coffee"] -= 18
    elif user_want == "latte":
        resources["water"] -= 200
        resources["coffee"] -= 24
        resources["milk"] -= 150
    elif user_want == "cappuccino":
        resources["water"] -= 250
        resources["coffee"] -= 24
        resources["milk"] -= 100
    return


def machine_works(user_guess, money):
    global drink
    if user_guess == "espresso":
        drink = MENU[user_guess]
        having_coin = insert_coin()
        if having_coin == 1.50 or having_coin > 1.50:
            change = round(having_coin - 1.50, 2)
            money += 1.50
            if resource_efficient(drink["ingredients"]):
                machine_stock(user_guess)
                print(f"Here is ${change} in change")
                print("Here is your espresso ☕️. Enjoy!")
        else:
            print("sorry you have not enough money, here your amount")
    elif user_guess == "latte":
        drink = MENU[user_guess]
        having_coin = insert_coin()
        if having_coin == 2.50 or having_coin > 2.50:
            change = round(having_coin - 2.50, 2)
            money += 2.50
            if resource_efficient(drink["ingredients"]):
                machine_stock(user_guess)
                print(f"Here is ${change} in change")
                print("Here is your latte ☕️. Enjoy!")
        else:
            print("sorry you have not enough money, here your amount")
    elif user_guess == "cappuccino":
        drink = MENU[user_guess]
        having_coin = insert_coin()
        if having_coin == 3.00 or having_coin > 3.00:
            change = round(having_coin - 3.00, 2)
            money += 3.00
            if resource_efficient(drink["ingredients"]):
                machine_stock(user_guess)
                print(f"Here is ${change} in change")
                print("Here is your cappuccino ☕️. Enjoy!")
        else:
            print("sorry you have not enough money, here your amount")
    else:
        print("please enter the valid data")
    return money


def resource_efficient(order_items):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for items in order_items:
        if order_items[items] > resources[items]:
            print(f"Sorry there is not enough {items}.")
            return False
        return True


machine_start = True

while machine_start:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        machine_start = False
    elif user_choice == "report":
        report()
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        if resource_efficient(drink["ingredients"]):
            machine_works(user_choice, profit)
