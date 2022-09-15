# Rock paper scissors - one player against the computer
# Introduces time and random
# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

import time
import random
from enum import IntEnum

# welcome staatement
print("Welcome to the rock paper scissors game!")
x = input("Have you played before? ")

if x == "yes" and "Yes" and "Yeah" and "yeah": 
	print("Great! Let's see your worth!")
else:
	print("OK, here are the rules! \n\nThe Rules: \nYou must defend your honour by selecting either Rock, Paper or Scissors as your weapon!")

time.sleep(1)

print("Let's get ready to play in:")

# countdown to the start of game
countdown = 3

# a while loop that counts down from countdown every 0.5 seconds
while countdown > 0:
	print(countdown)
	countdown -= 1
	time.sleep(0.5)

# define actions in a class. This class allows us to add or remove samples. 
class Action(IntEnum): # Action here could be anything.  
    Rock = 0 
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4

# this is a dictionary - it contains the selection variable plus two variables that are linked to the 
# selection variable - in this case it is the the two variables that defeat the input variable 
# dictionary that outlines the victories (values) given a certain choice (key)  
# rember a dictionary consists of key  followed by :  followed by value (key:value
victories = {
    Action.Scissors: [Action.Lizard, Action.Paper],
    Action.Paper: [Action.Spock, Action.Rock],
    Action.Rock: [Action.Lizard, Action.Scissors],
    Action.Lizard: [Action.Spock, Action.Paper],
    Action.Spock: [Action.Scissors, Action.Rock]
}
# this function gets the users selection. It first asks for choices. Choices can be added or removed by editing the
# class Action 
def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action] # editdable choices linked to action
    choices_str = ", ".join(choices) # removed square brackets (maybe does something else)
    selection = int(input(f"Enter a choice ({choices_str}): ")) # user selection that neatly uses choices
    action = Action(selection)
    return action


# function to generate the computers selection
def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action

''' old
# function to determine the winner
def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            print("Rock smashes Scissors! You win!")
        else:
            print("Paper covers Rock! You lose.")
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            print("Paper covers Rock! You win!")
        else:
            print("Scissors cuts Paper! You lose.")
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            print("Scissors cuts Paper! You win!")
        else:
            print("Rock smashes Scissors! You lose.")

'''

def determine_winner(user_action, computer_action):
    defeats = victories[user_action]
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif computer_action in defeats:
        print(f"{user_action.name} beats {computer_action.name}! You win!")
    else:
        print(f"{computer_action.name} beats {user_action.name}! You lose.")



# The while loop is the brining all the functions together
# inside the for loop is an exception statement that ensures the user only chooses 0-2 as their options
# it runs get_user_selection, if that fails due to user error it prints and asks again
# It then gets the computer action using get_computer_selection()
# it detrmines winner using the outcome of the two input functions. 
# then asks if we want to play again :)
while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print("Thank you for playing :)")
        break