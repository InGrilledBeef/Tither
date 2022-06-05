# Date: 2022-06-04
# Author: Ingrid Qin

from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
from tkinter import messagebox

# Start Window
root = Tk()
root.title("Tither")
root.resizable(False, False)


def resizeImg(path):
    image = Image.open(path)
    image = image.resize((270, 360), Image.ANTIALIAS)
    return image

# Importing Backgrounds
image1 = resizeImg("images/1.png")
my_img1 = ImageTk.PhotoImage(image1)
my_label1 = Label(image=my_img1)
my_label1.grid(row=0, column=0, columnspan=7, rowspan=8)

'''
image2 = resizeImg("images/2.png")
my_img2 = ImageTk.PhotoImage(image2)
my_label2 = Label(image=my_img2)
my_label2.grid(row=0, column=1)

image3 = resizeImg("images/3.png")
my_img3 = ImageTk.PhotoImage(image3)
my_label3 = Label(image=my_img3)
my_label3.grid(row=1, column=0)

image4 = resizeImg("images/4.png")
my_img4 = ImageTk.PhotoImage(image4)
my_label4 = Label(image=my_img4)
my_label4.grid(row=1, column=1)
'''

# ENTRY BOXES
entry1 = Entry(root, width = "30")
entry1.grid(row=0, column=3, columnspan=4)

'''
entry2 = Entry(root, width = "50")
entry2.grid(row=0, column=1)

entry3 = Entry(root, width = "50")
entry3.grid(row=1, column=0)

entry4 = Entry(root, width = "50")
entry4.grid(row=1, column=1)
'''

# Text
titleLabel = Label(root, text="AGE CALCULATOR APP")
titleLabel.grid(row=1, column=2)

yearLabel = Label(root, text="What year were you born? (e.g. 1876, 1999, 2004, etc) ")
yearLabel.grid(row=2, column=1)

monthLabel = Label(root, text="What month were you born? (e.g. January, March, July, etc) ")
monthLabel.grid(row=3, column=1)

dayLabel = Label(root, text="What day were you born? (e.g. 1, 5, 16, 31, etc) ")
dayLabel.grid(row=4, column=1)

mainloop()