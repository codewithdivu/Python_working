from tkinter import *
root = Tk()
root.title("Menu bar")
root.geometry("455x323")

def myfunc():
    print("Hello Bhosdiwalo kese ho")

# Use these to create a non dropdown menu
# mymenu = Menu(root)
# mymenu.add_command(label="File",command=myfunc)
# mymenu.add_command(label="Exit",command=quit)
# root.config(menu=mymenu)

Filemenu = Menu(root)
m1 = Menu(Filemenu,tearoff=0)
m1.add_command(label="New Project",command=myfunc)
m1.add_command(label="Project",command=myfunc)
m1.add_separator()
m1.add_command(label="Save",command=myfunc)
m1.add_command(label="Save AS",command=myfunc)
m1.add_separator() 
m1.add_command(label="Open",command=myfunc)
root.config(menu=Filemenu)
Filemenu.add_cascade(label="File",menu=m1)

root.mainloop()