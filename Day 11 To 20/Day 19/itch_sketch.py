from turtle import Turtle, Screen

brush = Turtle()


# Logic Starts
def move_forward():
    brush.forward(5)


def move_backward():
    brush.backward(5)


def turn_right():
    brush.right(5)


def turn_left():
    brush.left(5)


screen = Screen()
screen.listen()


def clear_screen():
    screen.reset()
    brush.shapesize(2)
    brush.pensize(5)


clear_screen()
screen.onkeypress(move_forward, "Up")
screen.onkeypress(move_backward, "Down")
screen.onkeypress(turn_right, "Right")
screen.onkeypress(turn_left, "Left")
screen.onkey(screen.reset, "c")
screen.exitonclick()
