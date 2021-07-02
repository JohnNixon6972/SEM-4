# Develop a simple GUI calculator using tkinter

from tkinter import *

root = Tk()
root.title("Simple Calculator")


first_label = Label(root, text="First Number: ")
first_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
Second_label = Label(root, text="Second Number: ")
Second_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
res_label = Label(root, text="Result")
res_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

first_entry = Entry(root, width=15)
first_entry.grid(row=0, column=3, columnspan=2, padx=5, pady=5)
second_entry = Entry(root, width=15)
second_entry.grid(row=1, column=3, columnspan=2, padx=5, pady=5)

res_entry = Entry(root, text="", width=15)
res_entry.grid(row=3, column=3, columnspan=2)


def add():
    num1 = int(first_entry.get())
    num2 = int(second_entry.get())
    res = num1+num2
    res_entry.delete(0, END)
    res_entry.insert(0, res)


def div():
    num1 = int(first_entry.get())
    num2 = int(second_entry.get())
    res = num1/num2
    res_entry.delete(0, END)
    res_entry.insert(0, res)


def sub():
    num1 = int(first_entry.get())
    num2 = int(second_entry.get())
    res = num1-num2
    res_entry.delete(0, END)
    res_entry.insert(0, res)


def mul():
    num1 = int(first_entry.get())
    num2 = int(second_entry.get())
    res = num1*num2
    res_entry.delete(0, END)
    res_entry.insert(0, res)


add_btn = Button(root, text="ADD", command=add)
add_btn.grid(row=2, column=1)
sub_btn = Button(root, text="SUB", command=sub)
sub_btn.grid(row=2, column=2)
div_btn = Button(root, text="DIV", command=div)
div_btn.grid(row=2, column=3)
mul_btn = Button(root, text="MUL", command=mul)
mul_btn.grid(row=2, column=4)

root.mainloop()
