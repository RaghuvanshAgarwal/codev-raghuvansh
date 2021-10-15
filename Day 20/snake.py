from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.initialize_snake_body()
        self.head = self.segments[0]
        self.head.color("red")

    def initialize_snake_body(self):
        for position in STARTING_POSITIONS:
            segment = Turtle(shape="square")
            segment.penup()
            segment.color("white")
            segment.goto(position)
            self.segments.append(segment)

    def add_segment(self):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(self.segments[-1].position())
        self.segments.append(segment)

    def move(self):
        for segment_index in range(len(self.segments) - 1, 0, -1):
            self.segments[segment_index].goto(self.segments[segment_index - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

