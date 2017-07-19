from tkinter import *

root = Tk()

def doNothing():
    print("wow")
menu1 = Menu(root)
root.config(menu = menu1)
subMenu = Menu(menu1)
menu1.add_cascade(label ="File",menu = subMenu)
subMenu.add_command(label = "New Project",command= doNothing)
subMenu.add_separator()
subMenu.add_command(label ="New", command = doNothing)

exitMenu = Menu(menu1)
menu1.add_cascade(label = "Edit",menu = exitMenu)
exitMenu.add_command(label="Redo", command=doNothing)

root.mainloop()