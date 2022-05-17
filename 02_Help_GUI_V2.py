"""
02_Help_GUI_V2:
Fixed Issue where dismiss button won't show up.
"""
from tkinter import *
# import functools
from functools import partial
# Ttk as ttk
import tkinter.ttk as ttk


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
        get_help = Help(self)
        get_help.help_text.configure(text="HelpText")


class Help:
    def __init__(self, partner):
        # Disable help
        partner.help_button.config(state=DISABLED)
        # Sets up child window
        self.help_box = Toplevel()
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))
        # GUI FRAME
        self.help_frame = Frame(self.help_box, width=300)
        self.help_frame.grid()

        # Help heading
        self.how_heading = Label(self.help_frame, text="help/instructions",
                                 font="arial 10 bold")
        self.how_heading.grid(row=0)

        # Help Text
        self.help_text = Label(self.help_frame, text="", justify=LEFT,
                               width=40)
        self.help_text.grid(row=1)

        # Dismiss button
        self.dismiss_btn = ttk.Button(self.help_frame, text="Dismiss",
                                      width=10,
                                      command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=20)

    def close_help(self, partner):
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("HELP GUI TESTER")
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")
    something = Quiz()
    root.mainloop()
