# import libraries
from replit import clear
from art import logo2
import time

'''# print art
print(logo2)'''

# The dictionary of bidder
dictionary_of_bidders = {}
bools = True
while bools == True:

    # print art
    print(logo2)

    # Name input 
    name = input("what is your name? ")

    # bid 
    bid = input("What is your bid? ")

    # any more bidders? 
    next_bidder = input("Are there any more bidders y/n? ")

    # add name and bid into the dictionary
    dictionary_of_bidders[name] = bid
    
    # loop through the game until there are no more bidders
    if next_bidder == "y":
        bools = True
    else:
        bools = False

    # clear screen for secrecy
    clear()

# cycle through the dictionary replacing the winner with the highest bidder
winner = ()

highest_bid = 0
for i in dictionary_of_bidders:
    bid = int(dictionary_of_bidders[i])
    if bid > highest_bid:
        highest_bid = bid
        winner = i
    
print(f"And the winner is . {time.sleep(0.1)} . {time.sleep(0.11)} . {time.sleep(0.1)} {winner}! ")


