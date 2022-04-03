import tkinter as tk
from random import randint
from time import sleep
from tkinter.colorchooser import askcolor

modus = "non"
if modus != "+" or "-" or "*" or "/":
    score = 0
options_list = ["+", "-", "*", "-"]


def startgame():
    print("Start Game")


def settings():
    print("settings")


root = tk.Tk()
root.title('Math Training v.0.1')
root.resizable(False, False)
root.iconbitmap('./assets/math_quiz_icon.ico')
root.geometry('600x400+50+50')
Hello = tk.Label(root, text="WELCOME TO THE MATH QUIZ!(version: 0.1)", fg="black")
Hello.pack()
Settings = tk.Button(root, text="Settings", command=settings, fg="red", )
Settings.pack()


def start():
    value_inside = tk.StringVar(root)
    optionslist = ["+", "-", "*", "-"]
    value_inside.set("Select a Mode")
    mode = tk.Label(root, text="Choose your Mode!", height=10, width=50, fg="black")
    mode.pack()
    question_menu = tk.OptionMenu(root, value_inside, *optionslist)
    question_menu.pack()
    tk.destroy(Hello)
    question_menu = tk.OptionMenu(root, value_inside, *optionslist)
    question_menu.pack()
    submit_button = tk.Button(root, text='Start Game', command=startgame)
    submit_button.pack()
    root.mainloop()


started = tk.Button(root, text='Next', command=start, fg="black", font="Arial", )
started.pack()
root.mainloop()
