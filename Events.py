from tkinter import *

root = Tk()
# defining different functions to different events of mouse click

def left_click(event):
    print("left")

def right_click(event):
    print("right")

def center(event):
    print("middle")

# Binding clck events to a frame
frame = Frame(root, width= 300, height= 300)
frame.bind("<Button-1>",left_click)
frame.bind("<Button-2>",center)
frame.bind("<Button-3>",right_click)

frame.pack()

root.mainloop()