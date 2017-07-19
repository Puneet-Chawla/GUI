from tkinter import *

root = Tk()
# Adding canvas size is needed

canvas = Canvas(root, width = 200, height = 100 )
canvas.pack()

# Adding starting and ending points
line = canvas.create_line(0, 0, 200, 50)
line1 = canvas.create_line(0, 100, 200, 50, fill ="red")

# creating a rectangle it takes starting point of left rectangle, then width and height of rectangle
box = canvas.create_rectangle(25, 25, 150, 60 , fill = "blue")


# hiding these shapes which can be added to a function which can be called on the click of  button or something
canvas.delete(line1)

# canvas.delete(all)  - to delete all the things on data
root.mainloop()