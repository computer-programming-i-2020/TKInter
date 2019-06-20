'''
Created on Jun 20, 2019

@author: karl
'''

import tkinter as tk

root = tk.Tk()

root.title("My GUI")
root.geometry("500x500")

myLabel = tk.Label(root, text="Hello World", font=30)
myLabel.pack()

def buttonAction():
    myLabel.config(text="Pressed")

myButton = tk.Button(root, text="Press Me", command=buttonAction)
myButton.pack()

root.mainloop()