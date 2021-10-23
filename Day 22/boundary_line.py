from turtle import Turtle


class BoundaryLine(Turtle):
    def __init__(self,position):
        super().__init__()
        self.hideturtle()
        self.pensize(5)
        self.penup()
        self.color("white")
        self.goto(position)
        self.setheading(90)
        for _ in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
