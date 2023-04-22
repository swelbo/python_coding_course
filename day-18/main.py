from turtle import Turtle, Screen, colormode
colormode(255)
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

def generate_colours():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

# cols = ["chocolate", "lime", "red", "black", "orange", "blue", "gold", "medium violet red", "yellow green", "dark cyan"]

# #### random walk 
# def random_walk(distance):
#     timmy.pensize(5)
#     timmy.speed(50)
#     timmy.color(generate_colours())
#     # movement = random.randint(10,50)
#     # angles = [90, 180, 270, 360]
#     angles = range(0,360)
#     heading = random.choice(angles)
#     timmy.setheading(heading)
#     timmy.hideturtle()
#     timmy.forward(distance)

# for i in range(300):
#     random_walk(5)


# timmy.color(generate_colours())
# timmy.circle(100)

x = ((-200,200), (200,200), (200, -200), (-200, -200), (0,0))
for i in x:
    timmy.penup()
    timmy.setposition(i)
    timmy.pendown()
    for i in range(0,360,1):
        timmy.speed("fastest")
        timmy.color(generate_colours())
        timmy.circle(100)
        timmy.setheading(i)



# ### circle spirograph 
# def spiro(distance):
#     timmy.speed("fastest")
#     timmy.color(generate_colours())
#     # movement = random.randint(10,50)
#     # angles = [90, 180, 270, 360]
#     angles = range(0,360)
#     heading = random.choice(angles)
#     timmy.setheading(heading)
#     timmy.hideturtle()
#     timmy.forward(distance)

# for i in range(300):
#     spiro(5)

# screen object 
screen = Screen()
screen.exitonclick()
