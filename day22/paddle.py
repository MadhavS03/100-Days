from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.penup()
        self.goto(x, y)

    def up(self):
            y = self.ycor() + 20
            self.goto(self.xcor(), y)

    def down(self):
            n_y = self.ycor() - 20
            self.goto(self.xcor(), n_y)

