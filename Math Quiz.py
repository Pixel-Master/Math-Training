# A Window Variant of the Math Quiz

# Imports
print("Importing Libraries...")
import tkinter as tk
from tkinter import messagebox as msg
print("Successful imported Tkinter!")
import random as rnd
print("Successful imported Random!")
from close import *
from window import *
from numbers import *
from os import *
print("Successful imported Os!")
print("Done!")


# The Launcher Window
root_setup()

# Setting up the Variables
modus = "non"
global score, Proof, m_a, m_b, mr_a, mr_b, math, root
score = 0
log = "non"
askformat = 0
global started
global hello



# The event for the "Play!" Button
def startgame():

    # Get the Selected Mode
    global mode
    mode = format(window.Mode_table.get())

    # Debug
    print("Selected Mode: {}".format(window.Mode_table.get()))

    # The function for the "Submit" button
    def clicked(mode_answer, try_ans):
        try_ans = format(answerField.get())
        global Proof
        print("Mode:", mode, "answer:", try_ans, "real Answer:", mode_answer)
        if try_ans == mode_answer:
            Proof = True
            score = + 1
        else:
            Proof = False
        print(Proof)

        m_a = rnd.randint(1, mr_a)
        m_b = rnd.randint(1, mr_b)

        if mode == "+":
            mode_answer = m_a + m_b

    # Hide the Launcher Window
    root.withdraw()

    # Setting up the Window
    math = tk.Tk()
    math.resizable(False, False)
    math.geometry('600x400+500+500')
    math.withdraw()

    # Setting up the GUI
    questionLabel = tk.Label(math, text=askformat, font=("Arial", 25, "bold"))
    questionLabel.config()
    questionLabel.pack(side="top")
    answerField = tk.Entry(math)
    answerField.pack(side="bottom")
    answerField.focus()
    Submit = tk.Button(math, text="Submit", )
    Submit.pack(side="bottom")
    close = tk.Button(math, text="Close", fg="red", command=mathclose())
    close.pack()
    close.place(x=510, y=350)

    # The code for "+"
    if mode == "+":
        # Showing the Window
        math.deiconify()

        # Setting the window title
        math.title("Plus Math Training v0.2")

        # Some variables
        plus_answer = "0"
        mr_a = 5
        mr_b = 5
        m_a = rnd.randint(0, mr_a)
        m_b = rnd.randint(0, mr_b)
        try_answer = format(answerField.get())

        # Event for clicking "Submit" button
        Submit.config(command=clicked(plus_answer, try_answer))
        p_askformat = 'What results in {1} + {1}'.format(m_a, m_b)
        questionLabel.config(text=p_askformat)

        # Debug
        print("Mode:", mode, "answer:", try_answer, "real Answer:", plus_answer, "mode not func")
        print("m_a:", m_a, "m_b:", m_b)

    # The code for "-"
    elif mode == "-":
        msg.askyesno("dev -", "This is still in development do you want to proceed anyways", )
        msg.showerror("nothing -", "This Mode is still in developing", command=root.deiconify())
    # The code for "*"
    elif mode == "*":
        msg.askyesno("dev *", "This is still in development do you want to proceed anyways", )
        msg.showerror("nothing *", "This Mode is still in developing", command=root.deiconify())

    # The code for "/"
    elif mode == "/":
        msg.askyesno("dev /", "This is still in development do you want to proceed anyways", )
        msg.showerror("nothing /", "This Mode is still in developing", command=root.deiconify())

    # Error when selecting no Mode
    elif mode == "Select a Mode":
        msg.showwarning("No Mode", "Select a valid Mode", command=root.deiconify())

    # You will NEVER see THIS
    else:
        msg.showwarning("Fatal", "You've broke the System!", command=root.deiconify())



