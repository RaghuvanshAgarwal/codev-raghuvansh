from turtle import Screen
from player import Player
from car_manager import CarManager
from score_manager import ScoreManager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


player = Player(starting_position=(0, -280))
screen.onkey(player.move_forward, "space")
car_manager = CarManager(player=player)
score_manager = ScoreManager()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.update()
    if player.ycor() > 300:
        player.goto(0,-280)
        score_manager.increase_score()
    if car_manager.collision_check():
        print("Game over")
        game_is_on = False

screen.exitonclick()
