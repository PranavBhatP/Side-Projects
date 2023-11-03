THEME_COLOR = "#375362"
from tkinter import *#type: ignore

class QuizInterface:
    def __init__(self):

        self.win = Tk()
        self.win.title("Quiz App")
        self.win.config(padx= 20, pady = 20, bg = THEME_COLOR)

        self.score_label = Label(text= "Score: 0", fg = THEME_COLOR)
        self.score_label.grid(row = 0, column = 1)
        self.canvas  = Canvas(self.win, height = 250, width = 300, highlightthickness= 0, background= "white")
        self.canvas.pack()

        question = self.canvas.create_text(125, 150, text = "Question", font = ('Ariel',20, 'italic'))
        self.win.mainloop()