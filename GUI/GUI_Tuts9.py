from tkinter import *
root = Tk()
root.geometry("655x333")

frame = Frame(root,borderwidth=8,bg="grey",relief=GROOVE)
frame.pack(side=LEFT,anchor="nw")

def hello():
    print("Hello Bhosdiwalo")

b1 = Button(frame, fg="blue",text="B1_Button",command=hello,pady=35)
b1.pack(pady=25)
b2 = Button(frame, fg="blue",text="B2_Button")
b2.pack(pady=25)
b3 = Button(frame, fg="blue",text="B3_Button")
b3.pack(pady=25)
b4 = Button(frame, fg="blue",text="B4_Button")
b4.pack(pady=25)

root.mainloop()