from tkinter import *
import pywhatkit




        
root = Tk()
root.title("WhatsApp Bot")
root.geometry("400x300")

def send_message(message, phoneno, hours, minutes):
    if message != '' and hours != '' and minutes != '' and phoneno != '':
        try:
            pywhatkit.sendwhatmsg(f"+91{phoneno}", f"{message}", hours, minutes)
            label_display = Label(root, text = "Message will be sent soon!")
            label_display.grid(row = 7, column = 4)
        except:
            label_display = Label(root, text = "Unable to send message!")
            label_display.grid(row = 7, column = 4)
    else:
        label_display = Label(root, text = "Please enter your details fully and correctly")
        label_display.grid(row = 7, column = 4)
Label(root, text = "WhatsApp Bot", font = "times 15 bold").grid(row = 0, column = 3)


l1 = Label(root, text = "Phone No")
l1.grid(row = 1, column  = 2)

l2 = Label(root, text = "Message")
l2.grid(row = 2, column  = 2)

l3 = Label(root, text = "Hour(in 24)")
l3.grid(row = 3, column  = 2)

l4 = Label(root, text = "Minutes(in 60)")
l4.grid(row = 4, column  = 2)

e1 = Entry(root)
e1.grid(row = 1, column = 3)

e2 = Entry(root)
e2.grid(row = 2, column = 3)

e3 = Entry(root)
e3.grid(row = 3, column = 3)

e4 = Entry(root)
e4.grid(row = 4, column = 3)

button = Button(root, text = "Send message", command = lambda : send_message(e1.get(), e2.get(), int(e3.get()), int(e4.get())))
button.grid(row = 6, column = 3)

# label_display = Label(root)
# label_display.grid(row = 7, column = 4)
# e2 = Entry(root, width = 50)
# e2.pack()
# e2.insert(0, "Enter the message")


# e3 = Entry(root, width = 50)
# e3.pack()
# e3.insert(0, "Enter the time in hours(24 hrs)")

# e4 = Entry(root, width = 50)
# e4.pack()
# e4.insert(0, "Enter the time in minutes(60 mins)")








root.mainloop()

