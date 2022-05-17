"""
00_GUI_framework:
Basic Template for tkinter Window.
"""
from tkinter import *


class Foo:
    def __init__(self, parent):
        print("hello")


if __name__ == "__main__":
    root = Tk()
    root.title("title goes here")
    something = Foo(root)
    root.mainloop()