# snake class
from turtle import Turtle

START_POSITION = [(0,0), (-20,0), (-40,0)]

class Snake:

    def __init__(self, length = 5):

        self.snake_length = length
        self.snake_segments = []
        self.dis = 0
        self.create_snake()
        self.head = self.snake_segments[0]
        
    def create_snake(self):
        for _ in range(0, self.snake_length):
            t = Turtle()
            t.shape("square")
            t.turtlesize(0.5,0.5, 1)
            t.penup()
            t.goto(0 + self.dis, 20)
            t.color("black")
            self.snake_segments.append(t)
            self.dis -= 10

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        
        self.head.forward(10)
    
    def up(self):
         self.head.setheading(90)
    def down(self):
        self.head.setheading(270)
    def left(self):
        self.head.setheading(180)
    def right(self):
        self.head.setheading(0)
