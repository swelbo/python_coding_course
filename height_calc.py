# 🚨 Don't change the code below 👇
from re import S


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆
#Write your code below this row 👇

# add together the total student heights - i.e. print(len(student_heights))
x = 0
for i in student_heights:
    x += i
print(f"The sum of all heights is {x}")

# divide by the total number of students - i.e. print(sum(student_heights))
y = 0
for i in student_heights:
    y += 1
print(f"There are {y} students")

#the result rounded
answer = round(x/y)

print(f"The average height of the students is {answer}")
