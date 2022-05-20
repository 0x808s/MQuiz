"""
02_Help_GUI_V0:
First try at help GUI using MSG box which is not
the desired method.
(Changed in V1)
"""

# Import Tkinter
from tkinter import *
# import partial from functools
from functools import partial
# Ttk as ttk
import tkinter.ttk as ttk
# Import msg box
import tkinter.messagebox


class Quiz:
    def __init__(self):
        # Formatting Variables
        print("Quiz Loaded")

        # Quiz start GUI
        self.quiz_frame = Frame(width=500, height=500)
        self.quiz_frame.grid()
        # Quiz title main (Maori Quiz)
        self.quiz_label = Label(text="Maori Quiz",
                                font=("Arial", "16", "bold"),

                                padx=10, pady=10)
        self.quiz_label.place(x=185, y=30)
        # Introduction text
        self.introduction_label = ttk.Label(text="TESTING HELP GUI")
        self.introduction_label.place(x=170, y=100)

        # Help button
        self.help_button = ttk.Button(text="Help",
                                      command=self.help_quiz)
        self.help_button.place(x=200, y=400)

    def help_quiz(self):
        print("you asked for help")
        tkinter.messagebox.showinfo("HELP!", "Example help text to help users"
                                             " navigate the quiz.")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("HELP GUI TESTER")
    # Import Azure theme DARK
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")
    something = Quiz()
    root.mainloop()
