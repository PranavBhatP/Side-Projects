
import time
from tkinter import * # type: ignore
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

reps = 1
is_running = True
tick_rows = 2
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps
    reps = 1
    global is_running
    is_running = False
    work_sec = WORK_MIN
    canvas.itemconfig(timer_count, text = f"{work_sec}:00")
    canvas.itemconfig(timer_title, text = "Pomodoro Timer")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_countdown():
    global tick_rows
    global reps
    global is_running
    is_running = True
    work_sec = WORK_MIN
    short_break = SHORT_BREAK_MIN
    long_break = LONG_BREAK_MIN

    if reps % 8  == 0:
        check_time = Label(win, text = "✔")
        tick_rows += 1
        check_time.grid(column  = 1, row  = tick_rows)
        canvas.itemconfig(timer_title, text= "Long Break")
        countdown(long_break * 60)
    elif reps % 2 == 0:
        check_time = Label(win, text = "✔")
        tick_rows += 1
        check_time.grid(column  = 1, row  = tick_rows)
        canvas.itemconfig(timer_title, text = "Short Break")
        countdown(short_break * 60)
    else:
        canvas.itemconfig(timer_title, text = "Time to work!")
        countdown(work_sec * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(counter):
    
    if is_running:
        global reps
        count = counter
        mins = count//60
        secs = count % 60
        if secs >= 10:
            canvas.itemconfig(timer_count, text = f"{mins}:{secs}")
        else:
            canvas.itemconfig(timer_count, text = f"{mins}:0{secs}")
        if count > 0:
            win.after(1000, countdown, count-1)
        else:
            reps += 1
            timer_countdown()
    # reset =  False

    
# ---------------------------- UI SETUP ------------------------------- #
win =  Tk()
win.title("Pomodoro App")
win.config(padx = 100, pady = 50, bg =  YELLOW)
# win.geometry("700x500")

canvas = Canvas(win, width = 600, height  = 400, bg = YELLOW, highlightthickness= 0)
canvas.pack()
img  = PhotoImage(file = "/Users/prana/OneDrive/Desktop/Python Code/Side-Projects/Pomodoro App/tomato.png")
canvas.create_image(300, 200, image = img)
timer_count  = canvas.create_text(300, 225, text =f"{WORK_MIN}:00", fill = 'white', font = (FONT_NAME, 35, "bold"))
timer_title = canvas.create_text(300, 50, text = "Pomodoro Timer", fill = "Black", font = (FONT_NAME, 35, "bold"))

canvas.grid(column = 1, row = 0)
start_btn = Button(win, text = "Start", font = (FONT_NAME, 10, "bold"), highlightthickness= 0, command = lambda : timer_countdown())
start_btn.grid(column = 0, row = 1)

reset_btn = Button(win, text = "Reset", font = (FONT_NAME, 10, "bold"), highlightthickness= 0, command = lambda : timer_reset())
reset_btn.grid(column= 2, row = 1)

check_time = Label(win, text = "✔")
check_time.grid(column  = 1, row  = tick_rows)


win.mainloop()