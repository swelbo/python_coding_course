# Snake game
import time
from turtle import Turtle, Screen

# screen setup
scr = Screen()
scr.setup(height = 600, width = 600)
scr.bgcolor("black")
scr.title("Snakey McSnakeName")
scr.tracer(0)

snake_length = 3
the_snake = []
dis = 0
for i in range(0, snake_length):
    t = Turtle()
    t.shape("square")
    t.turtlesize(0.5,0.5, 1)
    t.goto(0 + dis, 20)
    t.penup()
    t.color("white")
    the_snake.append(t)
    dis -= 10



game_on = True
while game_on:
    scr.update()
    time.sleep(0.1)

    for seg_num in range(len(the_snake) - 1, 0, -1):
        new_x = the_snake[seg_num - 1].xcor()
        new_y = the_snake[seg_num - 1].ycor()
        the_snake[seg_num].goto(new_x, new_y)

    the_snake[0].forward(10)
    the_snake[0].left(90)


# its over baby 
scr.exitonclick()