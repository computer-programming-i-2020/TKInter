'''
Created on Jun 20, 2019

@author: karl
'''

import tkinter as tk
import cv2 as cv
from PIL import Image, ImageTk

def main():
    root = tk.Tk()
    root.title("My GUI")
    root.geometry("1000x1000")
    
    tkFrame = tk.Frame(root)
    tkFrame.pack()
    
    camera = CameraFeed(0)
    
    myGUI = GUI(root, camera.getImage())
    
    while True:
        myGUI.displayImage(camera.getImage())
        root.update()

class GUI:
    def __init__(self, master, img):
        def hideVideo():
            self.myLabel.pack_forget()
            
        def showVideo():
            self.myLabel.pack(side=tk.constants.TOP)
        
        tkFrame = tk.Frame(master)
        tkFrame.pack(side=tk.TOP)
        
        self.myLabel = tk.Label(master, image=img)
        self.myLabel.pack(in_=master, side=tk.TOP)
        
        self.myButton = tk.Button(master, text="Hide", font=60, command=hideVideo, )
        self.myButton.pack(in_=tkFrame, side=tk.LEFT, fill=tk.BOTH)
        
        self.myButton2 = tk.Button(master, text="Show", font=60, command=showVideo)
        self.myButton2.pack(in_=tkFrame, side=tk.LEFT, fill=tk.BOTH)
        
    def displayImage(self, img):
        self.myLabel.config(image=img)

class CameraFeed:
    def __init__(self, cameraNumber):
        self.cap = cv.VideoCapture(cameraNumber)
    
    def getImage(self):
        _, frame = self.cap.read()
        self.image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        self.image = Image.fromarray(self.image)
        self.image = ImageTk.PhotoImage(self.image)
        return self.image

if __name__ == "__main__":
    main()