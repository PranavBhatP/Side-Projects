BACKGROUND_COLOR = "#B1DDC6"

from tkinter import * #type: ignore
import time
import random
import pandas as pd
import csv

TIMER_COUNT = 5
BREAK_COUNT = 3
win = Tk()
win.title("Flash Cards")
win.config(padx = 50, pady = 50, bg= BACKGROUND_COLOR)

crt_listen = True

#----------------------------CSV File Parser-------------------------+
word_data = pd.read_csv("/Users/prana/OneDrive/Desktop/Python Code/Side-Projects/FlashCardApp/data/hindi_words.csv")
hindi_words = word_data["Hindi"].to_list()
eng_words = word_data["in English"].to_list()
hindi_word = "पृथ्वी"

#known_word_data = pd.read_csv("C:/Users/prana/OneDrive/Desktop/Python Code/Side-Projects/FlashCardApp/data/known_words.csv")
df_dict = {
    "Hindi": [],
    "English": []
}

#----------------------------Button press listeners -----------------+
def r_btn_press(): 
    # rows = ["Hindi", "in English"]
    # known_word_info = [[hindi_word, eng_words[hindi_words.index(hindi_word)]]]
    # try:
    #     with open("C:/Users/prana/OneDrive/Desktop/Python Code/Side-Projects/FlashCardApp/data/known_words.csv", "r") as file:
    #         data = csv.writer(file)
    # except FileNotFoundError:
    #     with open("C:/Users/prana/OneDrive/Desktop/Python Code/Side-Projects/FlashCardApp/data/known_words.csv", "w") as file:
    #         data  = csv.writer(file)
    #         data.writerow(rows)
    #         data.writerow(known_word_info)
    # else:
    #     with open("C:/Users/prana/OneDrive/Desktop/Python Code/Side-Projects/FlashCardApp/data/known_words.csv", "w") as file:
    #         data.writerow(known_word_info)
    #Or we can implement it as a pandas dataframe
    
    global crt_listen
    if not crt_listen:
        crt_listen = True
    
    
def w_btn_press():
    global crt_listen
    if crt_listen:
        crt_listen = False 

#---------------------------Screen Transistions----------------------+
def choose_word():
    choice = random.choice(hindi_words)
    return choice

def display_eng():
    global hindi_word
    canvas.itemconfig(card_image, image = bg_img_back)
    canvas.itemconfig(top_title, text = "English", fill = 'white')
    canvas.itemconfig(mid_title, text = f"{eng_words[hindi_words.index(hindi_word)]}", fill = "white")
    
def display_hind():
    global hindi_word
    global eng_words
    global hindi_words
    global eng_words
    global df_dict
    df_dict["Hindi"].append(hindi_word)
    df_dict["English"].append(eng_words[hindi_words.index(hindi_word)])
    data = pd.DataFrame(df_dict)
    data.to_csv("C:/Users/prana/OneDrive/Desktop/Python Code/Side-Projects/FlashCardApp/data/known_words.csv", index = False)
    
    hindi_word = choose_word()
    #canvas.configure(background= "#014f3f")
    canvas.itemconfig(card_image, image = bg_img_front)
    canvas.itemconfig(top_title, text = 'Hindi', fill = "black")
    canvas.itemconfig(mid_title, text = f"{hindi_word}", fill = "black")    
#----------------------------Question Timer--------------------------+
# def set_timer(count):
    
#     secs = count
#     # canvas.itemconfig(countdown, text = f"Timer: {secs}")
#     # canvas.itemconfig(score, text = f"Word count: 1")
#     if count > 0:
#         win.after(1000, set_timer, count-1)
#     else:
#         change_page()

# def timer_countdown():
#     set_timer(TIMER_COUNT)
#----------------------------UI Setup--------------------------------+
canvas = Canvas(win, height = 526, width = 800,highlightthickness= 0)
canvas.pack()
bg_img_front = PhotoImage(file = "/Users/prana/OneDrive/Desktop/Python Code/Side-Projects/FlashCardApp/images/card_front.png")
bg_img_back = PhotoImage(file = "/Users/prana/OneDrive/Desktop/Python Code/Side-Projects/FlashCardApp/images/card_back.png")
card_image = canvas.create_image(400, 263, image = bg_img_front)
top_title = canvas.create_text(400, 150, text = "Hindi", font = ("Ariel", 40, "italic"))
mid_title = canvas.create_text(400, 263, text = "पृथ्वी", font = ("Ariel", 60, "bold"))
# countdown = canvas.create_text(200, 150, text = "Timer : 5", font = ("Ariel", 15, "bold"))
# score = canvas.create_text(600, 150, text = "Word count: 1", font = ("Ariel", 15, "bold"))

# down_btn = Button(win, text = "Start", highlightthickness= 0, background= '#FFFFFF', command = lambda : timer_countdown())
# down_btn.place(x = 400, y = 400)

canvas.configure(background= BACKGROUND_COLOR)
canvas.grid(row = 0, column = 0, columnspan= 2)

r_img = PhotoImage(file ="C:/Users/prana/OneDrive/Desktop/Python Code/Side-Projects/FlashCardApp/images/right.png")
r_btn = Button(image = r_img, highlightthickness= 0, background= BACKGROUND_COLOR, command = lambda : display_hind())
r_btn.grid(row = 1, column = 1)

w_img = PhotoImage(file ="C:/Users/prana/OneDrive/Desktop/Python Code/Side-Projects/FlashCardApp/images/wrong.png")
w_btn = Button(image = w_img, highlightthickness= 0, background= BACKGROUND_COLOR, command = lambda : display_eng())
w_btn.grid(row = 1, column = 0)

win.mainloop()
