# Import the required libraries
import tkinter
from tkinter import *
import tkinter.ttk as ttk
# Import Pillow for Images Manipulation
import PIL.Image
from PIL import ImageTk
# importing json for questions
import json

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
# JSON open
with open('questionsJSON.JSON') as x:
    obj = json.load(x)
questions = (obj['questions'])
options = (obj['options'])
answers = (obj['answers'])
# Test if loaded
print(questions)
print(options)
print(answers)


# Make quiz class
class MaoriQuiz:
    def __init__(self):
        self.question_number = 0
        self.question = self.question(self.question_number)

    def question(self, question_number):
        question_number = Label(m_quiz, text=questions[question_number],
                                font=("Proggy", 16, "bold"), anchor="center")
        question_number.place(x=350, y=120)
        return question_number


quiz = MaoriQuiz()
m_quiz.mainloop()
