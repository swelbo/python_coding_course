# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
### NESTED if statment!!!! 

if year % 4 == 0:
    if year != 0:
        print(f"{year} was a Leap year!")
    elif year % 400 == 0:
        print(f"{year} was a Leap year!")
else: 
    print(f"{year} was not a Leap year!")