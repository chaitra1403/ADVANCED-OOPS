import tkinter
from tkinter import*
from tkinter import messagebox
logpage=tkinter.Tk(className="LOGIN")
name="Chaitra"
pas="tumkur"

user=StringVar()
pwd=StringVar()

def login():
	if(user.get()==name and pwd.get()==pas):
		messagebox.showinfo("alert","login Done")
	else:
		messagebox.showinfo("alert","Wrong passwd or user name")

def clear():
	user.delete(0,END)
	pwd.delete(0,END)

logpage.geometry("400x200")
logpage.configure(bg='powderblue')	
l1=Label(logpage,text="USER NAME")
user=Entry(logpage,textvariable=user)
l2=Label(logpage,text="PASSWORD")
pwd=Entry(logpage,textvariable=pwd,show="*")
b1=Button(logpage,text="SUBMIT",command=login)
b2=Button(logpage,text="CLEAR",command=clear)

l1.pack()
user.pack()
l2.pack()
pwd.pack()
b1.pack()
b2.pack()

logpage.mainloop()
