"""
04_Quiz_V1:
Main Quiz.
Created GUI and used JSON file as source
of questions and answers.
Error after completing final question, needs to
be fixed in V2.
Doesn't Show final score need to add in V2.

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
with open('QnA.JSON') as x:
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
        # Question number and The Questions
        self.question_number = 0
        self.question = self.question(self.question_number)
        # Radio Buttons for selection
        self.option_selected = IntVar()
        self.options = self.radio_btn()
        self.display_options(self.question_number)
        # Buttons for navigating quiz
        self.quiz_buttons()
        self.correct_ans = 0

    # Display questions
    def question(self, question_number):
        question_number = Label(m_quiz, text=questions[question_number],
                                font=("Proggy", 16, "bold"), anchor="center")
        question_number.place(x=350, y=120)
        return question_number

    # Radio buttons for selecting answers
    def radio_btn(self):
        quiz_value = 0
        opt_list = []
        # Dynamic Y position for radio button locations.
        y_pos = 200
        while quiz_value < 4:
            btns = ttk.Radiobutton(m_quiz, text="", variable=self.option_selected,
                                   value=quiz_value + 1)
            opt_list.append(btns)
            btns.place(x=300, y=y_pos)
            quiz_value += 1
            y_pos += 40
        return opt_list

    # Display options available
    def display_options(self, question_number):
        quiz_value = 0
        self.option_selected.set(0)
        self.question['text'] = questions[question_number]
        # For loop
        for op in options[question_number]:
            self.options[quiz_value]['text'] = op
            quiz_value += 1

    # Buttons (next, Quit)
    def quiz_buttons(self):
        next_button = ttk.Button(m_quiz, text="Next Question",
                                 command=self.next_function)
        next_button.place(x=670, y=500)
        quit_button = ttk.Button(m_quiz, text='Quit Quiz',
                                 command=m_quiz.destroy)
        quit_button.place(x=200, y=500)

    # Placeholder answer check
    def check_ans(self, question_number):
        if self.option_selected.get() == answers[question_number]:
            return True

    # Navigate to next question
    def next_function(self):
        if self.check_ans(self.question_number):
            self.correct_ans += 1
        self.question_number += 1
        self.display_options(self.question_number)


quiz = MaoriQuiz()
m_quiz.mainloop()
