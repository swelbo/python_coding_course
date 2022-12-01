############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# import libraries
import random 
import art

# print the logo
#print(art.logo4)

def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_index = random.randint(0,12)
    return cards[card_index]

# generate a random card for each player 
user_card_1 = draw_card()
user_card_2 = draw_card()

# generate starting cards for the computer
cpu_card_1 = draw_card()

# card scores - Ace, 2, 3 etc ... 
# assumption - cards come from this list - all have equal chance of occuring
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Dictionary of card names so we can display the names
# TODO nested dictionary NAME:{Value:Index}
card_dict = {
    "ace":11,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
    "ten":10,
    "jack":10,
    "queen":10,
    "king":10,
}

# Show cards 
print(f"Your cards are {user_card_1} and {user_card_2}")

# print score
user_score = user_card_1 + user_card_2

# show cards 
print(f"The computers first card is {cpu_card_1}")
cpu_score = cpu_card_1

# print scores
print(f"Your current score is {user_score}")
print(f"The computers current score is {cpu_score}")
#

draw_again = True
while user_score < 21:
    x = input("Would you like to draw another card (y/n)? ")
    if x == "y":
        new_card = draw_card()
        print(f"Your new card is {new_card}\n")
        user_score += new_card
        print(f"Your score is now {user_score}")
    elif x == "n":
        draw_again = False

if user_score > 21:
    print("bust")

# while CPU score is less than 18 keep drawing cards 
cpu_draw = True
while cpu_score < 19:
    new_card = draw_card()
    cpu_score += new_card

print(f"CPU total is {cpu_score}")

# print

# draw = True
# while draw:
#     x = input("Would you like to pick another card (y/n)? ")
#     if x == "n":
#         draw = False
#     else:
#         draw_card()
