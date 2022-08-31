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
my_label1.grid(row=0, column=0, rowspan=8, columnspan=7)

image2 = resizeImg("images/2.png")
my_img2 = ImageTk.PhotoImage(image2)
my_label2 = Label(image=my_img2)
my_label2.grid(row=0, column=8, rowspan=8, columnspan=7)

image3 = resizeImg("images/3.png")
my_img3 = ImageTk.PhotoImage(image3)
my_label3 = Label(image=my_img3)
my_label3.grid(row=9, column=0, rowspan=8, columnspan=7)

image4 = resizeImg("images/4.png")
my_img4 = ImageTk.PhotoImage(image4)
my_label4 = Label(image=my_img4)
my_label4.grid(row=9, column=8, rowspan=8, columnspan=7)

# ENTRY BOXES

entry1 = Entry(root, width = "30")
entry1.grid(row=0, column=0, columnspan=7)

entry2 = Entry(root, width = "30")
entry2.grid(row=0, column=8, columnspan=7)

entry3 = Entry(root, width = "30")
entry3.grid(row=9, column=0, columnspan=7)

entry4 = Entry(root, width = "30")
entry4.grid(row=9, column=8, columnspan=7)

def submit(location, temp, feels_like, temp_min, temp_max, pressure, humidity):
    # Changes weather labels (make function pass in a var for the label that it should be changing)
    wList = getWeather(location)

    # Location Labels
    temp.config(text = "Temperature: " + str(wList[0])+' C')
    feels_like.config(text="Feels Like: " + str(wList[1]) + ' C')
    temp_min.config(text="Min Temperature: " + str(wList[2]) + ' C')
    temp_max.config(text="Max Temperature: " + str(wList[3]) + ' C')
    pressure.config(text="Pressure: " + str(wList[4]) + " hPa")
    humidity.config(text="Humidity: " + str(wList[5]) + " %")


# SUBMIT BUTTONS
submit_btn1 = Button(root, text="SUBMIT", command=lambda: submit(entry1.get(), tempLabel1, flLabel1, tempMinLabel1, tempMaxLabel1, pressureLabel1, humidityLabel1))
submit_btn1.grid(row=7, column=1)

submit_btn2 = Button(root, text="SUBMIT", command=lambda: submit(entry2.get(), tempLabel2, flLabel2, tempMinLabel2, tempMaxLabel2, pressureLabel2, humidityLabel2))
submit_btn2.grid(row=7, column=9)

submit_btn3 = Button(root, text="SUBMIT", command=lambda: submit(entry3.get(), tempLabel3, flLabel3, tempMinLabel3, tempMaxLabel3, pressureLabel3, humidityLabel3))
submit_btn3.grid(row=16, column=1)

submit_btn4 = Button(root, text="SUBMIT", command=lambda: submit(entry4.get(), tempLabel4, flLabel4, tempMinLabel4, tempMaxLabel4, pressureLabel4, humidityLabel4))
submit_btn4.grid(row=16, column=9)

# Text Labels
# ------------------Top Left----------------------------
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

# ------------------Top Right----------------------------
tempLabel2 = Label(root, text="Temperature: ")
tempLabel2.grid(row=1, column=8)

flLabel2 = Label(root, text="Feels Like: ")
flLabel2.grid(row=2, column=8)

tempMinLabel2 = Label(root, text="Min Temperature: ")
tempMinLabel2.grid(row=3, column=8)

tempMaxLabel2 = Label(root, text="Max Temperature: ")
tempMaxLabel2.grid(row=4, column=8)

pressureLabel2 = Label(root, text="Pressure: ")
pressureLabel2.grid(row=5, column=8)

humidityLabel2 = Label(root, text="Humidity: ")
humidityLabel2.grid(row=6, column=8)

# ------------------Bottom Left----------------------------
tempLabel3 = Label(root, text="Temperature: ")
tempLabel3.grid(row=10, column=0)

flLabel3 = Label(root, text="Feels Like: ")
flLabel3.grid(row=11, column=0)

tempMinLabel3 = Label(root, text="Min Temperature: ")
tempMinLabel3.grid(row=12, column=0)

tempMaxLabel3 = Label(root, text="Max Temperature: ")
tempMaxLabel3.grid(row=13, column=0)

pressureLabel3 = Label(root, text="Pressure: ")
pressureLabel3.grid(row=14, column=0)

humidityLabel3 = Label(root, text="Humidity: ")
humidityLabel3.grid(row=15, column=0)

# ------------------Bottom Right----------------------------
tempLabel4 = Label(root, text="Temperature: ")
tempLabel4.grid(row=10, column=8)

flLabel4 = Label(root, text="Feels Like: ")
flLabel4.grid(row=11, column=8)

tempMinLabel4 = Label(root, text="Min Temperature: ")
tempMinLabel4.grid(row=12, column=8)

tempMaxLabel4 = Label(root, text="Max Temperature: ")
tempMaxLabel4.grid(row=13, column=8)

pressureLabel4 = Label(root, text="Pressure: ")
pressureLabel4.grid(row=14, column=8)

humidityLabel4 = Label(root, text="Humidity: ")
humidityLabel4.grid(row=15, column=8)

mainloop()