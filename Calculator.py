from tkinter import *


root = Tk()
root.title("Calculator")

FONT= ("Calibri", 15, "bold")
OPERATION_BUTTON_STYLE = {"borderwidth": 2, "width": 8, "height": 3, "activebackground": "#f5a742", "background": "orange", "fg":"black", "font": FONT, "relief": "groove", "borderwidth": 1}
BUTTON_STYLE = {"borderwidth": 2, "background":"black", "width": 8, "height": 3,"activebackground": "#4a4642", "fg": "white", "font": FONT, "relief": "groove", "borderwidth": 1}

addition_check, minus_check, multiplication_check, division_check = 0, 0, 0, 0

data_input = Entry(root, width=35, borderwidth=2, font=FONT)
data_input.grid(row=0, columnspan=4, rowspan=2, sticky="NSWE")


def click_action(number: int):
    temp = data_input.get()
    data_input.delete(0, END)
    data_input.insert(0, str(temp) + str(number))


def click_comma():
    data_input.insert(0, ".")


def click_delete():
    data_input.delete(0, END)
    global number
    number = 0


def click_equal():
    global number 
    global addition_check
    global minus_check
    global division_check
    global multiplication_check

    second_number = data_input.get()    
    data_input.delete(0, END)

    if addition_check == 1:
        data_input.insert(0, number + float(second_number))
        number = float(number) + float(second_number)
        addition_check = 0

    if minus_check == 1:
        data_input.insert(0, number - float(second_number))
        minus_check = 0

    if division_check == 1:
        data_input.insert(0, number / float(second_number))
        division_check = 0

    if multiplication_check == 1:
        data_input.insert(0, number * float(second_number))
        multiplication_check = 0


def click_add():
    global number
    global addition_check
    addition_check = 1
    first_number = data_input.get()
    number = float(first_number)
    data_input.delete(0, END)


def click_minus():
    global number
    global minus_check 
    minus_check = 1
    first_number = data_input.get()
    number = float(first_number)
    data_input.delete(0, END)
  

def click_division():
    global number
    global division_check 
    division_check = 1
    first_number = data_input.get()
    number = float(first_number)
    data_input.delete(0, END)


def click_multiplication():
    global number
    global multiplication_check 
    multiplication_check = 1
    first_number = data_input.get()
    number = float(first_number)
    data_input.delete(0, END)


button_1 = Button(text="1", command=lambda: click_action(1), **BUTTON_STYLE).grid(row=6, column=0)
button_2 = Button(text="2", command=lambda: click_action(2), **BUTTON_STYLE).grid(row=6, column=1)
button_3 = Button(text="3", command=lambda: click_action(3), **BUTTON_STYLE).grid(row=6, column=2)
button_4 = Button(text="4", command=lambda: click_action(4), **BUTTON_STYLE).grid(row=5, column=0)
button_5 = Button(text="5", command=lambda: click_action(5), **BUTTON_STYLE).grid(row=5, column=1)
button_6 = Button(text="6", command=lambda: click_action(6), **BUTTON_STYLE).grid(row=5, column=2)
button_7 = Button(text="7", command=lambda: click_action(7), **BUTTON_STYLE).grid(row=4, column=0)
button_8 = Button(text="8", command=lambda: click_action(8), **BUTTON_STYLE).grid(row=4, column=1)
button_9 = Button(text="9", command=lambda: click_action(9), **BUTTON_STYLE).grid(row=4, column=2)
button_0 = Button(text="0", command=lambda: click_action(0), **BUTTON_STYLE).grid(row=7, column=1)


button_add = Button(text="+", command=lambda: click_add(), **OPERATION_BUTTON_STYLE).grid(row=4, column=3)
button_minus = Button(text="-", command=lambda: click_minus(), **OPERATION_BUTTON_STYLE).grid(row=5, column=3)
button_divide = Button(text="/", command=lambda: click_division(), **OPERATION_BUTTON_STYLE).grid(row=6, column=3)
button_multiply = Button(text="*", command=lambda: click_multiplication(), **OPERATION_BUTTON_STYLE).grid(row=7, column=3)


button_equal = Button(text="=", command=lambda: click_equal(), **OPERATION_BUTTON_STYLE).grid(row=7, column=2)
button_clear = Button(text="Clear input", command=click_delete, **OPERATION_BUTTON_STYLE).grid(row=8, column=0, columnspan=4, sticky="NSWE")
button_comma = Button(text=",", command=lambda: click_action("."), **OPERATION_BUTTON_STYLE).grid(row=7, column=0)


root.mainloop()