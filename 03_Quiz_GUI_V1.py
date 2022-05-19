"""
03_Quiz_GUI_V1:
Created a test window with button to
start the main quiz gui.

"""

# Import the required libraries
import tkinter
from tkinter import *
import tkinter.ttk as ttk
# Import Pillow for Images Manipulation
import PIL.Image
from PIL import ImageTk

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
    print("Start demo. This action will start the main quiz.")
    # Deleting Start_gui window.
    test_window.destroy()
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
    watermark = ImageTk.PhotoImage(PIL.Image.open("MaoriWarrior1.png"))
    image2 = Label(quiz_frame, image=watermark)
    image2.place(x=450, y=200, relwidth=1, relheight=1)
    m_quiz.mainloop()


# Create a button to close the window
Button(frame, text="Start Quiz", font=('Helvetica bold', 10), command=start_quiz).pack(pady=20)

test_window.mainloop()