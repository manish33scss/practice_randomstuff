# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 01:14:57 2020

@author: manish kumar
"""

from tkinter import *
from PIL import ImageTk , Image

root = Tk()

root.title("__")
#root.iconbitmap("location") #change icon of root window

#button_exit = Button(root, text = "exit" , command = root.destroy).pack()

def forward(image_number):
    global show_img
    global btn_forward
    global btn_back
    global status 
    
    show_img.grid_forget()
    show_img = Label(image = img_list[image_number-1])
    show_img.grid(row =0, column=0, columnspan = 3)
    
    btn_forward = Button(root, text = ">>" , command = lambda:forward(image_number +1))
    btn_back = Button(root,text = "<<" ,command = lambda:back(image_number-1))
    btn_forward.grid(row =1 , column = 1 )
    btn_back.grid(row = 1, column = 0)
    status = Label(root , text = "Image" +str(image_number) + "of " + str( len (img_list)))
    
    if image_number == len(img_list):
        btn_forward = Button (root, text = ">>" , state = DISABLED)
    show_img.grid(row =0, column=0, columnspan = 3)
   
    btn_forward.grid(row =1 , column = 1 )
    btn_back.grid(row = 1, column = 0)
    status.grid(row = 2, column = 0 , columnspan = 3, sticky = W)

def back (image_number):
    global show_img
    global btn_forward
    global btn_back
    global status
    
    show_img.grid_forget()
    show_img = Label(image = img_list[image_number-1])
    show_img.grid(row =0, column=0, columnspan = 3)
    status = Label(root , text = "Image" +str(image_number) + "of " + str( len (img_list)))

    btn_forward = Button(root, text = ">>" , command = lambda:forward(image_number +1))
    btn_back = Button(root,text = "<<" ,command = lambda:back(image_number-1))
    btn_forward.grid(row =1 , column = 1 )
    btn_back.grid(row = 1, column = 0)
    
    if image_number == 1:
        btn_back = Button (root, text = "<<" , state = DISABLED)
    show_img.grid(row =0, column=0, columnspan = 3)
    status.grid(row = 2, column = 0 , columnspan = 3, sticky = W)

    btn_forward.grid(row =1 , column = 1 )
    btn_back.grid(row = 1, column = 0)

img = ImageTk.PhotoImage(Image.open(r"D:\Work\Data_files\data\1.jpg"))
img2 = ImageTk.PhotoImage(Image.open(r"D:\Work\Data_files\data\blue1.jpg"))
img3 = ImageTk.PhotoImage(Image.open(r"D:\Work\Data_files\data\i.jpg"))
img4 = ImageTk.PhotoImage(Image.open(r"D:\Work\Data_files\data\j.jpg"))

img_list = [img,img2, img3,img4]  

show_img = Label(image = img)
show_img.grid(row=0, column = 0, columnspan = 3)

status = Label(root , text = "Image 1 of " + str( len (img_list)))
status.grid(row = 2, column = 0 , columnspan = 3 , sticky = W)


btn_forward = Button(root, text = ">>" , command = lambda:forward(2))
btn_exit = Button (root, text = "exit", command = root.destroy)
btn_back = Button (root, text = "<<" , command = back , state = DISABLED)

btn_forward.grid(row =1 , column = 1 )
btn_back.grid(row = 1, column = 0)
btn_exit.grid(row = 1, column = 3)


root.mainloop()
