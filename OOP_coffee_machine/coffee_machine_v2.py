from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from replit import clear

# create object from class Menu
menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()

machine = "on"
while machine == "on":
    # get users selection 
    user_input = input(f"What coffee do you want ({menu.get_items()})? ")
    selection = menu.find_drink(user_input)
    
    if user_input == "off":
        print("Powering down")
        machine = "off"
    elif user_input == "report":
        maker.report()
        money.report()
    elif selection == None:
        print("Please make another selection")
    else:
            # check that the selection exists and add to variable
            # print selection
        print(f"You have selected a {selection.name.title()}")

        # check the resources 
        enough_resources = maker.is_resource_sufficient(drink=selection)

        if enough_resources == True:
            enough_money = money.make_payment(selection.cost)
            if enough_money == False:
                print("Not enough money")
            else:
                maker.make_coffee(order=selection)
        else:
            print("Please refill the machine or make another selection")

    if selection == "off":
        machine = "off"


