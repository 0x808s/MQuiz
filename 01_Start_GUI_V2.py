"""
01_Start_GUI_V2
- Added Red Quit Button
"""

# Import gui library
from tkinter import *


# Main GUI Start
class Quiz:
    def __init__(self):
        # Formatting Variables
        print("Quiz Loaded")
        background_color = "white"
        # Quiz start GUI
        self.quiz_frame = Frame(width=500, height=500, bg=background_color)
        self.quiz_frame.grid()
        # Quiz title main (Maori Quiz)
        self.quiz_label = Label(text="Maori Quiz",
                                font=("Arial", "16", "bold"),
                                bg=background_color,
                                padx=10, pady=10)
        self.quiz_label.place(x=185, y=30)
        # Introduction text
        self.introduction_label = Label(text="Example introduction text",
                                        font=("Arial", "16",),
                                        bg=background_color,
                                        padx=10, pady=10, justify='center')
        self.introduction_label.place(x=120, y=100)
        # Start Button
        self.start_button = Button(text="Start Quiz",
                                   font=("Arial", "14"),
                                   padx=10, pady=10,
                                   command=self.startquiz)

        # Start Button location
        self.start_button.place(x=370, y=400)
        # Quit Button
        self.quit_button = Button(text="Quit Quiz",
                                  font=("Arial", "14",),
                                  padx=10, pady=10,
                                  bg='#fc032c',
                                  command=self.quitquiz)
        # Quit button location
        self.quit_button.place(x=10, y=400)

    # Test if button works
    def startquiz(self):
        print("Start demo. This action will start the main quiz.")

    # Test if quit button works
    def quitquiz(self):
        print("Terminated Quiz")
        exit()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Quiz")
    something = Quiz()
    root.mainloop()
