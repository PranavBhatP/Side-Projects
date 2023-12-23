STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

import turtle

class Player(turtle.Turtle):


    def __init__(self):
        
        super().__init__()
        self.penup()
        self.speed(4)
        self.setheading(90)
        self.shape('turtle')
        self.color("blue")
        self.goto(STARTING_POSITION)
    
    def move_up(self):
        self.setheading(90)
        self.forward(10)
    
    def move_down(self):
        self.backward(10)

    def check_win(self):
        if self.ycor() >= 200:
            self.goto(STARTING_POSITION)
            return True
        


