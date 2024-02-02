from tkinter import *
top=Tk()
def add ():
    label.config(text=CheckVar1.get())
CheckVar1=IntVar()
C1=Checkbutton(top,text="Music",variable=CheckVar1, \
               onvalue=1,offvalue=0,height=5, \
               width=20
               )
C1.pack()
CheckVar2=IntVar()
C2=Checkbutton(top,text="Game",variable=CheckVar2, \
               onvalue=2,offvalue=0,height=2, \
               width=20
               )
C2.pack()
btn=Button(top,text="Done",command=add)
label=Label(top,text="")
label.pack()
btn.pack()
top.mainloop()