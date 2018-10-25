import csv
from tkinter import *
from tkinter.filedialog import askopenfilename
import sys


def open_file():
    root = Tk()
    root.filename = askopenfilename()
    root.withdraw()
    if not root.filename:
        sys.exit()
    else:
        return root.filename


def get_csv_data():
    while True:
        try:
            while True:
                file_name = open_file()
                if not file_name.endswith('.csv'):
                    print('The file chosen is not in a csv format!')
                else:
                    break
            text = []
            file_save = []
            with open(file_name, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    file_save.append(row[0])
                    text.append([row[1], row[2]])
        except IndexError:
            print('File was not in correct format!')
        else:
            return file_save, text
