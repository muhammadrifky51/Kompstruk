# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 00:36:02 2018

@author: Muhammad Rifky Y
"""

import tkinter as tk
from InfixToPrefix import ITP

class Nomor2(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.master=master
        self.CopyVisible=True
        self.init=True
        self.ischecked=False
        self.smth=0
        self.init_window()
        
    def init_window(self):
        self.master.title("Nomor 2")
        self.pack(fill=tk.BOTH,expand=1)
        
        self.tulisan1=tk.Label(self, text="Masukkan ekspresi infiks")
        self.tulisan1.pack()
        
        self.MyEntry=tk.Entry(self,width=50)
        self.MyEntry.place(anchor=tk.E,x=500,y=40)
        self.CheckBox=tk.Checkbutton(self,command=self.CHECKBOX)
        self.CheckBox.place(anchor=tk.W,x=505,y=40)
        tulisan4=tk.Label(self,text="Hitung?")
        tulisan4.place(anchor=tk.W,x=525,y=40)
        tulisan4.bind('<Button-1>',self.IFGAPAS)
        
        self.tulisan2=tk.Label(self, text="")
        self.tulisan2["text"]="Is it infix expression?"
        self.tulisan2.place(anchor=tk.CENTER,x=300,y=65)
        self.inpoh=self.tulisan2.place_info()
        
        self.CekButton=tk.Button(self.master,text="Check",command=self.CEKBUTTON)
        self.CekButton.place(height=25,anchor=tk.E,x=295,y=85)
        self.FindButton=tk.Button(self.master,text="Convert",state=tk.DISABLED,command=self.FINDBUTTON)
        self.FindButton.place(height=25,anchor=tk.W,x=305,y=85)
        self.CopyButton=tk.Button(self.master,text="Copy",command=self.COPYBUTTON)
        self.CopyButton.place(height=25,anchor=tk.CENTER,x=300,y=150)
        self.CopyButtonLoc=self.CopyButton.place_info()
        
        self.tulisan3=tk.Label(self.master,text="")
        self.tulisan3.place(anchor=tk.N,x=300,y=110)
        
        if self.init:
            self.VANISH()
    
    def CEKBUTTON(self):
        if self.CekButton['text']=="Check":
            self.tulisan3['text']=""
            if not self.ischecked:
                if self.CopyVisible:
                    self.VANISH()
                if self.MyEntry.get()=="":
                    self.tulisan2["text"]="The input is blank"
                    self.tulisan2["fg"]="red"
                    self.tulisan3["text"]=""
                    return
                testinfix=self.MyEntry.get()
                try:
                    testinfix=testinfix.replace("^","**")
                    eval(testinfix)
                except SyntaxError:
                    self.tulisan2["text"]="Not an infix expression"
                    self.tulisan2["fg"]="red"
                    self.tulisan3["text"]=""
                    return
                except NameError:pass
                testinfix=testinfix.replace("**","^")
                testinfix=testinfix[::-1]     
                self.hasil=ITP(testinfix)
                self.tulisan2['text']="Input valid"
                self.tulisan2['fg']='green'
                self.MyEntry['state']=tk.DISABLED
                self.CekButton['text']="Batal"
                self.FindButton['state']=tk.NORMAL
                self.CheckBox['state']=tk.DISABLED
            else:
                if self.MyEntry.get()=="":
                    self.tulisan2['text']="Input kosong"
                    self.tulisan2['fg']='red'
                    self.tulisan3['text']=""
                    return
                try:
                    if self.MyEntry.get()[-1]!=")":
                        eval(self.MyEntry.get()[-1])
                    eval(str(ITP(self.MyEntry.get(),hitung=True)))
                except NameError:
                    self.tulisan2['text']="Tidak bisa menghitung variabel kosong"
                    self.tulisan2['fg']='red'
                    self.tulisan3['text']=""
                    return
                except:
                    self.smth+=1
                    if self.smth==2:
                        self.tulisan2['text']=str(ITP(self.MyEntry.get(),hitung=True))+"\nYou can try Convert to prefix expression first\nAnd press copy"
                        self.smth=0
                        self.tulisan2.place(anchor=tk.CENTER,x=300,y=160)
                    else:
                        self.tulisan2['text']=str(ITP(self.MyEntry.get(),hitung=True))
                        self.tulisan2.place(self.inpoh)
                    self.tulisan2['fg']='red'
                    self.tulisan3['text']=""
                    return
                self.hasil=ITP(self.MyEntry.get(),hitung=True)
                self.tulisan2['text']="Input valid"
                self.tulisan2['fg']='green'
                self.MyEntry['state']=tk.DISABLED
                self.CekButton['text']="Batal"
                self.FindButton['state']=tk.NORMAL
                self.CheckBox['state']=tk.DISABLED
        else:
            self.tulisan2['text']="Is it infix expression?"
            self.tulisan2['fg']="SystemButtonText"
            self.tulisan2.place(self.inpoh)
            self.tulisan3["text"]=""
            self.CekButton['text']="Check"
            self.FindButton['state']=tk.DISABLED
            self.MyEntry['state']=tk.NORMAL
            self.CheckBox['state']=tk.NORMAL
            
    def FINDBUTTON(self):
        self.tulisan3['text']=self.hasil
        if not self.ischecked:
            self.tulisan2['text']="Is it infix expression?"
        else:
            self.tulisan2['text']="Is it prefix expression?"
        self.tulisan2['fg']="SystemButtonText"
        self.CekButton['text']="Check"
        self.FindButton['state']=tk.DISABLED
        self.MyEntry['state']=tk.NORMAL
        self.CheckBox['state']=tk.NORMAL
        if not self.ischecked:
            self.VANISH()
        
    def VANISH(self):
        if self.CopyVisible:
            self.CopyButton.place_forget()
        else:
            self.CopyButton.place(self.CopyButtonLoc)
        self.CopyVisible = not self.CopyVisible
        
    def COPYBUTTON(self):
        tocopy=tk.Tk()
        tocopy.withdraw()
        tocopy.clipboard_clear()
        tocopy.clipboard_append(self.tulisan3["text"])
        self.tulisan3["text"]="Text Copied!"
        self.MyEntry.delete(0,'end')
        tocopy.update()
        tocopy.destroy()
        self.VANISH()
        
    def CHECKBOX(self):
        self.tulisan2.place(self.inpoh)
        if not self.ischecked:
            self.tulisan1["text"]="Masukkan ekspresi prefiks"
            self.tulisan2["text"]="Is it prefix expression?"
            self.FindButton["text"]="Evaluate"
        else:
            self.tulisan1["text"]="Masukkan ekspresi infiks"
            self.tulisan2["text"]="Is it infix expression?"
            self.FindButton["text"]="Convert"
        self.tulisan3["text"]=""
        self.MyEntry.delete(0,'end')
        self.tulisan2["fg"]="SystemButtonText"
        self.ischecked=not self.ischecked

    def IFGAPAS(self,event):
        self.CheckBox.invoke()