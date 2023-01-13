# Higher lower game 

# modules
import random as rd
import replit as rp
from art import logo6, logo7
from hilo_game_data import data

# create a while loop so that the user can choose to play again 
# create a while loop that only breaks if the player looses 
# first vs second people selected at random make sure the second isnt the same
# if the player gets it correctly then loop

def select_random_person(data):
    random_int1 = rd.randint(0, len(data)-1)
    return data[random_int1]

def person_info(person):
    print(f"{person['name']}")
    print(f"{person['description']}")
    print(f"{person['country']}")

# Print the two randomly selected people
def print_higher_lower(first_person, second_person):
    '''Print the two randomly selected people'''
    print("Who has more followers? ")
    person_info(first_person)
    print("")
    print("VS")
    print("")
    person_info(second_person)

# check winner 
def get_winner(first_person, second_person):
    if first_person['follower_count'] > second_person['follower_count']:
        winner = first_person
    else:
        winner = second_person
    return winner

def users_guess():
    guess = input("Who is higher? A or B ").lower()
    
    if guess == "a":
        guess = first_person
    elif guess == "b":
        guess = second_person
    return guess

keep_playing = "y"
while keep_playing == "y":
    # Get the first two people
    first_person = select_random_person(data)

    roll_over = True
    while roll_over == True:
        second_person = select_random_person(data)

        # While loop to make sure we haven't selected the two same people
        while first_person == second_person:
            second_person = select_random_person(data)

        # check who is the winner of the two
        winner = get_winner(first_person, second_person)

        print(winner["name"])

        # Print to the user who has been selected 
        print_higher_lower(first_person, second_person)

        # Ask the user who is higher
        guess = users_guess()

        # Print the winner 
        if guess["name"] == "Instagram":
            print("you reached the highest count in the db, well done")
            roll_over = False
        elif guess == winner:
            print("Well done! ")
            first_person = winner
        else:
            print("You lose")
            roll_over = False

    keep_playing = input("play again y/n? ").lower()

print("Cool, cya!")
