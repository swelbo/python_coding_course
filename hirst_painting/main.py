import colorgram
import turtle
turtle.colormode(255)
import random

# import colours 
colors = colorgram.extract("/Users/tom/python_coding_course/hirst_painting/hirst_dots.jpg", 20)

# generate a tuple of tuuuuples
cols = []
for i in range(0, len(colors)):
    cols.append(tuple(colors[i].rgb))
print(cols)

# create timmy! 
timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.penup()
timmy.hideturtle()
# set position

# Create a dot function with a random colour
def row_of_dots():
    for i in range(0,10):
        timmy.speed("fastest")
        timmy.color(random.choice(cols))
        timmy.dot(20)
        timmy.forward(60)

def main():
    for i in range(-300,300, 50):
        timmy.penup()
        timmy.setposition(-300,i)
        
        row_of_dots()

main()   

# click to close
screen = turtle.Screen()
# turtle.screensize(canvwidth=50, canvheight=50, bg="yellow")

# close
screen.exitonclick()