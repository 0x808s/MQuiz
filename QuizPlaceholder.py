"""
QuizPlaceholder:
This file is used to demonstrate my
method of creating the Main Quiz GUI
for 03_Quiz_GUI_V(x)

"""

# Import the required libraries
import tkinter
from tkinter import *
import tkinter.ttk as ttk
# Import Pillow for Images Manipulation
import PIL.Image
from PIL import ImageTk
# importing json for questions
import json


def quiz_start():
    # Making new window containing quiz.
    m_quiz = Tk()
    # Import Azure theme
    m_quiz.call("source", "azure.tcl")
    m_quiz.call("set_theme", "dark")
    # Naming Window
    m_quiz.title("Basic Beginner Maori Quiz")
    # Setting size and start location
    m_quiz.geometry("1000x600+400+150")
    m_quiz.resizable(False, False)
    quiz_frame = Frame(m_quiz)
    quiz_frame.pack(fill=BOTH, expand=YES)
    # Render Watermark
    watermark = ImageTk.PhotoImage(PIL.Image.open("MaoriWarrior1.png"))
    image2 = Label(quiz_frame, image=watermark)
    image2.place(x=450, y=200, relwidth=1, relheight=1)
    quiz_title = Label(quiz_frame, text="Māori Quiz",
                       font=("Proggy", "24", "bold"))
    quiz_title.place(x=400, y=0)

    m_quiz.mainloop()
