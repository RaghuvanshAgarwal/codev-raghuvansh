import turtle
from turtle import Screen, Turtle
from turtle_player import TurtlePlayer
import random

screen = Screen()
screen.setup(1000, 900)
user_bet = screen.textinput(title="Make your Bet", prompt="[Red | Orange | Pink | Green | Blue | Purple] "
                                                          "\nGuess which turtle will win the race : ").lower()

colors = ["red", "orange", "pink", "green", "blue", "purple"]
players = []


def initialize_players():
    global players
    y = -250
    for _ in range(6):
        player = TurtlePlayer(color=colors[_])
        player.go_to(-400, y)
        players.append(player)
        y += 100


def move_players():
    for player in players:
        player.move(direction=0, speed=random.random() * 20)


def check_end_game():
    global players
    flag = False
    color = "black"
    for player in players:
        if not flag:
            if player.get_player_x() > 420:
                flag = True
                color = player.get_player_color()
    return color


initialize_players()
end_game = False
winning_player_color = ""
while not end_game:
    move_players()
    turtle_color = check_end_game()
    if turtle_color != "black":
        winning_player_color = turtle_color
        end_game = True

print(f"{winning_player_color} Player won the race")
ui = Turtle()
ui.hideturtle()
ui.color(winning_player_color)
if user_bet == winning_player_color:
    ui.write(f"Congratulations {winning_player_color.capitalize()} Player won the race", align="center",
             font=("Arial", 32, "bold"))
else:
    ui.write(f"Try Again {winning_player_color.capitalize()} Player won the race", align="center",
             font=("Arial", 32, "bold"))
screen.exitonclick()
