from coffee_machine_data import MENU, resources
from time import sleep

# data and globals
data = MENU
coin = {"dollar":1.0, "quarter":0.25, "dime":0.10, "nickle":0.05, "pennies":0.01}
starting_stock = resources
current_stock = {"ingredients":{"water":300, "milk":200, "coffee":100}, "cost":0}

# Get the users secletion 
def get_selection():
    '''Users coffee selection'''
    selection = input("What do you want, espresso, latte or cappuccino? ")
    return selection

# check stock to see if there is enough stock based on the selection 
def sufficient_resources_check():
    '''Check machine stock'''
    for item in selection_resources["ingredients"]:
        if selection_resources["ingredients"][item] <= current_stock["ingredients"][item]:
            print(f"{item.title()} is in topped up, you're all good")
        else:
            print(f"Argh, no {item} in stock, here is your refund")
            break

def money_handling():
    '''Money handling'''
    inserted_money = 0
    while inserted_money < selection_resources['cost']:
        coin_input = input(f"You selected {selection_name}, please insert ${selection_resources['cost']} - please use: {', '.join(list(coin.keys()))} ")
        # TODO inser mechanism that allows user to input more than one coin
        inserted_money += coin[coin_input]
        print(f"You have inserted ${inserted_money}")
        if inserted_money <= selection_resources['cost']:
            print(f"You have ${selection_resources['cost'] - inserted_money} left to pay")

    print("You have inserted enough money!")
    current_stock["cost"] += inserted_money

    if inserted_money > selection_resources['cost']:
        change =  inserted_money - selection_resources['cost']
        print(f"Here is your change : ${round(change, 2)}")
        current_stock["cost"] -= change

def make_the_coffee():
    '''Make the coffee and deduct from resources'''
    print(f"Hold up, we are crafting your {selection_name.title()}")
    sleep(1)
    
    for item in selection_resources["ingredients"]:
        current_stock["ingredients"][item] = current_stock["ingredients"][item] - selection_resources["ingredients"][item]

    print(f"Here is you {selection_name.title()}. Enjoy!")

# step 1
selection_name = get_selection()
if selection_name == "off":
    print("Powering down")
elif selection_name == "report":
    print(current_stock)
else:
    # step 2
    selection_resources = data[selection_name]
    sufficient_resources_check()
    # step 3 
    money_handling()
    # step 4
    make_the_coffee()