import Tkinter

top = Tk()
top.geometry('500x520')
top.title("Registration form")

L=Label(top,text="Registration Form",font="bold")
L.place(x=120,y=60)

L1 = Label(top, text="FirstName")
L1.place(x=80,y=130)


E1 = Entry(top, bd =2,variable=fname)
E1.place(x=160,y=130)

L2 = Label(top, text="LastName")
L2.place(x=80,y=180)


E2 = Entry(top, bd =2)
E2.place(x=160,y=180)

L3 = Label(top, text="EmailID")
L3.place(x=80,y=230)

E3 = Entry(top, bd =2)
E3.place(x=160,y=230)

L4 = Label(top, text="Gender")
L4.place(x=80,y=280)

var=IntVar()
E4=Radiobutton(top,text="Male",variable=var,value=1)
E4.place(x=160,y=280)

E5=Radiobutton(top,text="Female",variable=var,value=0)
E5.place(x=220,y=280)

L5 = Label(top, text="Programming")
L5.place(x=80,y=335)

list1=['python','php','java','perl','ruby']
a=StringVar()
b=OptionMenu(top,a,*list1)
b.config(width=15)
a.set("select the course")
b.place(x=160,y=330)

L6=Label(top,text="Degree")
L6.place(x=80,y=380)
var1=IntVar()
A=Checkbutton(top,text="B.E",variable=var1)
A.place(x=160,y=380)
var2=IntVar()
B=Checkbutton(top,text="M.E",variable=var2)
B.place(x=220,y=380)

L7 = Label(top, text="PhoneNo")
L7.place(x=80,y=430)

E6 = Entry(top, bd =2)
E6.place(x=160,y=430)

E7 = Button(top,text="Submit",command=database)
E7.place(x=160,y=480)
top.mainloop() 
 














