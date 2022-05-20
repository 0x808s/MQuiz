"""Compiled Code"""

# Import gui library (tkinter)
import tkinter
from tkinter import *
import tkinter.ttk as ttk
# Import Pillow for Images Manipulation
import PIL.Image
from PIL import ImageTk
# Import JSON
import json
# Import Quiz File
from Quiz_Placeholder_V2 import *
from functools import partial


# Main GUI Start
class Quiz:
    def __init__(self, start_gui):
        # Help function
        def help_quiz():
            print("you asked for help")
            get_help = Help(self)
            get_help.help_text.configure(text="HelpText")

        # Quit Quiz Function
        def quit_quiz():
            print("Terminated Quiz")
            exit()

        # Start Quiz
        def start_quiz():
            print("Loaded Quiz")
            start_gui.destroy()
            quiz_start()

        gui_picture = ImageTk.PhotoImage(PIL.Image.open("MaoriWarrior1.png"))

        # Formatting Variables
        print("Quiz Loaded")

        # Quiz start GUI
        self.quiz_frame = Frame(width=500, height=500)
        self.quiz_frame.grid()
        # Adding Image
        image1 = Label(start_gui, image=gui_picture)
        image1.place(x=0, y=25, relwidth=1, relheight=1)
        # Show Image Layer
        image1.photo = gui_picture

        # Quiz title main (Maori Quiz)
        self.quiz_label = Label(text="Simple Māori Quiz!",
                                font=("Arial", "16", "bold"))
        self.quiz_label.place(x=150, y=30)
        # Introduction text
        self.introduction_label = ttk.Label(text="Kia Ora, Hello!, this is a simple quiz to help you learn"
                                                 " Basic Te Reo Māori.\n"
                                                 "To get started, please select the 'Start Quiz' button."
                                                 " Or use 'Quit Quiz' \n"
                                                 "to exit the program. Select 'Help' to receive more instructions.")
        self.introduction_label.place(x=20, y=100)
        # Start Button
        self.start_button = ttk.Button(start_gui, text="Start Quiz",
                                       command=start_quiz)

        # Start Button location
        self.start_button.place(x=375, y=400)
        # Quit Button
        self.quit_button = ttk.Button(text="Quit Quiz",
                                      command=quit_quiz)
        # Quit button location
        self.quit_button.place(x=35, y=400)

        # Help button
        self.help_button = ttk.Button(text="Help",
                                      command=help_quiz)
        self.help_button.place(x=140, y=400)


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
    start_gui = Tk()
    # name of window
    start_gui.title("Basic Beginner Maori Quiz")
    # size of window
    start_gui.geometry("500x500")
    start_gui.resizable(False, False)
    # Importing Azure theme for tkinter (dark)
    start_gui.tk.call("source", "azure.tcl")
    start_gui.tk.call("set_theme", "dark")
    Quiz(start_gui)
    start_gui.mainloop()
