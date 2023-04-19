from turtle import Turtle, Screen
import random

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
# j = 3
# for i in range(7):
#     angle = 360/j
#     for _ in range(j):
#         timmy.forward(100)
#         timmy.right(angle)
#     j += 1

# def draw_shape(side):
#     angle = 360/side
#     for _ in range(side):
#         timmy.forward(100)
#         timmy.right(angle)

# cols = ["chocolate", "lime", "red", "black", "orange", "blue", "gold", "medium violet red", "yellow green", "dark cyan"]

# for i in range(3, 11):
#     timmy.color(random.choice(cols))
#     draw_shape(i)

# for i in range(5):
#     timmy.forward(100)
#     timmy.right(72)

cols = ["chocolate", "lime", "red", "black", "orange", "blue", "gold", "medium violet red", "yellow green", "dark cyan"]

def random_walk(distance):
    timmy.pensize(5)
    timmy.speed(10)
    timmy.color(random.choice(cols))
    # movement = random.randint(10,50)
    angles = [90, 180, 270, 360]
    heading = random.choice(angles)
    timmy.setheading(heading)
    timmy.hideturtle()
    timmy.forward(distance)

for i in range(200):
    random_walk(20)

# screen object 
screen = Screen()
screen.exitonclick()