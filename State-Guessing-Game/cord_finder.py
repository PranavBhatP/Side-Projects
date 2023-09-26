FONT = ("Courier", 15, "normal")

import turtle
import pandas as pd
screen = turtle.Screen()
screen.setup(height = 900, width = 800)
screen.title("Guess the states of India")
image = "/Users/prana/OneDrive/Desktop/Python Code/Side-Projects/State-Guessing-Game/india_blank_map.gif"

screen.addshape(image)


pen = turtle.Turtle()
pen.goto((300,300))
pen.penup()
pen.hideturtle()
pen.write("State Guessing Game", font = ("Courier", 24, "normal"))
turtle.shape(image)
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

ans = turtle.textinput(title = "Enter", prompt = "Pleas enter some tex")
print(ans)
