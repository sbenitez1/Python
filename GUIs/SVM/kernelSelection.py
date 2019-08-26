################################################################
## {Code for selecting kernel of Support Vector Machines}
################################################################
## Author: {Sandra Benitez Pena}
## Email: {sbenitez1@us.es}
## Date:  {2019-08-26}
################################################################

import tkinter
import csv
from tkinter import *
from tkinter import messagebox
import tkinter as tk


window = Tk()
window.title('Code for selecting kernel of Support Vector Machines')
window.geometry('450x150+10+20')

lbl=Label(window, text="GUI and code created by Sandra Benitez-Pena, 2019", fg='black', font=("Times", 12))
lbl.place(x=100, y=110)

# label text 
Label(window, text ='Select which kernel of SVM to run:').place(x = 20, y = 20) 

# check buttons 
linear = Checkbutton(window, text ='Linear', 
               takefocus = 0).place(x = 40, y = 40) 

radial = Checkbutton(window, text ='Radial', 
              takefocus = 0).place(x = 40, y = 60) 
            

window.mainloop()
window.destroy()
