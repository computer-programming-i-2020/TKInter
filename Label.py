'''
Created on Jun 20, 2019

@author: karl
'''

#The next line imports a library called tkinter which is used to make GUIs
import tkinter as tk

#This creates an object for the window on our application
root = tk.Tk()

#This sets some of the parameters of our window
root.title("My GUI")
root.geometry("500x500")

#This creates a label object, sets some parameters, and sets a target window (root).
myLabel = tk.Label(root, text="Hello World", font=30)

#Adds the label to the window
myLabel.pack()

#Starts the looping application for the GUI
root.mainloop()