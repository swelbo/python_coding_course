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

# User input
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.? "))
computer = rd.randint(0,2)


if user == 1 and computer == 0:
    print("its a tie")
elif user == 1 and computer == 0:
    print("user wins")
elif user == 0 and computer == 2:
    print("user wins")
elif user == 2 and computer == 1:
    print("user wins")
else:
    print("computer wins")