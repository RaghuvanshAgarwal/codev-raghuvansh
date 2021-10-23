import turtle

import colorgram
from random import choice
from turtle import Turtle, Screen, colormode
images = ["image.jpg", "tree.jpg", "heart.jpg"]
colors = colorgram.extract(choice(images), 20)
brush = Turtle()
screen = Screen()
initial_x = -450
initial_y = 375
screen.screensize(500, 500)
brush.penup()
brush.speed("fastest")
brush.goto(initial_x, initial_y)
brush.hideturtle()
colormode(255)


def draw_dot():
    color = choice(colors).rgb
    brush.pendown()
    brush.fillcolor(color)
    brush.color(color)
    brush.begin_fill()
    brush.circle(10)
    brush.end_fill()
    brush.penup()


for row_index in range(15):
    for column_index in range(15):
        brush.goto(initial_x + (column_index * 50), initial_y - (row_index * 50))
        draw_dot()

screen.exitonclick()
