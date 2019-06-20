'''
Created on Jun 20, 2019

@author: karl
'''

import tkinter as tk            #Used for the GUI
import cv2 as cv                #Used to collect and edit camera data
from PIL import Image, ImageTk  #Used to convert image types between TKInter and OpenCV

def main():
    #Creates and gives attributes to the window
    root = tk.Tk()
    root.title("My GUI")
    root.geometry("750x550")
    
    #Creates instance of CameraFeed class connected to camera 0
    camera = CameraFeed(0)
    
    #Creates instance of GUI class using root as a base and an image input from the camera
    myGUI = GUI(root, camera.getImage())
    
    #Updates the frame given to the GUI constant to show live camera
    while True:
        myGUI.displayImage(camera.getImage())   #Gets the current frame from the camera and tell the GUI to display it
        root.update()                           #Updates the window so that any new changes are displayed to the user

class GUI:
    def __init__(self, master, img):    #Runs when an instance of GUI is created. Sets up everything needed for the class to function
        def hideVideo():                #Defines a function to hide the label
            self.myLabel.pack_forget()
            
        def showVideo():                #Defines a function to show the label
            self.myLabel.pack(side=tk.constants.TOP)
        
        #Creates a frame that will hold the buttons
        tkFrame = tk.Frame(master)
        tkFrame.pack(side=tk.TOP)                   #Sets the location of the frame
        
        #Creates the label and sets it to the initial frame
        self.myLabel = tk.Label(master, image=img)
        self.myLabel.pack(in_=master, side=tk.TOP) #Sets the location of the label
        
        #Creates the button used to hide the video and binds it to the hideVideo function
        self.myButton = tk.Button(master, text="Hide", font=60, command=hideVideo, )
        self.myButton.pack(in_=tkFrame, side=tk.LEFT, fill=tk.BOTH) #Sets the location of the hide button within the frame
        
        #Creates the button used to show the video and binds it to the showVideo function
        self.myButton2 = tk.Button(master, text="Show", font=60, command=showVideo)
        self.myButton2.pack(in_=tkFrame, side=tk.LEFT, fill=tk.BOTH)#Sets the location of the show button within the frame
        
    def displayImage(self, img): #Defines the function used to update the frame
        self.myLabel.config(image=img)  #Takes the parameter of an image and sets it as the image in the label

class CameraFeed:
    def __init__(self, cameraNumber):   #Runs when an instance of GUI is created. Sets up everything needed for the class to function
        self.cap = cv.VideoCapture(cameraNumber)    #Creates a new instance of VideoCapture using the ID entered as a parameter
    
    def getImage(self):                 #Defines a function that runs to get a new image from the camera
        _, frame = self.cap.read()                          #Gets the image from the camera
        self.image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)   #Converts the image from BGR to RGB
        self.image = Image.fromarray(self.image)            #Converts the image to the Python Imaging Library(PIL) format
        self.image = ImageTk.PhotoImage(self.image)         #Converts the PIL format image to a format that TKInter can display
        return self.image               #Returns the image to wherever the function is called

#This keeps the program from running if this is imported into another file
if __name__ == "__main__":
    main()