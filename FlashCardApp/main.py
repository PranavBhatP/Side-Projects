BACKGROUND_COLOR = "#B1DDC6"

from tkinter import * #type: ignore


win = Tk()
win.title("Flash Cards")
win.config(padx = 50, pady = 50, bg= BACKGROUND_COLOR)

canvas = Canvas(win, height = 526, width = 800,highlightthickness= 0)
canvas.pack()
bg_img = PhotoImage(file = "/Users/prana/OneDrive/Desktop/Python Code/Side-Projects/FlashCardApp/images/card_front.png")
canvas.create_image(400, 263, image = bg_img)
canvas.create_text(400, 150, text = "Flash card", font = ("Ariel", 40, "italic"))
canvas.create_text(400, 263, text = "पृथ्वी", font = ("Ariel", 60, "bold"))
canvas.configure(background= BACKGROUND_COLOR)
canvas.grid(row = 0, column = 0, columnspan= 2)

r_img = PhotoImage(file ="C:/Users/prana/OneDrive/Desktop/Python Code/Side-Projects/FlashCardApp/images/right.png")
r_btn = Button(image = r_img, highlightthickness= 0, background= BACKGROUND_COLOR)
r_btn.grid(row = 1, column = 1)


w_img = PhotoImage(file ="C:/Users/prana/OneDrive/Desktop/Python Code/Side-Projects/FlashCardApp/images/wrong.png")
w_btn = Button(image = w_img, highlightthickness= 0, background= BACKGROUND_COLOR)
w_btn.grid(row = 1, column = 0)
win.mainloop()
