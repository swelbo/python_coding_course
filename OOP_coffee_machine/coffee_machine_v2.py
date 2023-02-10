from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine = "on"
while machine == "on":
    # get users selection 
    options = menu.get_items()
    user_input = input(f"What coffee do you want {options}? ")
    selection = menu.find_drink(user_input)
    
    if user_input == "off":
        print("Powering down")
        machine = "off"
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif selection == None:
        print("Please make another selection")
    else:
        print(f"You have selected a {selection.name.title()}")
        enough_resources = coffee_maker.is_resource_sufficient(drink=selection)
        if enough_resources == True:
            enough_money = money_machine.make_payment(selection.cost)
            if enough_money == False:
                print("Not enough money")
            else:
                coffee_maker.make_coffee(order=selection)
        else:
            print("Please refill the machine or make another selection")