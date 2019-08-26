from tkinter import *

window = Tk()
window.title("SlideBars for selecting min and max values of C and gamma")
window.geometry("600x400") 
lbl=Label(window, text="GUI and code created by Sandra Benitez-Pena, 2019", fg='black', font=("Times", 12))
lbl.place(x=250, y=370)

def calcularResultadominC(x):
    labelminC.config(text="Minimum value of C is " + str(2**int(x)))
    
labelminC = Label(window)

   
valorActualSliderminC = DoubleVar()
scaleminC = Scale( window, variable = valorActualSliderminC , from_ =-12,to=12, tickinterval=2,
 command=calcularResultadominC, orient = HORIZONTAL, length=400)

scaleminC.pack(anchor=CENTER)
labelminC.pack()


def calcularResultadomaxC(x):
    labelmaxC.config(text="Maximum value of C is " + str(2**int(x)))
    
labelmaxC = Label(window)

   
valorActualSlidermaxC = DoubleVar()
scalemaxC = Scale( window, variable = valorActualSlidermaxC , from_ =-12,to=12, tickinterval=2,
 command=calcularResultadomaxC, orient = HORIZONTAL, length=400)

scalemaxC.pack(anchor=CENTER)
labelmaxC.pack()


def calcularResultadomingam(x):
    labelmingam.config(text="Minimum value of gamma is " + str(2**int(x)))
    
labelmingam = Label(window)

   
valorActualSlidermingam = DoubleVar()
scalemingam = Scale( window, variable = valorActualSlidermingam , from_ =-12,to=12, tickinterval=2,
 command=calcularResultadomingam, orient = HORIZONTAL, length=400)

scalemingam.pack(anchor=CENTER)
labelmingam.pack()


def calcularResultadomaxgam(x):
    labelmaxgam.config(text="Maximum value of gamma is " + str(2**int(x)))
    
labelmaxgam = Label(window)

   
valorActualSlidermaxgam = DoubleVar()
scalemaxgam = Scale( window, variable = valorActualSlidermaxgam , from_ =-12,to=12, tickinterval=2,
 command=calcularResultadomaxgam, orient = HORIZONTAL, length=400)

scalemaxgam.pack(anchor=CENTER)
labelmaxgam.pack()

window.mainloop()