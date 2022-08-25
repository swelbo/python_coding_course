# introduction
print("Hey, welcome to the tip calculator.")
feedback = input("How was your meal, Good or Bad? ")

'''
feedback = input("How was your meal, Good or Bad? ")
while quit != "enter":
    quit = input('Type "enter" to quit:' )
'''

# ifelse for first question

if feedback == "Good":
	print("Amazing, i'm glad you had a nice meal")
else:
	print("Sorry to hear that!")

# total price of the bill
bill = float(input("How much was the bill? "))

# percentage tip 
per = float(input("What percentage would you like to tip? "))

# total tip
tip = (bill / 100) * per

# total bill + tip
total = round(bill + tip, 2)

#
test = f"The total of your bill with tip is £{total}"

print(test)

# number of people split input
share = int(input("How many people would you like to split the bill with? "))

# final split that everyone needs to pay
final_split = round(total/share, 2)

# final print statement
print(f"You each need to pay ${final_split}")

# goodbye
print("Have a great day")