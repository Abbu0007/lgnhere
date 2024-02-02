from tkinter import *
root=Tk()
def click():
    text1="Address:"+ mytext.get('1.0',END)
    lbl.config(txt=str(txt1))
mytext=Text(root,font=20,width=20,height=10)
mytext.place(x=0,y=50)
btn=Button(root,text="Click Me",font=30,command=click)
btn.place(x=400,y=300)
lbl=Label(root,text="",font=30)
lbl.place(x=200,y=300)
root.mainloop()