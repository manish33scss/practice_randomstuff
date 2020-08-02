# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 04:43:58 2020

@author: manish kumar
"""


import tkinter as tk
root = tk.Tk()
root.geometry("450x90")
name_var= tk.StringVar()


label = tk.Label(root, text = "Enter the area" )
labl2 = tk.Label (root , text = "Convert to")
options = ['Gaj', 'Acre' , 'Nali', 'Sq.ft']
options_to = ["Sq.ft", "Gaj", "Acre", "Nali"]
clicked = tk.StringVar()
clicked.set(options[0])
clicked2 = tk.StringVar()
clicked2.set(options_to[0])


#FUNCTIONS >>>>>>>>>>>>>>>>
def convert ():
    pass

def clear():
    entry1.delete(first=0,last=100)

#def show():
#    label = Label(root, text = clicked.get())

def cal ():
    from_this = clicked.get()
    get_value = int(entry1.get())

    to_this = clicked2.get()
    if get_value > 0:
        if from_this == "Gaj" and to_this == "Sq.ft":
            converted_ = 10*get_value
            label_out = tk.Label(root, text = converted_)
            label_out.grid(row = 2, column =2)
        elif from_this == "Gaj" and to_this == "Gaj":
            converted_ = get_value
            label_out = tk.Label(root, text = converted_)
            label_out.grid(row = 2, column =2)
        elif from_this == "Gaj" and to_this == "Acre":
            converted_ = 0.00020661138759433*get_value
            label_out = tk.Label(root, text = converted_)
            label_out.grid(row = 2, column =2)
        elif from_this == "Gaj" and to_this == "Nali":
            converted_ = 0.00020661138759433*get_value
            label_out = tk.Label(root, text = converted_)
            label_out.grid(row = 2, column =2)
        # Acre >>>>>>>>>
        elif from_this == "Acre" and to_this == "Sq.ft":
            converted_ = 43560*get_value
            label_out = tk.Label(root, text = converted_)
            label_out.grid(row = 2, column =2)

        elif from_this == "Acre" and to_this == "Gaj":
            converted_ = 4886*get_value
            label_out = tk.Label(root, text = converted_)
            label_out.grid(row = 2, column =2)
        elif from_this == "Acre" and to_this == "Acre":
            converted_ = get_value
            label_out = tk.Label(root, text = converted_)
            label_out.grid(row = 2, column =2)
        elif from_this == "Acre" and to_this == "Nali":
            converted_ = 20.2*get_value
            label_out = tk.Label(root, text = converted_)
            label_out.grid(row = 2, column =2)

        #Nali
        elif from_this == "Nali" and to_this == "Nali":
            converted_ = get_value
            label_out = tk.Label(root, text = converted_)
            label_out.grid(row = 2, column =2)
        elif from_this == "Nali" and to_this == "Sq.ft":
            converted_ = 2160*get_value
            label_out = tk.Label(root, text = converted_)
            label_out.grid(row = 2, column =2)
        elif from_this == "Nali" and to_this == "Gaj":
            converted_ = 216*get_value
            label_out = tk.Label(root, text = converted_)
            label_out.grid(row = 2, column =2)
        elif from_this == "Nali" and to_this == "Acre":
            converted_ = 0.04958673302264*get_value
            label_out = tk.Label(root, text = converted_)
            label_out.grid(row = 2, column =2)

        #Sq.Ft
        elif from_this == "Sq.ft" and to_this == "Nali":
            converted_ = get_value
            label_out = tk.Label(root, text = converted_)
            label_out.grid(row = 2, column =2)
        elif from_this == "Sq.ft" and to_this == "Gaj":
            converted_ = 0.11*get_value
            label_out = tk.Label(root, text = converted_)
            label_out.grid(row = 2, column =2)
        elif from_this == "Sq.ft" and to_this == "Acre":
            converted_ = get_value
            label_out = tk.Label(root, text = converted_)
            label_out.grid(row = 2, column =2)
        elif from_this == "Sq.ft" and to_this == "Sq.ft":
            converted_ = 0.00020661138759433*get_value
            label_out = tk.Label(root, text = converted_)
            label_out.grid(row = 2, column =2)


#WIDGETS >>>>>>>>>>>>>>>>>>>>


entry1 = tk.Entry (root, textvariable=name_var)

btn1 = tk.Button(root , text = "Convert" , command = cal)
btn2  = tk.Button(root , text = "Clear" , command = clear)
#btn3 = Button (root, text = "Exit" , command = ).pack()
drop1 = tk.OptionMenu(root, clicked, *options)
drop2 = tk.OptionMenu(root, clicked2, *options_to)



#arrange >>>>>>>.
label.grid(row = 1 ,column=0)

entry1.grid (row = 1,column=2)
drop1.grid(row = 1,column = 3)
labl2.grid (row = 2 , column = 1)
drop2.grid (row =2, column =3)
btn1.grid(row = 3, column =3) #convert
btn2.grid(row=3,column = 4)





root.mainloop()
