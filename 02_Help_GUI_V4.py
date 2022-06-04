"""
02_Help_GUI_V4:
Final Help menu with
full help text.
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
        get_help.help_text.configure(text="First time playing? \n"
                                          "These instructions may help!\n"
                                          "Press the 'Start button' to start the quiz.\n"
                                          "Press the 'Quit' button anytime to quit the quiz.\n"
                                          "In the quiz, Press 'Next question' to proceed.\n"
                                          "In the result menu, press the 'export' button\n"
                                          "to export your results.\n"
                                          "\n"
                                          "\n"
                                          "Have fun!")


class Help:
    def __init__(self, partner):
        # Disable help
        partner.help_button.config(state=DISABLED)
        # Sets up child window
        self.help_box = Toplevel()
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))
        # GUI FRAME
        self.help_frame = Frame(self.help_box, width=300, height=900)
        self.help_frame.grid()

        # Help heading
        self.how_heading = Label(self.help_frame, text="Help menu",
                                 font="arial 10 bold")
        self.how_heading.grid(row=0)

        # Help Text
        self.help_text = Label(self.help_frame, text="", justify=LEFT,
                               width=40)
        self.help_text.grid(row=1)

        # Dismiss button
        self.dismiss_btn = ttk.Button(self.help_frame, text="OK, Got it.",
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
