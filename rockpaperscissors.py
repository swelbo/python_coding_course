# Rock paper scissors - one player against the computer
# Introduces time and random
# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

import time
import random

# welcome staatement
print("Welcome to the rock paper scissors game!")
x = input("Have you played before? ")

if x == "yes" and "Yes" and "Yeah" and "yeah": 
	print("Great! Let's begin")
else:
	print("OK, here are the rules! \nThe Rules: \nYou must defend your honour by selecting either Rock, Paper or Scissors  asss your weapon!")

time.sleep(2)

print("OK, great! Let's get ready to begin")

# countdown to the start of game
countdown = 5

while countdown > 0:
	print(countdown)
	countdown -= 1
	time.sleep(1)

# loop over the game
while True:

# players choice
    user_action = input("Player one, you're up! Rock, Paper or Scissors? ")

    # computers choice - uses random on a list of options. In this case its: rock paper scissors
    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(possible_actions)

    # pause for effect
    print("Hmm, intresting...")
    time.sleep(3)

    # output user
    print(f"The computer has chosen {computer_action} ... and you chose {user_action}!")

    # compaare outputs - not using if elif else block
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "Rock":
        if computer_action == "Scissors":
            print("Rock smashes Scissors! You win!")
        else:
            print("Paper covers Rock! You lose.")
    elif user_action == "Paper":
        if computer_action == "Rock":
            print("Paper covers Rock! You win!")
        else:
            print("Scissors cuts Paper! You lose.")
    elif user_action == "Scissors":
        if computer_action == "Paper":
            print("Scissors cuts Paper! You win!")
        else:
            print("Rock smashes Scissors! You lose.")

    play_again = input("Would you like another game? (y/n)")
    if play_again != "y":
        break



''' # This is the practice python method.
def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(u1, u2))
'''