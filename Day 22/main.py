from turtle import Screen
from Ball import Ball
from paddle import Paddle
from score_manager import ScoreManager
from boundary_line import BoundaryLine
import time

# Screen Setup Start
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.listen()
screen.tracer(0)

# Paddle Setup
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

# Ball Setup
ball = Ball(position=(0, 0))

# Score Manager
score_manager = ScoreManager(position=(0, 150))

# Boundary Line
boundary_line = BoundaryLine(position=(0, -290))

# Key Binding
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")


def ball_wall_bounce_check():
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.vertical_bounce()


def ball_bounce_paddle_check():
    if (ball.distance(r_paddle.pos()) < 50 and ball.xcor() > 330) or (
            ball.distance(l_paddle.pos()) < 50 and ball.xcor() < -330):
        ball.horizontal_bounce()


def game_over_check():
    """
    :return: 0 = Inside Screen | 1 = Outside Right Wall | -1 = Outside Left Wall
    """
    if ball.xcor() > 390:
        result = 1
    elif ball.xcor() < -390:
        result = -1
    else:
        result = 0
    return result


# Main Game Loop
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    ball_wall_bounce_check()
    ball_bounce_paddle_check()
    check = game_over_check()
    if check == 1:
        score_manager.increase_score(paddle="left")
        time.sleep(ball.ball_speed)
        ball.reset_state()
    elif check == -1:
        score_manager.increase_score(paddle="right")
        time.sleep(0.25)
        ball.reset_state()
screen.exitonclick()
