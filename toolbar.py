from tkinter import *

root = Tk()
# command to use on each buttin in drop down list

def doNothing():
    print("hello")
menu1 = Menu(root)
root.config(menu = menu1)
subMenu = Menu(menu1)
menu1.add_cascade(label = "File",menu = subMenu)
subMenu.add_command(label= "Open",command = doNothing)
subMenu.add_separator()
subMenu.add_command(label = "Save",command = doNothing)

exit = Menu(menu1)
menu1.add_cascade(label = "Exit",menu= exit)
exit.add_command(label="Undo",command = doNothing)
exit.add_command(label ='redo',command = doNothing)
exit.add_separator()
exit.add_command(label = "logout", command = doNothing)

# creating toolbar

toolbar = Frame(root ,bg ="blue")
insertButton = Button(toolbar,text ="Insert",relief = SUNKEN, command = doNothing)
insertButton.pack(side = LEFT,padx = 2,pady= 2)
printButton = Button(toolbar, text = "Print",relief = SUNKEN, command = doNothing)
printButton.pack(side = LEFT,padx = 2,pady = 2)
toolbar.pack(side = TOP, fill = "x")

# creating status bar

status = Label(root, text = "expression expected", bd = 1, relief = SUNKEN, anchor = W)
status.pack(side = BOTTOM, fill = "x")
root.mainloop()