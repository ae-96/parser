from tkinter import *
import tkinter.messagebox
from  Frame3 import  frame3
from  tkinter import  filedialog
import os.path
from os import path
class frame2 :
    def __init__(self,master):
        self.input=""
        self.newmaster = master
        self.master1 = Frame(master)
        self.master1.pack(side=TOP)
        self.master2 = Frame(master)
        self.master2.pack()
        self.master = Frame(master)
        self.master.pack()
        self.show_Label()
        self.Done_Button = Button(self.master2, text=" DONE ", command=self.Done, font="arial 14 italic", width=14)
        self.Done_Button.pack(side=TOP)
        self.enter_path = Label(self.master, text=" OR Enter\Browse Text File Path : ", font="arial 14 italic")
        self.enter_path.grid(row=0, column=0)
        self.path_entry = Entry(self.master, font="arial 14 italic")
        self.path_entry.grid(row=0, column=1)
        self.OK_Button = Button(self.master, text=" OK ", command=self.OK, font="arial 12 italic", width=10)
        self.OK_Button.grid(row=0, column=3)
        self.browse = Button(self.master, text=" Browse File ", command=self.browse, font="arial 12 italic", width=10)
        self.browse.grid(row=1, column=3)
    def filedialog(self):
        self.filename=filedialog.askopenfilename(title="Select A File",filetype=(("txt","*.txt"),("txt","*.txt")))
        return self.filename
    def Done(self):

        self.input = self.text.get("0.0", "end")
        if self.input == "\n":
            tkinter.messagebox.showinfo("error", "ERROR:Empty Entry")
        else :
            self.master.pack_forget()
            self.master.destroy()
            self.master1.pack_forget()
            self.master1.destroy()
            self.master2.pack_forget()
            self.master2.destroy()
            self.f = frame3(self.newmaster,self.input)
            self.f.show_Label(self.input)
    def OK(self):
        self.File_Path = self.path_entry.get()
        condition= path.isfile(self.File_Path)
        if (condition )==False:
            tkinter.messagebox.showinfo("error", "Please Enter valid path")
        else:
            print(self.File_Path)
            if self.File_Path == "":
                tkinter.messagebox.showinfo("error", "Please Enter file path")
            else:
                if self.File_Path[-3:] != "txt":
                    tkinter.messagebox.showinfo("error", "Please choose Proper file extension (.txt)")
                else:
                    self.master2.pack_forget()
                    self.master2.destroy()
                    self.master.pack_forget()
                    self.master.destroy()
                    self.master1.pack_forget()
                    self.master1.destroy()
                    ff = open(self.File_Path, "r",)

                    contents = ff.read()
                    ff.close()
                    self.f = frame3(self.newmaster,  contents)
                    self.f.show_Label(contents)

    def browse(self):
        self.File_Path = self.filedialog()
        print(self.File_Path)
        if self.File_Path == "":
            tkinter.messagebox.showinfo("error", "Please choose text file")
        else:
            if self.File_Path [-3:] != "txt":
                tkinter.messagebox.showinfo("error", "Please choose Proper file extension (.txt)")
            else :
                self.master2.pack_forget()
                self.master2.destroy()
                self.master.pack_forget()
                self.master.destroy()
                self.master1.pack_forget()
                self.master1.destroy()
                ff = open(self.File_Path, "r")
                contents = ff.read()
                ff.close()
                self.f = frame3(self.newmaster, contents)
                self.f.show_Label(contents)


    def show_Label(self):

        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"), width=1000, height=500)

        canvas = Canvas(self.master1)
        self.scroll = Frame(self.master1)
        self.scroll.pack(side=BOTTOM,fill="x")
        self.frame = Frame(canvas)
        myscrollbar = Scrollbar(self.master1, command=canvas.yview)
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


        self.text=Text(self.frame,width=500,height=600)
        self.text.pack(side=LEFT)

