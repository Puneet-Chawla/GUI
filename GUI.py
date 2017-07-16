from tkinter import *

root = Tk()

topFrame = Frame(root)
bottomFrame = Frame(root)
topFrame.pack()
bottomFrame.pack(side = BOTTOM)

button1 = Button(topFrame,text="Click Here",fg="blue")
button2 = Button(topFrame,text="Click Here",fg="yellow")
button3 = Button(topFrame,text="Click Here",fg="green")
button4 = Button(bottomFrame,text="Click Here",fg="red")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()
root.mainloop()