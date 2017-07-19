from tkinter import *
import tkinter.messagebox

# Adding message box

root = Tk()

# creating a normal message
tkinter.messagebox.showinfo("Welcome",message = "welcome to message project")

# creating a question dialog box(Y/N)
answer = tkinter.messagebox.askquestion("What?","Did you just run that")
if answer == 'yes':
    print(" okay cool ")
else:
    print("you got that")

# creating a Y/N messaeg box
answer1 =tkinter.messagebox.askyesno("Alert","Do u want to exit?")
if answer1 == "yes":
    print(" u better run")
    root.quit
else :
    print("So you decided to stay")

root.mainloop()