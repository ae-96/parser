from tkinter import *
from PIL import Image
from Parser import Parser
import pydotplus
import tkinter.messagebox
from tkinter import filedialog
import  os

class frame3 :
    def __init__(self,master,contents):
        self.contents = contents
        self.pars=Parser(self.contents)
        self.main=master
        self.Master = Frame(master)
        self.Master.pack(side=TOP)
        self.master_will_be_deleted = Frame(master)
        self.master_will_be_deleted.pack(side=BOTTOM)
        self._4_buttons_master = Frame(self.main)
        self._4_buttons_master.pack(side=TOP)
        self.save = Frame(self.main)
        self.save.pack(side=BOTTOM)

        self.Scan_Button = Button(self.master_will_be_deleted, text=" PrintTree ", command=self.PrintTree, font="arial 15 italic", width=20)
        self.Scan_Button.pack(side=BOTTOM)

    def PrintTree(self):

        if self.pars.check_error() == 1 :
            tkinter.messagebox.showinfo("error", "Invalid Tokens ")
        else :
            self.pars.start_parsing()
            self.discription = self.pars.convert_to_string()
            ff = open( 'demo.dot',"w")
            ff.write(self.pars.convert_to_string())
            ff.close()
            graph_a = pydotplus.graph_from_dot_file('demo.dot')
            graph_a.write_png('OutputTree.png')
            os.remove('demo.dot')
            f = Image.open("OutputTree.png").show()

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