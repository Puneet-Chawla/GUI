from tkinter import *

root= Tk()
label1= Label(root, text= "Name")
label2= Label(root, text= "Name")
label1.grid(row= 0, column=0, sticky= N)
label2.grid(row= 1, column=0, sticky= S)

entry1= Entry(root)
entry2= Entry(root)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

c= Checkbutton(root, text="keep me logged in")
c.grid(columnspan= 2)

root.mainloop()