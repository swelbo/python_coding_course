# Rock paper scissors
#https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

import time 

# welcome staatement
print("Welcome to the rock paper scissors game!")
x = input("Have you played before? ")

if x == "yes" and "Yes" and "Yeah" and "yeah": 
	print("Great! Let's begin")
else:
	print("OK, here are the rules! The Rules: ")

print("OK, great! Let's get ready to begin")

# countdown to the start of game
countdown = 5

while countdown > 0:
	print(countdown)
	countdown -= 1
	time.sleep(1)

# playr 1 
u1 = input("Player one, you're up! Rock, Paper or Scissors? ")

# plaayer 2
u2 = input("Player two, your turn! Rock, Paper or Scissors? ")

# sleeep
print("Hmm, intresting...")
time.sleep(3)

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
