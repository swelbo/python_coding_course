#### calculator.py

from art import logo3

# logo
print(logo3)

# addition 
def add(n1, n2):
    return n1 + n2

# subtraction
def subtract(n1, n2):
    return n1 - n2

# multiply
def mutiply(n1, n2):
    return n1 * n2

# divide
def divide(n1, n2):
    return n1 / n2  

operations = {
    "+":add, 
    "-":subtract, 
    "*":mutiply, 
    "/":divide
}

# ask for first number
num1 = float(input("What is the first number? "))

# for loop to print out all the operations
for symbol in operations:
    print(symbol)

continue_calculation = True
while continue_calculation:
    operation_symbol = input("Pick and operation ")
    num2 = float(input("What is the next number? "))
     
    answer = operations[operation_symbol](n1=num1, n2=num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    continue_calculation = input(f"Type y to continue calculating with {answer} or type n to exit ")

    if continue_calculation == "y":
        num1 = answer
    else:
        continue_calculation = False
    




