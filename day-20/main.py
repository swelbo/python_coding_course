# Snake game
import time
from turtle import Screen
from snake import Snake

# screen setup
scr = Screen()
scr.setup(height = 600, width = 600)
scr.bgcolor("pink")
scr.title("Snakey McSnakeName")
scr.tracer(0)

snake = Snake()

scr.listen()
scr.onkey(snake.up,"Up")
scr.onkey(snake.down,"Down")
scr.onkey(snake.left,"Left")
scr.onkey(snake.right,"Right")

game_on = True
while game_on:
    scr.update()
    time.sleep(0.01)
    snake.move()

# its over baby 
scr.exitonclick()