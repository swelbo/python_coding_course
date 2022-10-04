# 🚨 Don't change the code below 👇

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# calculate the top score in the class - i.e. print(max(student_scores)) and print(min(student_scores))
#print(student_scores[0])
#print(student_scores[-1])
'''
x=0
for i in student_scores:
    x += 1
print(x)
'''

# Need to loop over each of the numbers in a list [1, 2, 3] to see if they are smaller or larger than other items in the list

# for loop to ID highest number
highest_score = 0
for scores in student_scores:
    if scores > highest_score:
        highest_score = scores # x is replaced with scores only if it is higher than x 
print(f"The highest score is {highest_score}")