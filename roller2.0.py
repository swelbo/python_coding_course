# loada modules
import time

# input for the roller coaster 
def input_height():
    i = int(input("Hey how tall are you in cm (i.e. 156)? "))
    print("Thanks for your input")
    return(i)

# sssk for heigh using function
height = input_height()

# pause program lodaing effect
print("Thinking...")
time.sleep(1)

#height = int(input("How tall in cm? "))
bill = 0 

# if/else statement 
if height >= 100:
    time.sleep(1)
    print("Awesome, you can ride :)")
    age = int(input("Age? "))
    if age >= 45 and age <= 55: # free for people between 45 and 55(and logical operator)
        bill =  0
        time.sleep(1)
        print("Nice, you ride for free! Hang in there :)")
    elif age <= 12:
        bill = 5 # Kidsticket price is $5
    else:
        bill = 10 # adult ticket price is $10
    
    wants_photo = input("Would you like a photo? Type Y or N ")
    if wants_photo == "Y":
        # add three dollars to the bill for photo
        bill += 3
    print(f"Cool, your total bill is {bill}")
# else if height is too low
else:
    print("Sorry")