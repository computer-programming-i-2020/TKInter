'''
Created on Jun 21, 2019

@author: karl
'''

import tkinter as tk
from tkinter import filedialog as fd

root = tk.Tk()

root.title("File Finder")
root.geometry("500x250")

myLabel = tk.Label(root, text="", font=30)
myLabel.pack()

listbox = tk.Listbox(root)
listbox.pack()
listbox.config(width=60)

def buttonAction():
    listbox.insert(tk.END, fd.askopenfilename())

myButton = tk.Button(root, text="Find File", command=buttonAction)
myButton.pack()
myButton.config(width=50)

root.mainloop()