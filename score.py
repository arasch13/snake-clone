from turtle import Turtle

FONT = "Tahoma"
COLOR = "white"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(COLOR)
        self.penup()
        self.goto((0, 280))
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
