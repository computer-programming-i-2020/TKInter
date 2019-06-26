'''
Created on Jun 20, 2019

@author: karl
'''

import tkinter as tk            #Used for the GUI
from tkinter import filedialog as fd
import cv2 as cv                #Used to collect and edit camera data
from PIL import Image, ImageTk  #Used to convert image types between TKInter and OpenCV

def main():
    #Creates tk object and hides the initial window
    root = tk.Tk()
    root.withdraw()
    

    
    #Instantiates 2 VideoWindow classes for 2 different cameras
    videoWindow1 = VideoWindow(root, "VW1", 0)
    #videoWindow2 = VideoWindow(root, "VW2", 1)

    while True: #Updates the state of both windows each loop
        videoWindow1.update()
        #videoWindow2.update()

class VideoWindow:
    def __init__(self, master, windowName, cameraNumber):
        #Creates and gives attributes to a new window
        self.root = tk.Toplevel(master)
        self.root.title(windowName)
        self.root.geometry("750x550")
        
        #Creates instance of CameraFeed class connected to the camera number entered
        self.camera = CameraFeed(cameraNumber)
        
        #Creates instance of GUI class using root as a base and an image input from the camera
        self.myGUI = GUI(self.root, self.camera.getImage())
    
    def update(self):       #Updates the frame given to the GUI constant to show live camera
        self.myGUI.displayImage(self.camera.getImage())     #Gets the current frame from the camera and tell the GUI to display it
        self.root.update()                                  #Updates the window so that any new changes are displayed to the user

class GUI:
    def __init__(self, master, img):    #Runs when an instance of GUI is created. Sets up everything needed for the class to function
        def hideVideo():                #Defines a function to hide the label
            self.myLabel.pack_forget()
            
        def showVideo():                #Defines a function to show the label
            self.myLabel.pack(side=tk.constants.TOP)
            
        def saveImage():
            path = fd.asksaveasfilename(defaultextension=".png")
            cv.imwrite(path, self.savableImage)
            
        
        #Creates a frame that will hold the buttons
        tkFrame = tk.Frame(master)
        tkFrame.pack(side=tk.TOP)                   #Sets the location of the frame
        
        self.savableImage = img                             #Creates a new variables using openCV array that can be saved using openCV
        self.image = cv.cvtColor(img, cv.COLOR_BGR2RGB)     #Converts the image from BGR to RGB
        self.image = Image.fromarray(self.image)            #Converts the image to the Python Imaging Library(PIL) format
        self.image = ImageTk.PhotoImage(self.image)         #Converts the PIL format image to a format that TKInter can display
        
        #Creates the label and sets it to the initial frame
        self.myLabel = tk.Label(master, image=self.image)
        self.myLabel.pack(in_=master, side=tk.TOP) #Sets the location of the label
        
        #Creates the button used to hide the video and binds it to the hideVideo function
        self.myButton = tk.Button(master, text="Hide", font=60, command=hideVideo, )
        self.myButton.pack(in_=tkFrame, side=tk.LEFT, fill=tk.BOTH) #Sets the location of the hide button within the frame
        
        #Creates the button used to show the video and binds it to the showVideo function
        self.myButton2 = tk.Button(master, text="Show", font=60, command=showVideo)
        self.myButton2.pack(in_=tkFrame, side=tk.LEFT, fill=tk.BOTH)#Sets the location of the show button within the frame
        
        #Creates the button used to show the video and binds it to the showVideo function
        self.myButton3 = tk.Button(master, text="Take Photo", font=60, command=saveImage)
        self.myButton3.pack(in_=tkFrame, side=tk.LEFT, fill=tk.BOTH)#Sets the location of the show button within the frame
        
    def displayImage(self, img): #Defines the function used to update the frame
        self.savableImage = img                     #Creates a new variables using openCV array that can be saved using openCV
        self.image = cv.cvtColor(img, cv.COLOR_BGR2RGB)     #Converts the image from BGR to RGB
        self.image = Image.fromarray(self.image)            #Converts the image to the Python Imaging Library(PIL) format
        self.image = ImageTk.PhotoImage(self.image)         #Converts the PIL format image to a format that TKInter can display
        self.myLabel.config(image=self.image)  #Takes the parameter of an image and sets it as the image in the label

class CameraFeed:
    def __init__(self, cameraNumber):   #Runs when an instance of GUI is created. Sets up everything needed for the class to function
        self.cap = cv.VideoCapture(cameraNumber)    #Creates a new instance of VideoCapture using the ID entered as a parameter
    
    def getImage(self):                 #Defines a function that runs to get a new image from the camera
        _, frame = self.cap.read()                          #Gets the image from the camera
        return frame              #Returns the image to wherever the function is called

#This keeps the program from running if this is imported into another file
if __name__ == "__main__":
    main()