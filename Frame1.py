from tkinter import *
from  Frame2 import  frame2
root=Tk()
root.title("Parser")
f=Frame(root)
f.pack()
i=frame2(f)
def reset():
    global f
    f.pack_forget()
    f.destroy()
    f = Frame(root)
    f.pack()
    i = frame2(f)
reset_b = Button(root, text=" Reset ", command=reset,width=5 , height= 1,font="arial 12 italic")
reset_b.pack(side=BOTTOM)
root.mainloop()