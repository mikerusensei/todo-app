# Import modules
from flyweight import Flyweight

# Import libraries
import tkinter as tk

# Make class for the app
class App(tk.Tk):
    # Make constructor of the tk app
    def __init__(self) -> None:
        super().__init__()

        # Add the configure function
        self.__configure()

        # Add the add_frame function
        self.__add_frames()

        # Add the add_labels function
        self.__add_labels()

        # Add the run function
        self.run()

    # Make a function that configures the window
    def __configure(self) -> None:
        self.title("Todo Application")
        self.geometry("500x500")

    # Function that adds frames 
    def __add_frames(self) -> None:
        frame_configuration = [
            {"name": "self.main_frame", "root": self}
        ]

        for config in frame_configuration:
            Flyweight.get_frame(config["name"], config["root"])

    # Function that adds labels
    def __add_labels(self) -> None:

        label_configuration = [
            {"name": "label1", "text": "Hello World"},
            {"name": "label2", "text": "Hi World"},
        ]

        for config in label_configuration:
            label = Flyweight.get_label(config["name"], config["text"], self.main_frame)

    # Function that runs the app
    def run(self) -> None:
        self.mainloop()
