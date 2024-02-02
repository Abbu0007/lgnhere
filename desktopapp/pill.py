from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.title("Image insertion")
my_image=ImageTk.PhotoImage(Image.open("D:\prgarmming class\desktopapp\manu.jpg"))
my_label=Label( image=my_image )
my_label.pack()
root.mainloop()