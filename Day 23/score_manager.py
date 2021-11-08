from turtle import Turtle


class ScoreManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 125)
        self.score = 0
        self.draw()

    def draw(self):
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("bungee", 50, "bold"))

    def increase_score(self):
        self.score += 1
        self.draw()
