# Fizzbuzz interview question
# If the number is divis by 3 print Fizz
# if the number is divisible by 5 print Buzz
# if the number is dividible by 3 and 5 print FizzBuzz

# need to print out the whole range by ammend the 3, 5 and 3 AND 5 divisss. 

for i in range(1,101):
    #if i % 3 != 0 and i % 5 != 0:
        #print(i)
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)