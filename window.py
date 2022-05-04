import tkinter as tk
import close
print("Successful imported Window!")
global root, math
import math

# "Select a Mode" Drop-down
def start():
    global Mode_table
    Mode_table = tk.StringVar(root)
    options_list = ["+", "-", "*", "/"]
    Mode_table.set("Select a Mode")
    hello.config(text="Choose your Mode!")
    question_menu = tk.OptionMenu(root, Mode_table, *options_list)
    question_menu.pack(side="top")
    started.config(text="Play!", command=close.past())

# The Settings Window
def settings_setup():
    settingswindow = tk.Tk()
    settingswindow.title('Settings')
    settingswindow.resizable(False, False)
    settingswindow.geometry('600x400+50+50')
    Close = tk.Button(settingswindow, text="Close", command=settingswindow.destroy, fg="red")
    Close.pack(side="bottom")
    Close.place(x=510, y=350)

    # "Options" Label
    options = tk.Label(settingswindow,text="Options",font=("Arial-BoldMT",40))
    options.place(x=10,y=5)
    # Options
    close_without_ask_button = tk.Checkbutton(settingswindow, text="Closing the Application without asking?",offvalue=False,onvalue=True,variable=close.close_without_ask)
    close_without_ask_button.place(x=20,y=60)
    hard_exercises = tk.Checkbutton(settingswindow,text="Harder Exercises?")
    hard_exercises.place(x=20,y=80)

# The Launcher Window
def root_setup():
    global root
    root = tk.Tk()
    root.title('Math Training Launcher v0.2')
    root.resizable(False, False)
    root.geometry('600x400+50+50')

    # The Settings Button
    Settings = tk.Button(root, text="Settings", command=settings_setup, fg="red", )
    Settings.pack(side="bottom")
    Settings.place(x=510, y=350)

    # The "Next" Button
    global started
    started = tk.Button(root, text='Next', fg="black", font=("Arial", 30),command=start)
    started.pack(side="bottom")

    # Adds a "Quit"
    end = tk.Button(root, fg="red", text="Quit", command=close.root_quit)
    end.place(x=10, y=350)

    #The Welcome Label
    global hello
    hello = tk.Label(root, text="WELCOME TO THE MATH QUIZ!", font=("Arial", 25, "bold"))
    hello.pack()

    root.mainloop()