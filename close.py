import window
import os
import platform
print("Successful imported Close!")
global close_without_ask
close_without_ask = False
#math = tk.Tk()
#math.resizable(False, False)
#math.geometry('600x400+500+500')
#math.withdraw()

def past():
    pass

def root_quit():
    if platform.system() == "Darwin":
        # os.chdir("Library")
        print(os.getcwd())
    if close_without_ask:
        quit()
    else:
        print("Asked before Quitting")
        quit()
def mathclose():
    window.math.withdraw()
    print("Close!")
    window.root.deiconify()
