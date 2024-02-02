from tkinter import *
root=Tk()
root.title('Login')
root.iconbitmap("D:\\prgarmming class\\desktopapp\\abc.ico")
root.geometry("300x200")
name=Label(root,text='Username:',fg='Dark Blue',font=('Candara Light',13,'bold')).place(x=30,y=50)
e1=Entry(root).place(x=130,y=50)
pw=Label(root,text="Password:",fg='Dark Blue',font=('Candara Light',13,'bold')).place(x=30,y=80)
e2=Entry(root).place(x=130,y=80)
def add():
    nm=Label(text="Welcome!!!!",font=('Candara Light',13,'bold'))
    nm.pack()
submit=Button(root,text="Submit",command=add,fg='Red',font=('Cambria',13,'bold')).place(x=100,y=120)
root.mainloop()
