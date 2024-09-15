# import colorgram
#
# rgb_color = []
# colors = colorgram.extract('img.jpg', 20)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colour = (r, g, b)
#     rgb_color.append(colour)
#
# print(rgb_color)

from turtle import Turtle, Screen
import turtle
import random
t = Turtle()
screen = Screen()
turtle.colormode(255)

colours = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111)]
y = 0

while y != 500:

    for i in range(10):
        dot_color = random.choice(colours)
        t.dot(20, dot_color)
        t.penup()
        t.forward(50)
    y += 50
    t.setx(0)
    t.sety(y)




screen.exitonclick()
