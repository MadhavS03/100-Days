import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

timmy.shape("turtle")

# for i in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# for i in range(3):
#     timmy.forward(100)
#     timmy.right(120)
#
# for i in range(4):
#     timmy.color('red')
#     timmy.forward(100)
#     timmy.right(90)
#
# for i in range(5):
#     timmy.color('blue')
#     timmy.forward(100)
#     timmy.right(72)
#
# for i in range(6):
#     timmy.color('green')
#     timmy.forward(100)
#     timmy.right(60)
#
# for i in range(7):
#     timmy.color('cyan')
#     timmy.forward(100)
#     timmy.right(51.42)
#
# for i in range(8):
#     timmy.color('pink')
#     timmy.forward(100)
#     timmy.right(45)
#
# for i in range(9):
#     timmy.color('purple')
#     timmy.forward(100)
#     timmy.right(40)
#
# for i in range(10):
#     timmy.color('yellow')
#     timmy.forward(100)
#     timmy.right(36)

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
# for shape_side_n in range(3, 10):
#     timmy.color(random.choice(colours))
#     draw_shape(shape_side_n)


turtle.colormode(255)
def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# direction = [90, 180, 270, 0]
timmy.speed('fastest')
# while True:
#     timmy.forward(30)
#     timmy.color(color())
#     timmy.setheading(random.choice(direction))


r = 100
for i in range(100):
    timmy.circle(r)
    timmy.color(color())
    timmy.left(3.6)

screen.exitonclick()
