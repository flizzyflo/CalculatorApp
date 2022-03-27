from tkinter import *
from ButtonFunctions import click_action, click_add, click_comma, click_delete, click_division, click_equal, click_minus, click_multiplication


root = Tk()
root.title("Calculator")

FONT= ("Calibri", 15, "bold")
OPERATION_BUTTON_STYLE = {"borderwidth": 2, "width": 8, "height": 3, "activebackground": "#f5a742", "background": "orange", "fg":"black", "font": FONT, "relief": "groove", "borderwidth": 1}
BUTTON_STYLE = {"borderwidth": 2, "background":"black", "width": 8, "height": 3,"activebackground": "#4a4642", "fg": "white", "font": FONT, "relief": "groove", "borderwidth": 1}

data_input_widget = Entry(root, width=35, borderwidth=2, font=FONT)
data_input_widget.grid(row=0, columnspan=4, rowspan=2, sticky="NSWE")


button_1 = Button(text="1", command=lambda: click_action(input= 1, data_input= data_input_widget), **BUTTON_STYLE).grid(row=6, column=0)
button_2 = Button(text="2", command=lambda: click_action(input= 2, data_input= data_input_widget), **BUTTON_STYLE).grid(row=6, column=1)
button_3 = Button(text="3", command=lambda: click_action(input= 3, data_input= data_input_widget), **BUTTON_STYLE).grid(row=6, column=2)
button_4 = Button(text="4", command=lambda: click_action(input= 4, data_input= data_input_widget), **BUTTON_STYLE).grid(row=5, column=0)
button_5 = Button(text="5", command=lambda: click_action(input= 5, data_input= data_input_widget), **BUTTON_STYLE).grid(row=5, column=1)
button_6 = Button(text="6", command=lambda: click_action(input= 6, data_input= data_input_widget), **BUTTON_STYLE).grid(row=5, column=2)
button_7 = Button(text="7", command=lambda: click_action(input= 7, data_input= data_input_widget), **BUTTON_STYLE).grid(row=4, column=0)
button_8 = Button(text="8", command=lambda: click_action(input= 8, data_input= data_input_widget), **BUTTON_STYLE).grid(row=4, column=1)
button_9 = Button(text="9", command=lambda: click_action(input= 9, data_input= data_input_widget), **BUTTON_STYLE).grid(row=4, column=2)
button_0 = Button(text="0", command=lambda: click_action(input= 0, data_input= data_input_widget), **BUTTON_STYLE).grid(row=7, column=1)


button_add = Button(text="+", command=lambda: click_add(data_input= data_input_widget), **OPERATION_BUTTON_STYLE).grid(row=4, column=3)
button_minus = Button(text="-", command=lambda: click_minus(data_input= data_input_widget), **OPERATION_BUTTON_STYLE).grid(row=5, column=3)
button_divide = Button(text="/", command=lambda: click_division(data_input= data_input_widget), **OPERATION_BUTTON_STYLE).grid(row=6, column=3)
button_multiply = Button(text="*", command=lambda: click_multiplication(data_input= data_input_widget), **OPERATION_BUTTON_STYLE).grid(row=7, column=3)


button_equal = Button(text="=", command=lambda: click_equal(data_input= data_input_widget), **OPERATION_BUTTON_STYLE).grid(row=7, column=2)
button_clear = Button(text="Clear input", command= lambda: click_delete(data_input= data_input_widget), **OPERATION_BUTTON_STYLE).grid(row=8, column=0, columnspan=4, sticky="NSWE")
button_comma = Button(text=",", command=lambda: click_action(input=".", data_input= data_input_widget), **OPERATION_BUTTON_STYLE).grid(row=7, column=0)


def main():
    root.mainloop()

if __name__ == "__main__":
    main()