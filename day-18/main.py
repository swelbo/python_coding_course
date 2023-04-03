from turtle import Turtle, Screen

# turtle object
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

# draw square
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# dashed line
# for i in range(15):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)

# Crazy pattern
j = 3
for i in range(7):
    angle = 360/j
    for i in range(j):
        timmy.forward(100)
        timmy.right(angle)
    j += 1

# for i in range(5):
#     timmy.forward(100)
#     timmy.right(72)

# screen object 
screen = Screen()
screen.exitonclick()