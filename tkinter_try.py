from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("600x600")
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")

B = Button(top, text = "Hello", command = helloCallBack)
B.place(x = 0,y = 200)
top.mainloop()