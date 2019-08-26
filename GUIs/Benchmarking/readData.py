################################################################
## {Code for reading data as csv, using pandas}
################################################################
## Author: {Sandra Benitez Pena}
## Email: {sbenitez1@us.es}
## Date:  {2019-08-26}
################################################################

import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd


def import_csv_data():
    global v
    csv_file_path = askopenfilename()
    print(csv_file_path)
    v.set(csv_file_path)
    df = pd.read_csv(csv_file_path)
    #print(df.head())

root = tk.Tk()
root.title("Code for reading data as csv, using pandas")
root.geometry("450x100") 
tk.Label(root, text='File Path').grid(row=0, column=0)
v = tk.StringVar()
entry = tk.Entry(root, textvariable=v,bd=5,width=50).grid(row=0, column=1)
tk.Button(root, text='Browse Data Set',command=import_csv_data).grid(row=1, column=0)
tk.Button(root, text='Close',command=root.destroy).grid(row=1, column=1)

tk.Label(root, text="GUI and code created by Sandra Benitez-Pena, 2019", fg='black', font=("Times", 12)).place(x=100, y=75)
#lbl.place(x=20, y=20)

root.mainloop()
