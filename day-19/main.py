from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(20)

def move_backwards():
    timmy.backward(20)

def turn_clock():
    timmy.right(10)

def turn_anti():
    timmy.left(10)

def clear():
    timmy.reset()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_anti)
screen.onkey(key="d", fun=turn_clock)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
