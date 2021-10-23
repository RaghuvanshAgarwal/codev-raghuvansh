from turtle import Turtle, Screen, colormode
import random


def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return r, g, b


brush = Turtle()
canvas = Screen()
colormode(255)
brush.speed(0)
angle_step = 10
for _ in range(round(360 / angle_step)):
    brush.color(random_color())
    brush.circle(100)
    brush.right(angle_step)
canvas.exitonclick()
