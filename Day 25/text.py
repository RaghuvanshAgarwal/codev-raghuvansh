from turtle import Turtle


class Text(Turtle):
    def __init__(self, position, text):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.write(text, align="center", font=("roboto", 10, "bold"))
