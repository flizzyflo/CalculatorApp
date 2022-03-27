
from tkinter import END

addition_check, minus_check, multiplication_check, division_check = 0, 0, 0, 0

def click_action(input: int, data_input: object):
    temp = data_input.get()
    data_input.delete(0, END)
    data_input.insert(0, str(temp) + str(input))


def click_comma(data_input: object):
    data_input.insert(0, ".")


def click_delete(data_input: object):
    data_input.delete(0, END)
    global number
    number = 0


def click_equal(data_input: object):
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


def click_add(data_input: object):
    global number
    global addition_check
    addition_check = 1
    first_number = data_input.get()
    number = float(first_number)
    data_input.delete(0, END)


def click_minus(data_input: object):
    global number
    global minus_check 
    minus_check = 1
    first_number = data_input.get()
    number = float(first_number)
    data_input.delete(0, END)
  

def click_division(data_input: object):
    global number
    global division_check 
    division_check = 1
    first_number = data_input.get()
    number = float(first_number)
    data_input.delete(0, END)


def click_multiplication(data_input: object):
    global number
    global multiplication_check 
    multiplication_check = 1
    first_number = data_input.get()
    number = float(first_number)
    data_input.delete(0, END)
