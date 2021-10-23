from turtle import Turtle, Screen, colormode
import random

directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return r, g, b


canvas = Screen()
canvas.screensize(5000, 5000)
paint_brush = Turtle()
paint_brush.shape("arrow")
paint_brush.pensize(10)
paint_brush.speed("fastest")
paint_brush.penup()
paint_brush.goto(-200, 0)
paint_brush.pendown()
colormode(255)
for _ in range(500):
    paint_brush.color(random_color())
    paint_brush.forward(25)
    paint_brush.right(random.choice(directions))

canvas.exitonclick()
