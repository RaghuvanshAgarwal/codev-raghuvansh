from turtle import Turtle


class TurtlePlayer:
    def __init__(self, color):
        self.player = Turtle()
        self.player.color(color)
        self.player.shape("turtle")
        self.player.shapesize(3)
        self.player.penup()

    def move(self, direction, speed):
        if direction == 0:
            self.player.forward(speed)
        elif direction == 1:
            self.player.backward(speed)
        elif direction == 2:
            self.player.right(90)
            self.player.forward(speed)
        else:
            self.player.left(90)
            self.player.forward(speed)

    def go_to(self, x, y):
        self.player.goto(x, y)

    def get_player_x(self):
        return self.player.xcor()

    def get_player_y(self):
        return self.player.ycor()

    def get_player_color(self):
        return self.player.color()[0]
