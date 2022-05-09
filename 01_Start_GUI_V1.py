# Import gui library
from tkinter import *


class Quiz:
    def __init__(self):
        # Formatting Variables
        print("Quiz Loaded")
        background_color = "white"
        # Quiz start GUI
        self.quiz_frame = Frame(width=500, height=500, bg=background_color)
        self.quiz_frame.grid()
        self.quiz_label = Label(text="Maori Quiz",
                                font=("Arial", "16", "bold"),
                                bg=background_color,
                                padx=10, pady=10)
        self.quiz_label.grid(row=0)
        # Start Button
        self.start_button = Button(text="Start Quiz",
                                   font=("Arial", "14"),
                                   padx=10, pady=10,
                                   command=self.startquiz)
        self.start_button.grid(row=1)

    # Test if button works
    def startquiz(self):
        print("start")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Quiz")
    something = Quiz()
    root.mainloop()
