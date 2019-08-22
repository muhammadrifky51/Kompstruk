# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 19:34:15 2018

@author: Muhammad Rifky Y
"""

import tkinter as tk

class Nomor1(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.master=master
        self.findcount=0
        self.init_window()
        
    def init_window(self):
        self.master.title("Nomor 1")
        self.pack(fill=tk.BOTH,expand=1)
        
        tulisan1=tk.Label(self, text="Masukkan Matriks")
        tulisan1.pack()
        
        self.MyEntry=tk.Entry(self,width=50)
        self.MyEntry.pack()

        self.tulisan2=tk.Label(self.master,text="")
        self.tulisan2["text"]="Check Matriks (Restrict to 2 dimensional matrix)"
        self.tulisan2.place(anchor=tk.CENTER,x=300,y=65)
        
        self.CekButton=tk.Button(self.master,text="Check",command=self.CEKBUTTON)
        self.CekButton.place(height=25,anchor=tk.E,x=295,y=85)
        self.FindButton=tk.Button(self.master,text="Find Peak",state=tk.DISABLED,command=self.FINDBUTTON)
        self.FindButton.place(height=25,anchor=tk.W,x=305,y=85)
        
        self.tulisan3=tk.Label(self.master,text="")
        self.tulisan3.place(anchor=tk.N,x=300,y=110)
        
        self.master.bind('<Return>',self.ENTERKEY)
        
    def CEKBUTTON(self):
        if self.CekButton["text"]=="Check":
            if self.MyEntry.get()=="":
                self.tulisan2["text"]="Input kosong"
                self.tulisan2["fg"]="red"
                return
            try:
                self.matriks=eval(self.MyEntry.get())
                int(self.matriks)
                self.matriks=[self.matriks]
            except SyntaxError:
                self.tulisan2["text"]="Ada kesalahan penulisan pada matriks"
                self.tulisan2["fg"]="red"
                return
            except:
                pass
            if type(self.matriks)==tuple:
                self.matriks=list(self.matriks)
            if type(self.matriks[0])==tuple:
                for i in range(len(self.matriks)):
                    self.matriks[i]=list(self.matriks[i])
            try:
                self.matriks[0][0]
            except TypeError:
                self.matriks=[self.matriks]
            
            sebwahmatriks=True
            sebwahkata=""
            for i in range(len(self.matriks)):
                if sebwahmatriks==True and i!=len(self.matriks)-1:
                    if len(self.matriks[i])!=len(self.matriks[i+1]):
                        self.tulisan2["text"]="Matriks tidak valid"
                        self.tulisan2["fg"]="red"
                        self.FindButton["state"]=tk.DISABLED
                        sebwahmatriks=False
                for j in range(len(self.matriks[i])):
                    try:
                        int(self.matriks[i][j])
                    except TypeError:
                        self.tulisan2["text"]="Restrict to 2 dimensional matrix"
                        self.tulisan2["fg"]="red"
                        self.tulisan3["text"]=""
                        return
                    sebwahkata+=str(self.matriks[i][j])+" "
                sebwahkata+="\n"
            if sebwahmatriks==True:
                self.tulisan2["text"]="Matriks valid"
                self.tulisan2["fg"]="green"
                self.CekButton["text"]="Batal"
                self.MyEntry["state"]=tk.DISABLED
                self.FindButton["state"]=tk.NORMAL
            self.tulisan3["text"]=sebwahkata
        else:
            self.FindButton["state"]=tk.DISABLED
            self.MyEntry["state"]=tk.NORMAL
            self.CekButton["text"]="Check"
            
    def FINDBUTTON(self):
        if self.findcount==0:
            self.findcount=1
            peak=[]
            indeks=[]
            if len(self.matriks[0])==1 and len(self.matriks[0])==1:
                self.top=tk.Toplevel()
                self.top.geometry("210x50")
                self.top.title("Info")
                self.top.minsize(210,50)
                msg=tk.Label(self.top,text="Tidak ada peak element")
                msg.pack()
                self.top.protocol("WM_DELETE_WINDOW",self.CommandTopLevel)
            else:
                for i in range(len(self.matriks)):
                    for j in range(len(self.matriks[i])):
                        tes=self.matriks[i][j]
                        if j-1>=0 and tes<=self.matriks[i][j-1]:
                            continue
                        if i-1>=0 and tes<=self.matriks[i-1][j]:
                            continue
                        if j+1<len(self.matriks[i]) and tes<=self.matriks[i][j+1]:
                            continue
                        if i+1<len(self.matriks) and tes<=self.matriks[i+1][j]:
                            continue
                        indeks.append((i+1,j+1))
                        peak.append(tes)
                if len(peak)!=0:
                    txt="Peak element: \n"
                    j=0
                    for i in range(len(peak)):
                        if j+1==len(peak):
                            txt+=str(peak[i])+" {0}".format(indeks[i])
                        elif (j+1)%3==0:
                            txt+=str(peak[i])+" {0},\n".format(indeks[i])
                        else:
                            txt+=str(peak[i])+" {0}, ".format(indeks[i])
                        j+=1
                else:
                    txt="Tidak ada peak"
                self.top=tk.Toplevel()
                self.top.geometry("300x100")
                self.top.title("Jawaban:")
                self.top.minsize(300,100)
                msg=tk.Label(self.top,text="")
                msg["text"]=txt
                msg.pack()
                self.top.protocol("WM_DELETE_WINDOW",self.CommandTopLevel)
                
    def CommandTopLevel(self):
        self.FindButton["state"]=tk.DISABLED
        self.MyEntry["state"]=tk.NORMAL
        self.CekButton["text"]="Check"
        self.tulisan3["text"]=""
        self.findcount=0
        self.top.destroy()
        
    def ENTERKEY(self,event):
        self.CEKBUTTON()