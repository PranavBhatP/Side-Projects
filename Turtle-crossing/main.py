import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import winsound


player = Player()
car_mng = CarManager()
scr_board = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkeypress(player.move_up, "w")
screen.onkeypress(player.move_down, "s")


game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    
    # x = random.randint(0,2)
    # y = random.randint(3,5)
    # z = random.randint(6,9)
    # car_mng.move_cars(x)
    # car_mng.move_cars(y)
    # car_mng.move_cars(z)

    for i in range(len(car_mng.cars_list)):
        car_mng.move_cars(i)

    

    car_mng.check_out_of_bounds()

    if player.check_win() :
        car_mng.add_cars(car_mng.cars_list)
        scr_board.level += 1
        car_mng.speed += 0.5

    for car in car_mng.cars_list:
        if car.distance(player) < 15:
            
            scr_board.clear()
            winsound.PlaySound("squish.wav", winsound.SND_ASYNC)
            player.goto((0, -280))
            for car in car_mng.cars_list[10:]:
                car.goto((1000,1000))
            
            for car in car_mng.cars_list[:10]:
                car.goto((310, random.randint(-200, 200)))
                car.speed(3)
                
            car_mng.cars_list = car_mng.cars_list[0:10]
            scr_board.level = 1
            print(scr_board.level)
            print(car_mng.cars_list[9].speed())
            scr_board.write("Game Over!", align = "center",font=("Courier", 24, "normal"))
            
            time.sleep(1)
    
    



    scr_board.score_update()
screen.mainloop()
screen.exitonclick()
#Game Complete!!