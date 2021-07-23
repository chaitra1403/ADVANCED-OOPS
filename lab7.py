import tkinter
from tkinter import *
from tkinter import messagebox
top=tkinter.Tk()
top.geometry("400x300")
gram=DoubleVar()
kilo=DoubleVar()
ahr=DoubleVar()
feren=DoubleVar()
ounce=DoubleVar()

top['bg']='blue'

def gtoo():
	ounce=gram.get()*0.0352
	messagebox.showinfo("alert",ounce)
def ktop():
	pound=kilo.get()*2.204
	messagebox.showinfo("alert",pound)
def ttos():
	stone=ahr.get() *2.204
	messagebox.showinfo("alert",stone)
def ftoc():
	cel=(feren.get()*1.8)+32
	messagebox.showinfo("alert",cel)

l1=Label(top,text="GRAM TO OUNCE")
l1.grid(row = 0, column = 0, sticky = W,padx=10, pady = 2) 
gra=Entry(top,textvariable=gram)
gra.grid(row = 0, column = 1, sticky = W, padx=10,pady = 2) 
b1=Button(top,text="ok",command=gtoo)
b1.grid(row = 0, column = 2, sticky = W,padx=10, pady = 2) 

l2=Label(top,text="KILO TO PONDS")
l2.grid(row = 1, column = 0, sticky = W, padx=10,pady = 5) 
kil=Entry(top,textvariable=kilo)
kil.grid(row = 1, column = 1, sticky = W,padx=10, pady = 5) 
b2=Button(top,text="ok",command=ktop)
b2.grid(row = 1, column = 2, sticky = W,padx=10, pady = 5)

l3=Label(top,text="STONE TO AHER")
l3.grid(row = 2, column = 0, sticky = W, padx=10,pady = 5) 
ah=Entry(top,textvariable=ahr)
ah.grid(row = 2, column = 1, sticky = W,padx=10, pady = 5) 
b3=Button(top,text="ok",command=ttos)
b3.grid(row = 2, column = 2, sticky = W,padx=10,pady = 5) 

l4=Label(top,text="CELC to FREN")
l4.grid(row = 3, column = 0, sticky = W,padx=10, pady = 5) 
fer=Entry(top,textvariable=feren)
fer.grid(row = 3, column = 1, sticky = W,padx=10, pady = 5) 
b4=Button(top,text="ok",command=ftoc)
b4.grid(row = 3, column = 2, sticky = W,padx=10, pady = 5) 

top.mainloop()












