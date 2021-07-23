import tkinter
from tkinter import *

top=tkinter.Tk()
def mmt():
	Canvas.move("car",2,0)
	Canvas.after(20,mmt)
	
Canvas=Canvas(top)
rect=Canvas.create_rectangle(40,100,300,200,tag="car",fill="powderblue")
l1=Canvas.create_line(100,40,200,40,tag="car")
l2=Canvas.create_line(100,40,80,100,tag="car")
l3=Canvas.create_line(200,40,300,100,tag="car")
c1=Canvas.create_oval(70,180,110,220,tag="car",fill="black")
c2=Canvas.create_oval(35,100,40,120,tag="car",fill="black")
l1=Canvas.create_oval(35,100,40,120,tag="car")
l1=Canvas.create_oval(319,100,300,120,tag="car")

c1=Canvas.create_oval(250,180,280,220,tag="car",fill="black")

mmt()

Canvas.pack()

top.mainloop()
