from turtle import Turtle

MOVE_DISTANCE = 20


class Player(Turtle):

    def __init__(self, starting_position):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(starting_position)
        self.setheading(90)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)
