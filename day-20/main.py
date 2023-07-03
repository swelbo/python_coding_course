# Snake game

from turtle import Turtle, Screen

# screen setup
scr = Screen()
scr.setup(height = 600, width = 600)
scr.bgcolor("black")
scr.title("Snakey McSnakeName")

snake_length = 3
the_snake = []
dis = 0
for i in range(0, snake_length):
    t = Turtle()
    t.shape("square")
    t.turtlesize(0.5,0.5, 1)
    t.goto(0 + dis, 20)
    t.color("white")
    the_snake.append(t)
    dis += 10

# its over baby 
scr.exitonclick()