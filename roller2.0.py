# input for the roller coaster 
height = int(input("How tall in cm? "))
bill = 0 

# if/else statement 
if height >= 100:
    print("Great, you can ride :)")
    age = int(input("Age? "))
    if age <= 12:
        bill = 5 # Kidsticket price is $5
    else:
        bill = 10 # aadult ticket price is $10
    
    wants_photo = input("Would you like a photo? Type Y or N ")
    if wants_photo == "Y":
        # add three dollars to the bill for photo
        bill += 3
    print(f"Your total bill is {bill}")
# else if height is too low
else:
    print("Sorry")

