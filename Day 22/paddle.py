from turtle import Turtle

WIDTH = 20
HEIGHT = 100
SPEED = 20
COLOR = "white"
SHAPE = "square"
SCREEN_HEIGHT = 600


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape(SHAPE)
        self.setheading(90)
        self.color(COLOR)
        self.penup()
        self.shapesize(stretch_wid=WIDTH / 20, stretch_len=HEIGHT / 20)
        self.goto(x_pos, y_pos)

    def move_up(self):
        if self.ycor() < (SCREEN_HEIGHT - HEIGHT)/2:
            self.forward(SPEED)

    def move_down(self):
        if self.ycor() > -(SCREEN_HEIGHT - HEIGHT) / 2:
            self.backward(SPEED)
