from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? enter color: ")
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
pos = [-50, -20, 10, 40, 70, 100]
turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=pos[i])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = Turtle

while is_race_on:
    for t in turtles:
        if t.xcor() > 230:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"You won, {winning_color} turtle won. ")
            else:
                print(f"You lost, {winning_color} turtle won. ")


        speed = random.randint(0, 10)
        t.forward(speed)



screen.exitonclick()