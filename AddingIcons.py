from tkinter import *

root = Tk()
# accessing a photo in any directory from the project
photo = PhotoImage(file= "homecoming.jpg")

# in tkinter we cannot add image directly to the window thus we use label
label = Label(root, image= photo)
label.pack()

root.mainloop()