#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# libraries
import random as rd
from art import logo5
import replit

#function to check winner
def check_winner(guess, random_number, attempts):
    ''' Function that checks whether number is correct and returns attempts '''
    if guess > random_number:
        print("Nope! Too high!")
        return attempts - 1

    elif guess < random_number:
        print("Nope! Too low!")
        return attempts - 1

    else: 
        print(f"Correct! The answer was {random_number}")
        print(f"You completed the game with {attempts - 1} attempts remaining!")

def set_diff():
    ''' Function that sets level difficulty'''
    mode = input("  Please select a mode - easy/hard? - ").lower()

    if mode == "easy":
        attempts = 10
    elif mode == "hard":
        attempts = 5

    return attempts

# welcome message
def game():
    ''' The game '''
    print("Welcome to the number guessing game!")

    # input variables
    random_number = rd.randint(0,100)

    play_again = "y"
    while play_again == "y":
        
        attempts = set_diff()

        # The game 
        guess = 0
        while guess != random_number:
            guess = int(input("  Guess a number between 0-100 - "))
            attempts = check_winner(guess, random_number, attempts)
            
            if attempts != None:
                print(f"You have {attempts} remaining")
        
        if attempts == 0:
            print("Oh no you ran out of attempts")
        
        play_again = input("Would you like to play again - y/n? ")

        if play_again == "n":
            print("Goodbye.")
    return

# run game
game()
