from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def mov_forward():
    tim.forward(10)

def mov_backward():
    tim.backward(10)

def counter_clockwise():
    tim.left(10)

def clockwise():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
screen.listen()
screen.onkey(key='w', fun=mov_forward)
screen.onkey(key='s', fun=mov_backward)
screen.onkey(key='a', fun=counter_clockwise)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='c', fun=clear)

screen.exitonclick()