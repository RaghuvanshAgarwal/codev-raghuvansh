from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

food.goto(random.randint(-280, 280), random.randint(-280, 280))
game_not_over = True
while game_not_over:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if food.detect_collision(snake):
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        snake.add_segment()
        scoreboard.increase_score()
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_not_over = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_not_over = False
            scoreboard.game_over()

screen.exitonclick()
