
# Import gui library (tkinter)
from tkinter import *
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
        self.introduction_label = ttk.Label(text="Example introduction text")
        self.introduction_label.place(x=170, y=100)
        # Start Button
        self.start_button = ttk.Button(root, text="Start Quiz",
                                       command=self.startquiz)

        # Start Button location
        self.start_button.place(x=375, y=400)
        # Quit Button
        self.quit_button = ttk.Button(text="Quit Quiz",
                                      command=self.quitquiz)
        # Quit button location
        self.quit_button.place(x=35, y=400)

        # Help button
        self.help_button = ttk.Button(text="Help",
                                      command=self.helpquiz)
        self.help_button.place(x=140, y=400)

    # Test if button works
    def startquiz(self):
        print("Start demo. This action will start the main quiz.")

    # Test if quit button works
    def quitquiz(self):
        print("Terminated Quiz")
        exit()
    # Help Command / Function
    def helpquiz(self):
        print("Help placeholder")



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Basic Beginner Maori Quiz")
    # Importing Azure theme for tkinter (dark)
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")
    something = Quiz()
    root.mainloop()
