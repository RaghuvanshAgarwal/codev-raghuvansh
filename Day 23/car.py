import turtle
import random
from turtle import Turtle

MOVE_DISTANCE = 5


class Car(Turtle):
    def __init__(self, starting_position, callback):
        super().__init__()
        turtle.colormode(255)
        self.callback = callback
        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        self.penup()
        self.goto(starting_position)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)
        self.destroy_check()

    def is_collided_with_player(self, player):
        return abs(self.xcor() - player.xcor()) < 15 and abs(self.ycor() - player.ycor()) < 10

    def destroy_check(self):
        if self.xcor() < -320:
            self.callback(self)
