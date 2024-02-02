from tkinter import *
root=Tk()
root.title('Registration')
root.iconbitmap("D:\\prgarmming class\\desktopapp\\abc.ico")
root.geometry("300x300")
reg=Label(text="Registration",fg='Red',font=('Cambria',18,'bold')).place(x=80,y=30)
name=Label(root,text='First Name:',fg='Dark Blue',font=('Candara Light',13,'bold')).place(x=30,y=70)
e1=Entry(root).place(x=130,y=70)
lm=Label(root,text="Last Name:",fg='Dark Blue',font=('Candara Light',13,'bold')).place(x=30,y=100)
e2=Entry(root).place(x=130,y=100)
addr=Label(root,text='Address:',fg='Dark Blue',font=('Candara Light',13,'bold')).place(x=30,y=130)
e4=Entry(root).place(x=130,y=130)
cn=Label(root,text='C.Number:',fg='Dark Blue',font=('Candara Light',13,'bold')).place(x=30,y=170)
e5=Entry(root).place(x=130,y=170)
em=Label(root,text='E-mail:',fg='Dark Blue',font=('Candara Light',13,'bold')).place(x=30,y=200)
e5=Entry(root).place(x=130,y=200)
def add():
    nm=Label(text="Welcome!!!!",font=('Candara Light',13,'bold'))
    nm.pack()
    root.destroy()
    import lgn
submit=Button(root,text="Submit",command=add,fg='Red',font=('Cambria',13,'bold')).place(x=100,y=250)

root.mainloop()