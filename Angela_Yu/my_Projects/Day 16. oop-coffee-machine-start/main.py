from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#
coffee_menu = Menu()
list_item = MenuItem
resource_report = CoffeeMaker()
profit_report = MoneyMachine()

is_gamestart = True

while is_gamestart:
    options = coffee_menu.get_items()
    user_choice = input(f"What would you like? ({options}): ")
    if user_choice == "off":
        is_gamestart = False
    elif user_choice == "report":
        resource_report.report()
        profit_report.report()
    else:
        drink = coffee_menu.find_drink(user_choice)
        # drink = coffee_menu.find_drink(user_choice)
        if resource_report.is_resource_sufficient(drink) and profit_report.make_payment(drink.cost):
            resource_report.make_coffee(drink)
