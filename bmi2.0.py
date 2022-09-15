# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / (height** 2), 1)
print(f"Your BMI score is {bmi}")

if bmi <= 18.5:
  print("You are underweight")
elif bmi <= 25:
  print("You are normal weight")
elif bmi <= 30:
  print("You are slightly overweight")
elif bmi <= 35:
  print("You obese baby!")
else:
  print("Oh my, you are clinically obese")