from turtle import Turtle
import random
COLOR = "white"
SHAPE = "square"


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape(SHAPE)
        self.color(COLOR)
        self.goto(position)
        self.my_var = 10
        self.ball_speed = 0.1
        self.direction = [random.random(), 1]

    def move(self):
        new_x = self.xcor() + self.direction[0] * 10
        new_y = self.ycor() + self.direction[1] * 10
        self.goto(new_x, new_y)

    def vertical_bounce(self):
        self.direction[1] *= -1

    def horizontal_bounce(self):
        self.direction[0] *= -1
        self.ball_speed *= 0.9

    def reset_state(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.direction[0] = random.random()
        self.horizontal_bounce()
