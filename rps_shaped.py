rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

#
import random as rd
import time

# User input
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.?\n"))
computer = rd.randint(0,2)

# game images list
game_images = [rock, paper, scissors]

# check the entry is between 0-2
# change at somepoint to try/except
if user >= 3 or -0:
    print("Invalid entry, please try again")
else:

    # computer image 
    print("The computer chose:")
    print(game_images[user])

    # sleep for suspense
    time.sleep(1)
    
    # user image
    print("you chose:")
    print(game_images[computer])

    # result 
    time.sleep(1)
    if user == computer:
        print("Ah, it is a tie")
    elif user == 1 and computer == 0:
        print("Nice! You win :)")
    elif user == 0 and computer == 2:
        print("Nice! You win :)")
    elif user == 2 and computer == 1:
        print("Nice! You win :)")
    else:
        print("Ah, shucks. The computer wins this time")