# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Import modules
import random

# random number
number = random.randint(0,len(names)-1)

# print output
print(f"{names[number]} is paying the bill")

# shorter version using the choice method
print(f"{random.choice(names)} is paying up")