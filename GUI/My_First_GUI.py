# now we are going to make our first form by tkinter

from tkinter import *
root = Tk()

def Information():
    print(f"Name is {name_value.get()}")
    print(f"Gender is {gender_value.get()}")
    print(f"Phone Number is {number_value.get()}")
    print(f"Aadhar is {aadhar_value.get()}")
    print(f"Age is {age_value.get()}")

    with open("Information.txt","a") as f:
        f.write(f"Name is {name_value.get()}"
                f"Gender is {gender_value.get()}\n"
                f"Phone Number is {number_value.get()}\n"
                f"Aadhar is {aadhar_value.get()}\n"
                f"Age is {age_value.get()}\n"
                )

root.geometry("644x344")
root.title("My First form")

heading = Label(root , text="Welcome to the first form", font="comicsansms 25 bold",pady=15)
heading.grid(row=0,column=3)

name = Label(text="Name",font="15")
gender = Label(text="Gender",font="15")
number = Label(text="Phone_number",font="15")
aadhar = Label(text="Aadhar_number",font="15")
age = Label(text="Age",font="15")

name.grid(row=1,column=2)
gender.grid(row=2,column=2)
number.grid(row=3,column=2)
aadhar.grid(row=4,column=2)
age.grid(row=5,column=2)

name_value = StringVar()
gender_value = StringVar()
number_value = StringVar()
aadhar_value = StringVar()
age_value = StringVar()
# Making for check box value
Term_and_condition = IntVar()


name_entry = Entry(root,textvariable=name_value)
gender_entry = Entry(root,textvariable=gender_value)
number_entry = Entry(root,textvariable=number_value)
aadhar_entry = Entry(root,textvariable=aadhar_value)
age_entry = Entry(root,textvariable=age_value)

name_entry.grid(row=1,column=3)
gender_entry.grid(row=2,column=3)
number_entry.grid(row=3,column=3)
aadhar_entry.grid(row=4,column=3)
age_entry.grid(row=5,column=3)

privacy_policy = Checkbutton(text="Please you must have accept our privacy policy",font="10",variable=Term_and_condition)
privacy_policy.grid(row=9,column=3,pady=15)

Button(text="SUBMIT",font="20",command=Information).grid(row=10,column=3)
root.mainloop()