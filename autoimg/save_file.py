from tkinter import *
from tkinter import filedialog

def save_file():
    root = Tk()
    root.filename = filedialog.askdirectory()
    root.withdraw()
    return root.filename