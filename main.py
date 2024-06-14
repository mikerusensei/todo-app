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
        self.__add_frame()

        # Add the run function
        self.run()

    # Make a function that configures the window
    def __configure(self) -> None:
        self.title("Todo Application")

    # Make a function that contains the frames
    def __add_frames(self) -> None:
        pass

    # Make a function to run the app
    def run(self) -> None:
        self.mainloop()
