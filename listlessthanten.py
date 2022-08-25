# List Less Than Ten
# https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

print("Think of a number between 1 and 100")
number = int(input("What is the number? "))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

x = []

for i in a:
  if i < number:
  	x.append(i)

final_var = (", ".join(map(str, x)))

print(f"In our list: {final_var} are all lower than your number")