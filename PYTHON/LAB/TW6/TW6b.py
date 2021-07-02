#  Create a GUI program that calculates the hypotenuse of a right angled 
# triangle after the user enters the lengths of the two sides and clicks the 
# Calculate button.

from tkinter import *
import math 

root = Tk()
root.title("Hypotenuse Calculator")

label1 = Label(root,text="Side 1 value : ")
label1.grid(row=0,column=0,columnspan=1,padx=10,pady=5)
label2 = Label(root,text="Side 2 value : ")
label2.grid(row=1,column=0,columnspan=1,padx=10,pady=5)

entry1 = Entry(root,width=10)
entry1.grid(row=0,column=1,columnspan=1,padx=10,pady=5)
entry2 = Entry(root,width=10)
entry2.grid(row=1,column=1,columnspan=1,padx=10,pady=5)

def calc():
    side1 = int(entry1.get())
    side2 = int(entry2.get())

    res = (side1**2) + (side2**2)
    res = math.sqrt(res) 

    res_label = Label(root,text="Hypotenuse is : "+str(res))
    res_label.grid(row=3,column=0,columnspan=1,padx=10,pady=5)

calc_btn = Button(root,text="Calculate",command=calc)
calc_btn.grid(row=2,column=0,columnspan=1,padx=10,pady=5)

root.mainloop()