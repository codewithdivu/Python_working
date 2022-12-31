from tkinter import *
root = Tk()
root.geometry("655x333")
f1 = Frame(root,bg="grey",borderwidth=6,relief=GROOVE)
f1.pack(side=LEFT,fill="y")

f2 = Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f2.pack(side=TOP,fill="x")

l=Label(f1,text="Hello Coders..",bg="red")
l.pack(pady=150)

l=Label(f2,text="Kem so badhay..")
l.pack()

root.mainloop()