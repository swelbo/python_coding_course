# Snake game
import time
from turtle import Screen
from snake import Snake

# screen setup
scr = Screen()
scr.setup(height = 600, width = 600)
scr.bgcolor("black")
scr.title("Snakey McSnakeName")
scr.tracer(0)

snake = Snake()

game_on = True
while game_on:
    scr.update()
    time.sleep(0.1)
    snake.move()

# its over baby 
scr.exitonclick()