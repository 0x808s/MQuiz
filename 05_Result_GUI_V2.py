"""
05_Results_GUI_V2:
Added export button for users
to export their results.
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
from tkinter import messagebox
from tkinter import filedialog

# Score calculation placeholder
score = 70
result = str(score) + "%"
correct = 7
wrong = 3


# Result GUI
def get_result():
    m_quiz.destroy()
    r_gui = Tk()
    print("Get results")
    # Import Azure theme
    r_gui.call("source", "azure.tcl")
    r_gui.call("set_theme", "dark")
    # Naming Window
    r_gui.title("Basic Beginner Maori Quiz")
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
    r_title = Label(r_frame, text="Final Results",
                    font=("Proggy", "16", "bold"))
    r_title.place(x=180, y=0)
    # Labels for displaying user score
    r_score = Label(r_frame, text=f"Score: {result}")
    r_score.place(x=100, y=50)
    # Export button
    r_export = ttk.Button(r_frame, text="Export",
                          command=export_result)
    r_export.place(x=100, y=400)
    r_gui.mainloop()


# Export func
def export_result():
    filename = filedialog.asksaveasfilename(initialdir='/desktop',
                                            title='Save File',
                                            defaultextension=".txt")
    my_file = open(filename, "w+", encoding="utf-8")
    my_file.write(f"Results: {result, correct, wrong}")


# Main Quiz Placeholder
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
quiz_title = Label(quiz_frame, text="Māori Quiz Placeholder",
                   font=("Proggy", "24", "bold"))
quiz_title.place(x=330, y=0)
# Results button
result_btn = ttk.Button(quiz_frame, text="Get Results",
                        command=get_result)
result_btn.place(x=430, y=300)

m_quiz.mainloop()
