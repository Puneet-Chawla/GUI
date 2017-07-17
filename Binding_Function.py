from tkinter import *

# type 1 of binding a function to an event

def printName():
    print("hye its way one")

root = Tk()
button1 = Button(root, text="Print Name", command=printName)
button1.pack()


# type 2 of binding a function to enent

def printname(event):
    print("hello its way two")

button2 = Button(root, text="Print Name")
button2.bind("<Button-1>",printname)
button2.pack()
# looping the GUI unitl close is pressed

root.mainloop()