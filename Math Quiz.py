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
global score
score = 0
log = "non"
global Proof

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
    # Get the Selected Mode
    global mode
    mode = format(value_inside.get())

    # Debug
    print("Selected Option: {}".format(value_inside.get()))

    # The function for the "Submit" button
    def clicked(mr_a, mr_b, mode_answer, m_a, m_b,try_ans):
        try_ans = format(answerField.get())
        global Proof
        print(mode, "answer:", try_ans, "real Answer:", mode_answer)
        msg.showerror(text="Only Numbers are Valid")
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

    # Setting up the GUI
    questionLabel = tk.Label(math, text="What results in 0 + 0 ?", font=("Arial", 25, "bold"))
    questionLabel.config()
    questionLabel.pack(side="top")
    answerField = tk.Entry(math, text="0")
    answerField.pack(side="bottom")
    answerField.focus()
    Submit = tk.Button(math, text="Submit", )
    Submit.pack(side="bottom")

    # The code for "+"
    if mode == "+":
        # Setting the window title
        math.title("Plus Math Training v0.2")
        try_answer = "0"
        plus_answer = "0"
        p_a = "0"
        p_b = "0"
        pr_a = 5
        try_answer = format(answerField.get())
        # Event for clicking "Submit" button
        Submit.config(command=clicked(pr_a, pr_a, plus_answer, p_a, p_b, try_answer))
        questionLabel.config(text="%.2f°C = %.2f°F" % (p_b, p_a))

        # Debug
        print(mode, "answer:", try_answer, "real Answer:", plus_answer)

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
