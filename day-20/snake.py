# snake class
from turtle import Turtle

START_POSITION = [(0,0), (-20,0), (-40,0)]

class Snake:

    def __init__(self, length = 5):

        self.snake_length = length
        self.the_snake = []
        self.dis = 0
        self.create_snake()
        
    def create_snake(self):
        for _ in range(0, self.snake_length):
            t = Turtle()
            t.shape("square")
            t.turtlesize(0.5,0.5, 1)
            t.goto(0 + self.dis, 20)
            t.penup()
            t.color("white")
            self.the_snake.append(t)
            self.dis -= 10

    def move(self):
        for seg_num in range(len(self.the_snake) - 1, 0, -1):
            new_x = self.the_snake[seg_num - 1].xcor()
            new_y = self.the_snake[seg_num - 1].ycor()
            self.the_snake[seg_num].goto(new_x, new_y)
        
        self.the_snake[0].forward(10)
