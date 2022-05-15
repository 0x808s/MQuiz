from tkinter import *
# import functols
from functools import partial


# Base plate for testing the button for Help GUI
class Quiz:
    def __init__(self):
        print("Help GUI Loaded")

        # formatting var
        background_color = "grey"

        # Converter Main Screen GUI
        self.quiz_frame = Frame(width=600, height=600,
                                     bg=background_color, pady=10)
        self.quiz_frame.grid()
        # Heading Title in window
        self.temp_converter_label = Label(self.quiz_frame, text="Maori Quiz",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)
        # Help Button (row 1)
        self.help_button = Button(self.quiz_frame, text="Help",
                                  font=("Arial", "14"),
                                  padx=15, pady=15,
                                  command=self.helpquiz)
        self.help_button.grid(row=1)

    def helpquiz(self):
        print("you asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="HelpText")


class Help:
    def __init__(self, partner):
        background = "grey"
        # Disable help
        partner.help_button.config(state=DISABLED)
        # Sets up child window
        self.help_box = Toplevel()

        # GUI FRAME
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # Help heading
        self.how_heading = Label(self.help_frame, text="Help/instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Help Text
        self.help_text = Label(self.help_frame, text="", justify=LEFT,
                               width=40, bg=background, wrap=25)
        self.help_text.grid(row=1)

        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Dismiss
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="orange", font="arial 10 bold",
                                  command=partial(self.close_help, partner))

    def close_help(self, partner):
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Help GUI Component Tester")
    something = Quiz()
    root.mainloop()
