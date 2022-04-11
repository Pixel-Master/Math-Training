# A Window Variant of the Math Quiz

# Imports
import tkinter as tk
import random as rnd

# The Launcher Window
root = tk.Tk()
root.title('Math Training Launcher.0.1')
root.resizable(False, False)
root.iconbitmap('/Users/constipixel/Documents/Phyton/math_quiz/assets/math_quiz_icon.ico')
root.geometry('600x400+50+50')

# Setting up the Variables
modus = "non"
score = 0


# The Settings Window
def settings():
    settingswindow = tk.Tk()
    settingswindow.title('Settings')
    settingswindow.resizable(False, False)
    settingswindow.iconbitmap('/Users/constipixel/Documents/Phyton/math_quiz/assets/math_quiz_icon.ico')
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
hello = tk.Label(root, text="WELCOME TO THE MATH QUIZ!(version: 0.1)!", font=("Arial", 25, "bold"))
hello.pack()


# The event for the "Play!" Button
# noinspection PyTypeChecker
def startgame():
    Answer = format(value_inside.get())
    print(Answer)
    print("Selected Option: {}".format(value_inside.get()))
    # The mainloop for "+"
    if Answer == "+":
        plus = tk.Tk()
        plus.title("Math")
        plus.resizable(False, False)
        plus.iconbitmap('/Users/constipixel/Documents/Phyton/math_quiz/assets/math_quiz_icon.ico')
        plus.geometry('600x400+50+50')
        a = rnd.randint(1, 5)
        b = rnd.randint(1, 5)
        questionLabel = tk.Label(plus, text=("What results in" + a + "+" + b + "?"), font=("Arial", 25, "bold"))
        questionLabel.pack()


# The function for the "Select a Mode" table
def start():
    global value_inside
    value_inside = tk.StringVar(root)
    options_list = ["+", "-", "*", "-"]
    value_inside.set("Select a Mode")
    hello.config(text="Choose your Mode!")
    question_menu = tk.OptionMenu(root, value_inside, *options_list)
    question_menu.pack(side="top")
    started.config(text="Play!", command=startgame)


# Adds a command to the "Next" Button
started.config(command=start)
# The mainloop
root.mainloop()
