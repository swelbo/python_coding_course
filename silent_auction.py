# import libraries
from replit import clear
from art import logo2
import time

def find_highest_biddder(bidding_record):
    winner = ""
    highest_bid = 0
    for bidder in dictionary_of_bidders:
        bid = int(dictionary_of_bidders[bidder])
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder
    return winner

# The dictionary of bidder
dictionary_of_bidders = {}

# while loop
bidding_finished = False
while not bidding_finished:
    # print art
    print(logo2)
    # Name input 
    name = input("what is your name? ")
    # bid 
    bid = int(input("What is your bid? $"))
    # any more bidders? 
    next_bidder = input("Are there any more bidders y/n? ")
    # add name and bid into the dictionary
    dictionary_of_bidders[name] = bid
    # loop through the game until there are no more bidders
    if next_bidder == "n":
        bidding_finished = True
        winner = find_highest_biddder(dictionary_of_bidders)
    else:
        bidding_finished = False
    # clear screen for secrecy
    clear()

# cycle through the dictionary replacing the winner with the highest bidder\
print("And the winner is . . .") 
time.sleep(0.5)
print(winner.title())
print(f"Congratulations, {winner.title()}")