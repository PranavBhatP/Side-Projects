THEME_COLOR = "#375362"
from tkinter import *#type: ignore
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.win = Tk()
        self.win.title("Quiz App")
        self.win.config(padx= 20, pady = 20, bg = THEME_COLOR)

        self.score_label = Label(text= "Score: 0", bg='#fff')
        self.score_label.grid(row = 0, column = 1)
        self.canvas  = Canvas(self.win, height = 250, width = 300, highlightthickness= 0, background= "white")

        self.question_text = self.canvas.create_text(150, 125, text = "Question", fill = THEME_COLOR, font = ('Ariel',20, 'italic'), width = 280)
        self.canvas.grid(row = 1, column = 0, columnspan = 2, pady = 50)
        true_image = PhotoImage(file = "/Users/prana/OneDrive/Desktop/Python Code/Side-Projects/API Projects/QuizApp/images/true.png") 
        self.true_button = Button(image = true_image, highlightthickness = 0,command = lambda: self.true_button_press())
        self.true_button.grid(row = 2, column = 0)

        false_image = PhotoImage(file = "/Users/prana/OneDrive/Desktop/Python Code/Side-Projects/API Projects/QuizApp/images/false.png")
        
        self.false_button = Button(image = false_image, highlightthickness= 0, command = lambda: self.false_button_press())
        self.false_button.grid(row = 2, column = 1)

        self.get_next_question()
        self.win.mainloop()

    def get_next_question(self):
        self.canvas.config(bg = "white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
        else:
            q_text = f"Thank you for playing, your score is {self.quiz.score}/10"
        self.canvas.itemconfig(self.question_text, text = q_text)
        self.score_label.config(text = f"Score: {self.quiz.score}, Question: {self.quiz.question_number}/10")

    def true_button_press(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def false_button_press(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.win.after(1000, self.get_next_question())
