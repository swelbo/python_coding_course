#Write your code below this line 👇

# prime number has only two factors. Is only divisible by 1 and itself
# % gives you the remainder after you have divided by n.
# a non prime number would have 0 reamining 
# if you divide the number by anything other than one or itself, you will get a remainder that is not zero.

def prime_checker(number):
    bol = True
    for i in range(2, number):  
        if number % i == 0: # as you loop through the range there will occasions where i != 0, however never switch bol back to False so it is fine. 
            bol = False
    
    if bol:
        print(f"{number}, is prime number")
    else:
        print(f"{number}, is not a prime number")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)