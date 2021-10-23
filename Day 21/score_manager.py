from turtle import Turtle


class ScoreManager(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = [0, 0]
        self.goto(position)
        self.draw()

    def draw(self):
        self.clear()
        self.write(f"{self.score[0]}\t{self.score[1]}", align="center", font=("bungee", 50, "bold"))

    def increase_score(self, paddle):
        if paddle == "right":
            self.score[1] += 1
        elif paddle == "left":
            self.score[0] += 1

        self.draw()
