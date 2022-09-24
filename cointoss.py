import random as rd

user = input("Heads or Tails?\n").lower()
toss = rd.randint(0,1)

if toss == 1:
    toss = "tails"
else:
    toss = "heads"

if user == toss:
    print("you nailed it!")
else:
    print("too bad")

    