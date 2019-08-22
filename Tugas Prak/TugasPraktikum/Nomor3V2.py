# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 11:42:33 2018

@author: Muhammad Rifky Y
"""

import sys
import tkinter as tk
from graphviz import Graph
from UsedADT import Node,DLL,BinaryTree
from PIL import Image, ImageTk
sys.path.insert(0,'..')

class Nomor3(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.master=master
        self.findcount=0
        self.init_window()
        self.ischecked=False
        
    def init_window(self):
        self.master.title("Nomor 3 V2")
        self.pack(fill=tk.BOTH,expand=1)
        
        self.tulisan1=tk.Label(self, text="Masukkan kumpulan bilangan berbeda")
        self.tulisan1.pack()
        
        self.MyEntry=tk.Entry(self,width=50)
        self.MyEntry.place(anchor=tk.E,x=500,y=40)
        self.CheckBox=tk.Checkbutton(self,command=self.CHECKBOX)
        self.CheckBox.place(anchor=tk.W,x=505,y=40)
        tulisan4=tk.Label(self,text="Sort?")
        tulisan4.place(anchor=tk.W,x=525,y=40)
        tulisan4.bind('<Button-1>',self.IFGAPAS)
        
        self.tulisan2=tk.Label(self, text="")
        self.tulisan2["text"]="Is it really a set of numbers?"
        self.tulisan2.place(anchor=tk.CENTER,x=300,y=65)
        
        self.CekButton=tk.Button(self.master,text="Check",command=self.CEKBUTTON)
        self.CekButton.place(height=25,anchor=tk.E,x=295,y=85)
        self.FindButton=tk.Button(self.master,text="Find Family",state=tk.DISABLED,command=self.FINDBUTTON)
        self.FindButton.place(height=25,anchor=tk.W,x=305,y=85)
        
        self.tulisan3=tk.Label(self.master,text="")
        self.tulisan3.place(anchor=tk.N,x=300,y=110)
        
    
    def CEKBUTTON(self):
        if self.CekButton['text']=="Check":
            if self.MyEntry.get()=="":
                self.tulisan2["text"]="The input is blank"
                self.tulisan2["fg"]="red"
                self.tulisan3["text"]=""
                return
            testing=eval(self.MyEntry.get())
            for i in testing:
                try:
                    eval(str(i))
                except:
                    self.tulisan2["text"]="Tidak semuanya angka"
                    self.tulisan2["fg"]="red"
                    self.tulisan3["text"]=""
                    return
            if not self.ischecked:
                for i in testing:
                    if testing.count(i)>1:
                        self.tulisan2["text"]="Angka-angka tidak unique"
                        self.tulisan2["fg"]="red"
                        self.tulisan3["text"]=""
                        return
            nodes=[]
            if not self.ischecked:
                dot=Graph(format='png')
                somevar1={}
                somevar2={}
                for i in range(len(testing)):
                    somevar1[chr(65+i)]=str(testing[i])
                    somevar2[str(testing[i])]=chr(65+i)
                for i in range(len(testing)):
                    dot.node(somevar2[str(testing[i])],str(testing[i]))
            for i in testing:
                nodes.append(Node(i))
            track=DLL()
            for i in nodes:
                track.push_back(i)
            if self.ischecked:
                track.sort()
                self.hasil=str(track.print_list())
                self.tulisan2['text']="Input valid"
                self.tulisan2['fg']="green"
                self.tulisan3['text']=""
                self.MyEntry['state']=tk.DISABLED
            else:
                BT=BinaryTree()
                self.hasil=BT.insert(track)
                somecon=[]
                for i in range(len(track)):
                    current_pointer=self.hasil.search(eval(str(testing[i])))
                    if isinstance(current_pointer.left,BinaryTree):
                        if isinstance(current_pointer.right,BinaryTree):
                            somecon.append(somevar2[str(current_pointer.root)]+somevar2[str(current_pointer.left.root)])
                            somecon.append(somevar2[str(current_pointer.root)]+somevar2[str(current_pointer.right.root)])
                        else:
                            somecon.append(somevar2[str(current_pointer.root)]+somevar2[str(current_pointer.left.root)])
                dot.edges(somecon) #Look at this https://pypi.org/project/graphviz/ and https://stackoverflow.com/questions/26653929/pdf-viewer-for-python-tkinter
                dot.render('tree-output/BinaryTree')
                self.tulisan2['text']="Input sebuah angka"
                self.tulisan2['fg']="SystemButtonText"
                self.tulisan3['text']=str(self.hasil)
            self.CheckBox['state']=tk.DISABLED
            self.CekButton['text']="Batal"
            self.FindButton['state']=tk.NORMAL
            self.MyEntry.delete(0,'end')
            if not self.ischecked:
                load=Image.open('tree-output/BinaryTree.png')
                load=load.resize((350,350),Image.ANTIALIAS)
                render=ImageTk.PhotoImage(load)
                self.top1=tk.Toplevel()
                self.top1.geometry("400x400")
                self.top1.minsize(350,350)
                img=tk.Label(self.top1,image=render)
                img.image=render
                img.pack()
                self.top1.protocol("WM_DELETE_WINDOW",self.CommandTop2)
        else:
            self.CekButton['text']="Check"
            self.tulisan2['text']="Is it really a set of numbers?"
            self.tulisan2['fg']="SystemButtonText"
            self.tulisan3['text']=""
            self.MyEntry['state']=tk.NORMAL
            self.CheckBox['state']=tk.NORMAL
            self.FindButton['state']=tk.DISABLED
            self.MyEntry.delete(0,'end')
            try: self.top1.destroy()
            except:pass
            try:self.top.destroy()
            except:pass
    
    def FINDBUTTON(self):
        if not self.findcount:
            if self.ischecked:
                self.CekButton['text']="Check"
                self.tulisan2['text']="Is it really a set of numbers?"
                self.tulisan2['fg']="SystemButtonText"
                self.tulisan3['text']=self.hasil
                self.CheckBox['state']=tk.NORMAL
                self.FindButton['state']=tk.DISABLED
                self.MyEntry['state']=tk.NORMAL
                self.MyEntry.delete(0,'end')
            else: 
                if self.MyEntry.get()=="":
                    self.tulisan2["text"]="The input is blank"
                    self.tulisan2["fg"]="red"
                    return
                testing=eval(self.MyEntry.get())
                try:
                    int(testing)
                except:
                    self.tulisan2["text"]="Hanya masukkan angka"
                    self.tulisan2["fg"]="red"
                    return
                self.findcount=1
                if self.hasil.search(testing) is None:
                    self.tulisan2["text"]="Tidak ditemukan keluarga"
                    self.tulisan2["fg"]="red"
                    self.top=tk.Toplevel()
                    self.top.geometry("300x75")
                    self.top.minsize(300,75)
                    self.top.title("Keluarga dari "+str(testing))
                    self.CekButton['state']=tk.DISABLED
                    self.MyEntry['state']=tk.DISABLED
                    msg=tk.Label(self.top,text="Parent: None\nChildren: None")
                    msg.pack()
                    self.top.protocol("WM_DELETE_WINDOW",self.CommandTopLevel)
                    return
                tmp=self.hasil.search(testing)
                self.tulisan2["text"]="Keluarga ditemukan"
                self.tulisan2["fg"]="green"
                self.top=tk.Toplevel()
                self.top.geometry("300x75")
                self.top.minsize(300,75)
                self.top.title("Keluarga dari "+str(testing))
                self.CekButton['state']=tk.DISABLED
                self.MyEntry['state']=tk.DISABLED
                if isinstance(tmp.left,BinaryTree):
                    if isinstance(tmp.right,BinaryTree):
                        txt="Parent: {0}\nChildren:{1},{2}".format(tmp.prev,tmp.left.root,tmp.right.root)
                    else:
                        txt="Parent: {0}\nChild:{1},{2}".format(tmp.prev,tmp.left.root,tmp.right)
                else:
                    txt="Parent: {0}\nChildren:{1},{2}".format(tmp.prev,tmp.left,tmp.right)
                msg=tk.Label(self.top,text=txt)
                msg.pack()
                self.top.protocol("WM_DELETE_WINDOW",self.CommandTopLevel)
                return
            
    def CommandTopLevel(self):
        self.findcount=0
        self.CekButton['state']=tk.NORMAL
        self.MyEntry['state']=tk.NORMAL
        self.tulisan2['text']="Input sebuah angka"
        self.tulisan2['fg']="SystemButtonText"
        self.top.destroy()
    
    def CHECKBOX(self):
        if self.ischecked:
            self.FindButton['text']="Find Family"
        else:
            self.FindButton['text']="Start Sorting"
        self.tulisan3["text"]=""
        self.ischecked=not self.ischecked

    def CommandTop2(self):
        self.top1.destroy()
        self.CekButton['text']="Check"
        self.tulisan2['text']="Is it really a set of numbers?"
        self.tulisan2['fg']="SystemButtonText"
        self.tulisan3['text']=""
        self.MyEntry['state']=tk.NORMAL
        self.CheckBox['state']=tk.NORMAL
        self.FindButton['state']=tk.DISABLED
        self.MyEntry.delete(0,'end')
        try:self.top.destroy()
        except:pass
        
    def IFGAPAS(self,event):
        self.CheckBox.invoke()