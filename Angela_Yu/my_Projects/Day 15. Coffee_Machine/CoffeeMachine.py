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


def resources_sufficient(order_items):
    for item in order_items:
        if  resources[item] <= order_items[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def insert_coin():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01

    total_coin = quarters + dimes + nickles + pennies
    return total_coin


def transaction_successful(total_user_coins, order_drink_cost):
    global profit
    drink_cost = order_drink_cost["cost"]
    if total_user_coins >= drink_cost:
        profit += drink_cost
        change = round(total_user_coins - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(user_drink):
    for item in user_drink:
        resources[item] -= user_drink[item]
    return True    


is_machine_on = True
while is_machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        is_machine_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: {profit}")
    elif user_choice in MENU:
        drink = MENU[user_choice]
        coffee_ingredient = drink["ingredients"]
        if resources_sufficient(coffee_ingredient):
            having_coins = insert_coin()
            if transaction_successful(having_coins, drink):
                if make_coffee(coffee_ingredient):
                    print(f"Here is your {user_choice} ☕️. Enjoy!")
                


