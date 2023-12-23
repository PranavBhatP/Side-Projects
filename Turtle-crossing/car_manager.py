COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import turtle
import random
class CarManager():
    
    def __init__(self):
        self.cars_list = []
        self.num_cars = 10
        self.speed = 3.0
        pen = turtle.Turtle()
        pen.hideturtle()
        for i in range(self.num_cars):
            new_car = turtle.Turtle("square")
            new_car.setheading(180)
            new_car.shapesize(stretch_wid = 1, stretch_len = 2)
            new_car.penup()
            pen.penup()
            pen.write(f"{10-i}", align = "center",font=("Courier", 24, "normal"))
            self.cars_list.append(new_car)
            self.cars_list[i].goto((310, random.randint(-200, 200)))
            self.cars_list[i].speed(self.speed)
            self.cars_list[i].color(random.choice(COLORS))
            pen.clear()
        pen.hideturtle()
    
    def add_cars(self, list):
        for i in range(2):
            new_car = turtle.Turtle("square")
            new_car.penup()
            new_car.goto((310, random.randint(-200, 200)))
            new_car.color(random.choice(COLORS))
            
            new_car.setheading(180)
            new_car.shapesize(stretch_wid = 1, stretch_len = 2)
            
            self.cars_list.append(new_car)
            

    def move_cars(self, car_no):
        self.cars_list[car_no].forward(random.randint(10,40))

    def check_out_of_bounds(self):
        for _ in range(len(self.cars_list)):
            if self.cars_list[_].xcor() <-310:
                self.cars_list[_].goto((310, random.randint(-200, 200)))      
