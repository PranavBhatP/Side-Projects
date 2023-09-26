FONT = ("Courier", 12, "normal")

import turtle
import pandas as pd
screen = turtle.Screen()
screen.setup(height = 900, width = 800)
screen.title("Guess the states of India")
image = "/Users/prana/OneDrive/Desktop/Python Code/Side-Projects/State-Guessing-Game/india_blank_map.gif"

screen.addshape(image)


pen = turtle.Turtle()
pen.penup()

pen.hideturtle()


scoreboard = turtle.Turtle()
scoreboard.penup()
scoreboard.hideturtle()

turtle.shape(image)
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

data = pd.read_csv("/Users/prana/OneDrive/Desktop/Python Code/Side-Projects/State-Guessing-Game/states_of_india.csv")

states_list = data["State"].to_list()
x_cors = data["x"].to_list()
y_cors = data["y"].to_list()


# for i in range(len(states_list)):
#     if i == 0:
#         pen.goto((50,300))
#         pen.write("State Guessing Game", font = ("Courier", 18, "normal"))
#     pen.goto((x_cors[i], y_cors[i]))
#     pen.write(states_list[i])

gameon = True

crct_guess = []
pen.goto((50,300))
pen.write("""State Guessing Game\nType exit to quit.""", font = ("Courier", 18, "normal"))
scoreboard.goto((150, 270))
scoreboard.write(f"{len(crct_guess)}/30", align='center', font = ("Courier", 18, "normal"))

while len(crct_guess) < 29:

    tut = str(turtle.textinput("Input", "Enter your guess"))

    if tut.title() in states_list and tut.title() not in crct_guess:
        ele_index = states_list.index(tut.title())
        pen.goto(x_cors[ele_index], y_cors[ele_index])
        pen.write(tut.title(), align= 'center', font = FONT)
        crct_guess.append(tut.title())
        scoreboard.clear()
        #scoreboard.goto((40, 300))
        scoreboard.write(f"{len(crct_guess)}/30", align='center', font = ("Courier", 18, "normal"))
    elif tut == "exit":
        break
    else:
        continue



screen.exitonclick()


