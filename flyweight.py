# Flyweight module
# This module serves as cache for the widgets that
# already instantiated/made when the app.py runs.
# Main purpose is to lessen the memory usage for
# the run of the application.

# Import needed modules
from builder import *

# Import needed libraries
import tkinter as tk

# Flyweight class
class Flyweight:
    # Container of labels
    __labels = {}

    # Container of frames
    __frames = {}

    # Function that gets the labels
    @staticmethod
    def get_label(name, text, root=None):
        if name not in Flyweight.__labels:
            Flyweight.__labels[name] = BuildLabel(root).set_text(text).build()

        return Flyweight.__labels[name]

    # Function that gets the frames
    @staticmethod
    def get_frame(name, root=None):
        if name not in Flyweight.__frames:
            Flyweight.__frames[name] = BuildFrame(root).build()

        return Flyweight.__frames[name]
