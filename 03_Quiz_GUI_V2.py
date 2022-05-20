"""
03_Quiz_GUI_V2:
Using a more efficient way of
running the Main Quiz.

"""
# Import the required libraries
import tkinter
from tkinter import *
import tkinter.ttk as ttk
# Import Pillow for Images Manipulation
import PIL.Image
from PIL import ImageTk
# Import Json
import json
# Import My other Python file QuizPlaceholder
# Contains Function for the main quiz.
from QuizPlaceholder import *

# Create an instance of tkinter frame
test_window = Tk()
test_window.title("Main Quiz Launcher")

# Set the geometry of test frame
test_window.geometry("600x250")

# Create a frame
frame = Frame(test_window)
frame.pack(side="top", expand=True, fill="both")

# Create a text label
Label(frame, text="MAIN QUIZ TESTER", font=('Helvetica', 20)).pack(pady=20)


def start_quiz():
    test_window.destroy()
    # This is from the QuizPlaceholder file
    quiz_start()


# Create a button to close the window
Button(frame, text="Start Quiz", font=('Helvetica bold', 10), command=start_quiz).pack(pady=20)

test_window.mainloop()
