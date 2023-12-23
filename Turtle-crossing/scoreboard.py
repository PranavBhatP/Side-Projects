FONT = ("Courier", 24, "normal")

import turtle
class Scoreboard(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.speed(0)
        self.shape("square")
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(f"Level : {self.level}", align = 'center', font = FONT)

    def score_update(self):
        self.clear()
        self.write(f"Level : {self.level}", align = 'center', font = FONT)

    

