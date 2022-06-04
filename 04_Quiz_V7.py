"""
04_Quiz_V7:
Adding dynamic question numbers
to questions so users can see
what q number they are up to.
"""

# Import the required libraries
import tkinter
from tkinter import *
import tkinter.ttk as ttk
# Import Pillow for Images Manipulation
import PIL.Image
from PIL import ImageTk
# Importing json for questions
import json
# Import File Dialog for exports
from tkinter import filedialog
# Import random for question randomizer
import random


# Make quiz class
class MaoriQuiz:
    def __init__(self):
        # Question number and The Questions
        self.question_number = 0
        # Quiz number in V7 showing users what q they are on
        self.quiz_number = 1
        # Quiz number string for label.
        self.quiz_str = StringVar()
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
        self.quiz_str.set(str(self.quiz_number)+". "+questions[question_number])
        # Changed to get question numbers on each question.
        question_number = Label(m_quiz, textvariable=self.quiz_str,
                                font=("Proggy", 16, "bold"), anchor="center")
        question_number.place(x=350, y=120)
        return question_number

    # Radio buttons for selecting answers
    def radio_btn(self):
        quiz_value = 0
        # Option list
        opt_list = []
        # Dynamic Y position for radio button locations.
        y_pos = 200
        # Whileloop for Ans
        while quiz_value < 4:
            btns = ttk.Radiobutton(m_quiz, text="",
                                   variable=self.option_selected,
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
        self.quiz_number += 1

        if self.question_number == len(questions):
            self.display_result()
        else:
            self.quiz_str.set(str(self.quiz_number)+". "+questions[self.question_number])
            self.display_options(self.question_number)

    # Export Results in Result GUI instead

    # Display results fix
    def display_result(self):
        # Show results in separate GUI
        self.get_result()

    # Result GUI
    def get_result(self):
        m_quiz.destroy()
        # Score calculation
        score = int(self.correct_ans / len(questions) * 100)
        result = "Final Results: " + str(score) + "%"
        wrong_ans = len(questions) - self.correct_ans
        correct = "Correct Answers: " + str(self.correct_ans)
        wrong = "Wrong Answers: " + str(wrong_ans)
        r_gui = Tk()
        print("Get results")
        # Import Azure theme
        r_gui.call("source", "azure.tcl")
        r_gui.call("set_theme", "dark")
        # Naming Window
        r_gui.title("Result Screen")
        # Setting size and start location (Optimized for my laptop)
        # Laptop resolution: 1368x780
        r_gui.geometry("500x600+200+50")
        r_gui.resizable(False, False)
        r_frame = Frame(r_gui)
        r_frame.pack(fill=BOTH, expand=YES)
        # Render Watermark
        watermark2 = ImageTk.PhotoImage(PIL.Image.open("MaoriWarrior1.png"))
        image3 = Label(r_frame, image=watermark2)
        image3.place(x=150, y=200, relwidth=1, relheight=1)
        r_title = Label(r_frame, text="Final Results (PLACEHOLDER)",
                        font=("Proggy", "16", "bold"))
        r_title.place(x=100, y=0)
        # Labels for displaying user score
        r_score = Label(r_frame, text="Score: xxx(placeholder)")
        r_score.place(x=100, y=50)
        # Export Btn
        r_export = ttk.Button(r_frame, text="Export",
                              command=self.export_result)
        r_export.place(x=100, y=400)
        r_gui.mainloop()

    # Export Results Function
    def export_result(self):
        score = int(self.correct_ans / len(questions) * 100)
        result = "Final Results: " + str(score) + "%"
        wrong_ans = len(questions) - self.correct_ans
        correct = "Correct Answers: " + str(self.correct_ans)
        wrong = "Wrong Answers: " + str(wrong_ans)
        filename = filedialog.asksaveasfilename(initialdir='/desktop',
                                                title='Save File',
                                                defaultextension=".txt")
        my_file = open(filename, "w+", encoding="utf-8")
        my_file.write(f"Results: {result, correct, wrong}")


m_quiz = Tk()
# Import Azure theme
m_quiz.call("source", "azure.tcl")
m_quiz.call("set_theme", "dark")
# Naming Window
m_quiz.title("Basic Beginner Maori Quiz")
# Setting size and start location (Optimized for my laptop)
# Laptop resolution: 1368x780
m_quiz.geometry("1000x600+200+50")
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
with open('QnA_Randomized.JSON') as x:
    obj = json.load(x)
questions = (obj['questions'])
options = (obj['options'])
answers = (obj['answers'])
# Combine lists to randomize properly
zipper = zip(questions, answers, options)
quiz_list = list(zipper)
random.shuffle(quiz_list)
questions, answers, options = zip(*quiz_list)
# DEBUGGER (Deleted later)
print(questions)
print(options)
print(answers)

quiz = MaoriQuiz()
m_quiz.mainloop()
