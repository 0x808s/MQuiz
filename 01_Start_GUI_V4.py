"""
01_Start_GUI_V4:
Changed Title Labels to make it fit the social implication,
added the Instruction text.
added help button to further help users navigate program.
"""

# Import gui library (tkinter)
import tkinter
from tkinter import *
import tkinter.ttk as ttk
import PIL.ImageTk, PIL.Image


# Start Quiz Placeholder function
def start_quiz():
    print("Start demo. This action will start the main quiz.")


# Quit Quiz Function
def quit_quiz():
    print("Terminated Quiz")
    exit()


# Help function placeholder
def help_quiz():
    print("Help placeholder / Start help GUI")


# Main GUI Start
class Quiz:
    def __init__(self):
        # Formatting Variables
        print("Quiz Loaded")

        # Quiz start GUI
        self.quiz_frame = Frame(width=500, height=500)
        self.quiz_frame.grid()
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
        self.start_button = ttk.Button(root, text="Start Quiz",
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
        img = PIL.ImageTk.PhotoImage(PIL.Image.open("MaoriWarrior1.png"))
        self.image = ttk.Label(root, image=img)
        self.image.place(x=100, y=100)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Basic Beginner Maori Quiz")
    root.geometry("500x500")
    # Importing Azure theme for tkinter (dark)
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")
    something = Quiz()
    root.mainloop()
