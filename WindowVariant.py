# A Window Variant of the Math Quiz

# Imports
import tkinter as tk
from tkinter import messagebox as msg
import random as rnd

# The Launcher Window
root = tk.Tk()
root.title('Math Training Launcher v0.2')
root.resizable(False, False)
root.geometry('600x400+50+50')

# Setting up the Variables
modus = "non"
score = 0


# The Settings Window
def settings():
    settingswindow = tk.Tk()
    settingswindow.title('Settings')
    settingswindow.resizable(False, False)
    settingswindow.geometry('600x400+50+50')
    Close = tk.Button(settingswindow, text="Close", command=settingswindow.destroy, fg="red")
    Close.pack(side="bottom")


# The Settings Button
Settings = tk.Button(root, text="Settings", command=settings, fg="red", )
Settings.pack(side="bottom")

# The Launcher GUI
global started
global hello
started = tk.Button(root, text='Next', fg="black", font=("Arial", 30))
started.pack(side="bottom")
hello = tk.Label(root, text="WELCOME TO THE MATH QUIZ!", font=("Arial", 25, "bold"))
hello.pack()


# The event for the "Play!" Button
def startgame():
    Answer = format(value_inside.get())
    print("Selected Option: {}".format(value_inside.get()))
    root.withdraw()
    # The mainloop for "+"
    if Answer == "+":
        # Setting up the Window
        plus = tk.Tk()
        plus.title("Plus Math Training v0.2")
        plus.resizable(False, False)
        plus.geometry('600x400+50+50')

        # Some Stuff
        def result(score):
            answ = tk.StringVar()
            p_a = rnd.randint(1, 5)
            p_b = rnd.randint(1, 5)
            plus_answer = p_a + p_b
            questionLabel = tk.Label(plus, text=("What results in 0 + 0 ?"), font=("Arial", 25, "bold"))
            questionLabel.pack(side="top")
            answerField = tk.Entry(plus, width=20,textvariable=answ)
            answerField.insert(0,"")
            answerField.pack(side="bottom")

        result(score)
    # The mainloop for "-"
    elif Answer == "-":
        msg.askyesno("dev -", "This is still in development do you want to proceed anyways", )
        msg.showerror("nothing -", "This Mode is still in developing")

    # The mainloop for "*"
    elif Answer == "*":
        msg.askyesno("dev *", "This is still in development do you want to proceed anyways", )
        msg.showerror("nothing *", "This Mode is still in developing")

    # The mainloop for "/"
    elif Answer == "/":
        msg.askyesno("dev /", "This is still in development do you want to proceed anyways", )
        msg.showerror("nothing /", "This Mode is still in developing")

    # Error when selecting no Mode
    elif Answer == "Select a Mode":
        msg.showwarning("No Mode", "Select a valid Mode")

    # You will NEVER see THIS
    else:
        msg.showwarning("Fatal", "You've broke the System!")


# The function for the "Select a Mode" table
def start():
    global value_inside
    value_inside = tk.StringVar(root)
    options_list = ["+", "-", "*", "/"]
    value_inside.set("Select a Mode")
    hello.config(text="Choose your Mode!")
    question_menu = tk.OptionMenu(root, value_inside, *options_list)
    question_menu.pack(side="top")
    started.config(text="Play!", command=startgame)


# Adds an event to the "Next" Button
started.config(command=start)

# The mainloop
root.mainloop()
