'''
Created on Jun 20, 2019

@author: karl
'''

import tkinter as tk

root = tk.Tk()

root.title("Radio Buttons")
root.geometry("200x250")

def showStringChoice():
    lblString.config(text=("You chose " + str(varString.get())))
    print(varString.get())
    lblString.pack(anchor = tk.W)
    
def showIntChoice():
    lblInt.config(text=("You chose " + str(varInt.get())))
    print(varInt.get())
    lblInt.pack(anchor = tk.W)

varString = tk.StringVar()
varInt = tk.IntVar()

lblString = tk.Label(root, text="", font=30)
lblString.pack(anchor = tk.W)

tk.Radiobutton(root, text="Option A", variable=varString, value="A", command=showStringChoice).pack(anchor = tk.W)
tk.Radiobutton(root, text="Option B", variable=varString, value="B", command=showStringChoice).pack(anchor = tk.W)
tk.Radiobutton(root, text="Option C", variable=varString, value="C", command=showStringChoice).pack(anchor = tk.W)
tk.Radiobutton(root, text="Option D", variable=varString, value="D", command=showStringChoice).pack(anchor = tk.W)

lblInt = tk.Label(root, text="", font=30)
lblInt.pack(anchor = tk.W)

tk.Radiobutton(root, text="Option 1", variable=varInt, value=1, command=showIntChoice).pack(anchor = tk.W)
tk.Radiobutton(root, text="Option 2", variable=varInt, value=2, command=showIntChoice).pack(anchor = tk.W)
tk.Radiobutton(root, text="Option 3", variable=varInt, value=3, command=showIntChoice).pack(anchor = tk.W)

root.mainloop()