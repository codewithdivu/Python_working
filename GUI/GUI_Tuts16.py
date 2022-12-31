# Exercise - 2

from tkinter import *

def Divu():
    Width_Value = Width.get()
    Height_Value = Height.get()
    root.geometry(f"{Width_Value}x{Height_Value}")

root = Tk()
root.title("Exercise-2")
root.geometry("400x350")

Label(root,text="Exercise No-2",font='comicsansms 30 bold',pady=25).grid(column=2)

Label(root,text="Width",font='comicsansms 20 bold',pady=25).grid(row=1,column=1)
Label(root,text="Height",font='comicsansms 20 bold',pady=25).grid(row=2,column=1)

Width = StringVar()
Height = StringVar()

Width_entry = Entry(root , textvariable=Width).grid(row=1,column=2)
Height_entry = Entry(root , textvariable=Height).grid(row=2,column=2)

Button(text="Apply",command=Divu,pady=2, font="comicsansms 11").grid(column=2)

root.mainloop()