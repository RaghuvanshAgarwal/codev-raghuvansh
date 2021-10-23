from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.penup()
        self.color("blue")
        self.speed("fastest")

    def detect_collision(self, snake):
        return self.distance(snake.head) < 15
