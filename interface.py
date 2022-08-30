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
    # Changes weather labels (make function pass in a var for the label that it should be changing)
    wList = getWeather(location)
    print(wList)

    # Location Labels
    tempLabel1.config(text = "Temperature: " + str(wList[0])+' C')
    flLabel1.config(text="Feels Like: " + str(wList[1]) + ' C')
    tempMinLabel1.config(text="Min Temperature: " + str(wList[2]) + ' C')
    tempMaxLabel1.config(text="Max Temperature: " + str(wList[3]) + ' C')
    pressureLabel1.config(text="Pressure: " + str(wList[4]) + " hPa")
    humidityLabel1.config(text="Humidity: " + str(wList[5]) + " %")

# SUBMIT BUTTON
submit_btn1 = Button(root, text="SUBMIT", command=lambda: submit(entry1.get()))
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

pressureLabel1 = Label(root, text="Pressure: ")
pressureLabel1.grid(row=5, column=0)

humidityLabel1 = Label(root, text="Humidity: ")
humidityLabel1.grid(row=6, column=0)


mainloop()