# from tkinter import *
# window=Tk()
# def add ():
#     print(var.get())
# var=IntVar()
# r1=Radiobutton(window,text="Male",variable=var,value=1,command=add)
# r1.pack(anchor=W)
# r2=Radiobutton(window,text="Female",variable=var,value=2,command=add)
# r2.pack(anchor=W)
# window.mainloop()

from tkinter import *
window=Tk()
def add ():
    selection="you have selected the option"+ str(var.get())
    label.config(text=selection)
var=IntVar()
r1=Radiobutton(window,text="Option 1",variable=var,value=1,command=add)
r1.pack(anchor=W)
r2=Radiobutton(window,text="Option 2",variable=var,value=2,command=add)
r2.pack(anchor=W)
r3=Radiobutton(window,text="Option 3",variable=var,value=3,command=add)
r3.pack(anchor=W)
label=Label(window)
label.pack()
window.mainloop()