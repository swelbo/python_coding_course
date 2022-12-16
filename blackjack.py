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

# import libraries
import random 
import art
import replit 

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

# define a draw cards function
def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_index = random.randint(0,12)
    return cards[card_index]

def sum_scores(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0 
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_scores(users_score, cpu_score):
    if users_score == cpu_score:
        print("It is a draw")
    elif cpu_score == 0:
        print("You lose! Computer had a blackjack!")
    elif cpu_score > 21:
        print("Computer went bust, you win! ")
    elif users_score == 0:
        print("You got a blackjack! You win!")
    elif users_score > cpu_score:
        print("You win!")
    else: 
        print("Computer wins!")

def main():
    # print the logo
    #print(art.logo4)
    # generate a random card for each player
    users_cards = []
    users_cards.append(draw_card())

    cpu_cards = []
    cpu_cards.append(draw_card())

    # Get the computers cards
    cpu_score = 0
    while cpu_score < 18:
        cpu_cards.append(draw_card())
        cpu_score = sum_scores(cpu_cards)

    users_score = 0
    draw_again = True
    while draw_again: 
        users_cards.append(draw_card())
        users_score = sum_scores(users_cards)
        
        print(f"Your cards are {users_cards}, your total score is {users_score}")
        print(f"Computer's first card is [{cpu_cards[0]}]")
        
        if sum(users_cards) <= 21:
            x = input("Draw again? ")
            if x == "y":
                draw_again = True
            else:
                draw_again = False

                compare_scores(users_score, cpu_score)

                print(f" - Your final hand was {users_cards} and the computers was {cpu_cards}")
                print(f" - Your score was {users_score} and the computers was {cpu_score}")

        else:
            draw_again = False
            print(f"You went bust! Computer wins with a hand of {cpu_cards[0:2]} and a score of {sum(cpu_cards[0:2])}")

play_again = True
while play_again:
    main()
    if input("Play again? ") == "y":
        replit.clear()
        play_again = True
    else:
        print("No problem! Here are your game stats: The computer won X times, and you won X times. That is a win percentage of X ")
        play_again = False