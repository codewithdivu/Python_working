from tkinter import *
from PIL import Image , ImageTk

root = Tk()

root.geometry("644x355")
# photo = PhotoImage(file="divu.JPG")

# for JPG
image =Image.open("divu.JPG")
photo = ImageTk.PhotoImage(image)
a_label = Label(image=photo)
a_label.pack()

root.mainloop()