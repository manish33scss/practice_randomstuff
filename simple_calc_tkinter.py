"""
Created on Sat Jul 25 04:33:02 2020

@author: manish kumar
"""
from tkinter import *

root = Tk()
root.title(" Calcula-THOR")


enter = Entry(root,width = 15,borderwidth = 3, bg= "white", fg= "cyan" )
enter.grid(row = 0 , column = 0 )

def button_click(number):
    #enter.delete(0,END)
    curr = enter.get()
    enter.delete(0,END)
    enter.insert(0,str(curr )+str( number))

def button_clear():
    enter.delete(0,END)


def button_add():
    first_n = enter.get()
    global f_num
    f_num = int(first_n)
    enter.delete(0, END)

def button_equals():
    sec_n = enter.get()
    enter.delete(0,END)
    res = f_num + int(sec_n)
    enter.insert(0 , res)

b1 = Button (root , text = "1" ,   fg = "blue" , bg = "white" , command = lambda: button_click(1)) #pad to change the sze of button
b2 = Button (root , text = "2" ,   fg = "blue" , bg = "white" , command = lambda: button_click(2)) #pad to change the sze of button
b3 = Button (root , text = "3" ,   fg = "blue" , bg = "white" , command = lambda: button_click(3)) #pad to change the sze of button
b4 = Button (root , text = "4" ,   fg = "blue" , bg = "white", command = lambda: button_click(4)) #pad to change the sze of button
b5 = Button (root , text = "5" ,   fg = "blue" , bg = "white", command = lambda: button_click(5)) #pad to change the sze of button
b6 = Button (root , text = "6" ,   fg = "blue" , bg = "white", command = lambda: button_click(6)) #pad to change the sze of button
b7 = Button (root , text = "7" ,   fg = "blue" , bg = "white", command = lambda: button_click(7)) 
b8 = Button (root , text = "8" ,   fg = "blue" , bg = "white", command = lambda: button_click(8)) #pad to change the sze of button
b9 = Button (root , text = "9" ,   fg = "blue" , bg = "white", command = lambda: button_click(9)) #pad to change the sze of button
b0 = Button (root , text = "0" ,   fg = "blue" , bg = "white", command = lambda: button_click(0)) #pad to change the sze of button
bp = Button (root , text = "+" ,   fg = "blue" , bg = "white" , command = button_add) #pad to change the sze of button
be = Button (root , text = "=" ,   fg = "blue" , bg = "white", command = button_equals) #pad to change the sze of button
bclear = Button (root, text = "clear", command = button_clear)

b1.grid(row = 1, column = 0)
b2.grid(row = 1, column = 1)
b3.grid(row = 1, column = 2)
b4.grid(row = 2, column = 0)
b5.grid(row = 2, column = 1)
b6.grid(row = 2, column = 2)
b7.grid(row = 3, column = 0)
b8.grid(row = 3, column = 1)
b9.grid(row = 3, column = 2)
b0.grid(row = 4, column = 0)
bp.grid(row = 4, column = 1)
be.grid(row = 4, column = 2)
bclear.grid(row = 4, column = 3)


root.mainloop()
