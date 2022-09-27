from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
items_menu = Menu()
is_on = True

while is_on:
    choice = input(f"What would you like? ({items_menu.get_items()}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        confirm_choice = items_menu.find_drink(choice)
        if confirm_choice:
            if coffee_machine.is_resource_sufficient(confirm_choice):
                cost = confirm_choice.cost
                print(f"The cost is {cost}.")
                payment = money_machine.make_payment(cost)
                if payment:
                    coffee_machine.make_coffee(confirm_choice)
