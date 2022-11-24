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

# ask to choose operation
operation_symbol = input("Pick an operation from the list above ")

# ask for second number 
num2 = float(input("What is the second number? "))

# calculate answer
answer = operations[operation_symbol](n1=num1, n2=num2)

# print to user 
print(f"{num1} {operation_symbol} {num2} = {answer}")




####
