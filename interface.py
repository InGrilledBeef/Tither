# Date: 2022-06-04
# Author: Ingrid Qin

import sys
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
from tkinter import messagebox
from src.weather import *

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
entry1.grid(row=0, column=0, columnspan=7)

'''
entry2 = Entry(root, width = "50")
entry2.grid(row=0, column=1)

entry3 = Entry(root, width = "50")
entry3.grid(row=1, column=0)

entry4 = Entry(root, width = "50")
entry4.grid(row=1, column=1)
'''

def submit(location):
    print(location)
    #wList = getWeather(str(location))

    # Location Labels
    #tempLabel1 = Label(root, text=str(wList[0]))
    #tempLabel1.grid(row=1, column=5)

    '''
    flLabel1 = Label(root, text=str(wList[1]))
    flLabel1.grid(row=2, column=5)

    tempMinLabel1 = Label(root, text=str(wList[2]))
    tempMinLabel1.grid(row=3, column=5)

    tempMaxLabel1 = Label(root, text=str(wList[3]))
    tempMaxLabel1.grid(row=4, column=5)

    pressureLabel = Label(root, text=str(wList[4]))
    pressureLabel.grid(row=5, column=5)

    humidityLabel = Label(root, text=str(wList[5]))
    humidityLabel.grid(row=6, column=5)
    '''
    #return wList

# SUBMIT BUTTON
submit_btn1 = Button(root, text="SUBMIT", command=lambda: submit(entry1))
submit_btn1.grid(row=8, column=3)

# Text Labels
tempLabel1 = Label(root, text="Temperature: ")
tempLabel1.grid(row=1, column=0)

flLabel1 = Label(root, text="Feels Like: ")
flLabel1.grid(row=2, column=0)

tempMinLabel1 = Label(root, text="Min Temperature: ")
tempMinLabel1.grid(row=3, column=0)

tempMaxLabel1 = Label(root, text="Max Temperature: ")
tempMaxLabel1.grid(row=4, column=0)

pressureLabel = Label(root, text="Pressure: ")
pressureLabel.grid(row=5, column=0)

humidityLabel = Label(root, text="Humidity: ")
humidityLabel.grid(row=6, column=0)


mainloop()