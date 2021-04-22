from turtle import Turtle
import random

FOOD_LOCATION = [ -280, -260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0,
                  20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shape("circle")
        self.hideturtle()
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.refresh()

    def refresh(self):
        self.goto(random.choice(FOOD_LOCATION), random.choice(FOOD_LOCATION))
        self.showturtle()
