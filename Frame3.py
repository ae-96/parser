from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
import  os

class frame3 :
    def __init__(self,master,contents):
        self.contents = contents
        self.main=master
        self.Master = Frame(master)
        self.Master.pack(side=TOP)
        self.master_will_be_deleted = Frame(master)
        self.master_will_be_deleted.pack(side=BOTTOM)
        self._4_buttons_master = Frame(self.main)
        self._4_buttons_master.pack(side=TOP)
        self.save = Frame(self.main)
        self.save.pack(side=BOTTOM)

        self.Scan_Button = Button(self.master_will_be_deleted, text=" Scan ", command=self.PrintTree, font="arial 15 italic", width=20)
        self.Scan_Button.pack(side=BOTTOM)

    def PrintTree(self):
        d=""
    def show_Label(self,contents=""):

        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"), width=1000, height=500)

        canvas = Canvas(self.Master)
        self.scroll = Frame(self.Master)
        self.scroll.pack(side=BOTTOM,fill="x")
        self.frame = Frame(canvas)
        myscrollbar = Scrollbar(self.Master, command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set)
        canvas.create_window((0, 0), window=self.frame, anchor='nw')
        self.frame.bind("<Configure>", myfunction)
        myscrollbar.pack(side=RIGHT,fill="y")
        canvas.pack(side=RIGHT)



        myscrollbar1 = Scrollbar(self.scroll, orient="horizontal", command=canvas.xview)
        canvas.configure(xscrollcommand=myscrollbar1.set)
        canvas.create_window((0, 0), window=self.frame, anchor='nw')
        self.frame.bind("<Configure>", myfunction)
        myscrollbar1.pack(side="bottom", fill="x")
        canvas.pack(side="bottom")


        self.text=Text(self.frame,width=5000,height=600)
        self.text.insert(INSERT, contents)

        self.text.pack(side=LEFT)