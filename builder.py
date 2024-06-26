# Builder Module
# This module serves as the builder for the
# widgets used in the application.
# It's purpose it to implement the
# dry methodology in programming.

# Import needed libraries
import tkinter as tk 

# Builder class for the label
class BuildLabel(tk.Label):
    # Make a constructor for the class 
    def __init__(self, root) -> None:
        self.root = root
        self.label = None

    # Function that sets text to the label
    def set_text(self, text):
        self.text = text
        return self

    # Function that builds the Label
    def build(self):
        self.label = tk.Label(self.root, text=self.text)
        self.label.pack()
        return self.label

class BuildFrame(tk.Frame):
    # Make a consturctor
    def __init__(self, root) -> None:
        self.root = root
        self.frame = None

    # Function that builds the frame
    def build(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        return self.frame