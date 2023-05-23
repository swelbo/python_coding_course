from turtle import Turtle, Screen
import random

is_race_running = False
screen = Screen()
screen.setup(height = 500, width = 400)
user_bet = screen.textinput(title="Which turtle?", prompt= "Which turtle will win the race? Enter a colour: ")
screen.listen()

cols = ["red", "orange", "yellow", "green", "blue"]
starting_positions = [-100, -50, 0, 50, 100]

# create list of turtles with different colours and different starting loactions
list_of_turtles = []
position = 0
for i in range(0,5):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(cols[i])
    new_turtle.penup()
    new_turtle.goto(x=-240, y = starting_positions[i])
    list_of_turtles.append(new_turtle)
    position 


# race the little turtles
if user_bet:
    is_race_running = True

# game loop
while is_race_running:

    for turtle in list_of_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        
        if turtle.xcor() > 240:
            is_race_running = False

            # select the winner 
            winner = turtle.pencolor()
            
            if winner == user_bet:
                print(f"You win! {winner.title()} won!")
            else:
                print(f"You lose! {winner.title()} won!")


screen.exitonclick()