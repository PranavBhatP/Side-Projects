
import time
from tkinter import *
# from PIL import ImageTk, Image

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# win =  Tk()
# win.geometry("700x500")


# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    mins = 5
    secs = 0
    init_time = 0
    timer_count = canvas.create_text(300, 225, text = f"{mins}" + ":" + f"{secs}", fill = 'white', font = (FONT_NAME, 35, "bold"))
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_countdown():

    init_time = 5*60
    mins = 5
    secs = 0
    timer_count = canvas.create_text(300, 225, text = f"{mins}" + ":" + f"{secs}", fill = 'white', font = (FONT_NAME, 35, "bold"))

    while init_time > -1:
        mins = init_time // 60
        secs = init_time % 60
        if secs >= 10:
            canvas.itemconfig(timer_count,text = f"{mins}" + ":" + f"{secs}" )
        else:
            canvas.itemconfig(timer_count,text = f"{mins}" + ":0" + f"{secs}" )
        init_time -= 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown():
    init_time  = 5
    count = canvas.create_text(300, 225, text = f"{init_time}", fill = 'white', font = (FONT_NAME, 35, "bold"))
    while init_time > -1:
        canvas.itemconfig(count, text = f"{init_time}")
        init_time -= 1
        win.update()
        time.sleep(1)

    
# ---------------------------- UI SETUP ------------------------------- #
win =  Tk()
win.title("Pomodoro App")
win.config(padx = 100, pady = 50, bg =  YELLOW)
# win.geometry("700x500")

canvas = Canvas(win, width = 600, height  = 400, bg = YELLOW, highlightthickness= 0)
canvas.pack()
img  = PhotoImage(file = "/Users/prana/OneDrive/Desktop/Python Code/Side-Projects/Pomodoro App/tomato.png")
canvas.create_image(300, 200, image = img)
canvas.create_text(300, 225, text = "5:00", fill = 'white', font = (FONT_NAME, 35, "bold"))
canvas.create_text(300, 50, text = "Pomodoro Timer", fill = "Black", font = (FONT_NAME, 35, "bold"))


btn_pressed = False 
def check_button():
    btn_pressed = True
canvas.grid(column = 1, row = 0)
start_btn = Button(win, text = "Start", font = (FONT_NAME, 10, "bold"), highlightthickness= 0, command = lambda : check_button)
start_btn.grid(column = 0, row = 1)

reset_btn = Button(win, text = "Reset", font = (FONT_NAME, 10, "bold"), highlightthickness= 0, command = lambda : timer_reset)
reset_btn.grid(column= 2, row = 1)

check_time = Label(win, text = "✔")
check_time.grid(column  = 1, row  = 2)




win.mainloop()