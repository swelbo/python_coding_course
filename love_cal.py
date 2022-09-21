# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Function that lowers case and counts number of a given letter
def count(name, letter):
    x = name.lower()
    x = x.count(letter)
    return(x)

# combine names
names = name1+name2

# Loop through True 
trulst=[]
for i in "true":
    x = count(names, i)
    trulst.append(x)

# sum the list
tru = sum(trulst)

luvlst=[]
for i in "love":
    x = count(names, i)
    luvlst.append(x)

# sum the list
luv = sum(luvlst)

# concatenate the two numbers together
result = int(str(tru)  + str(luv))
 
# print Athe final result 
if result <= 10 or result >= 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result >= 40 and result <= 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}")