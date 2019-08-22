# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 19:34:15 2018

@author: Muhammad Rifky Y
"""

import tkinter as tk
from Nomor1 import Nomor1
from Nomor2 import Nomor2
import Nomor3V2 
import Nomor3V1 
try:
    import winsound
except:
    pass

class MainWindow(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.master=master
        self.init_window()
        self.aboutcount=0
        self.iswindowactive=0
        self.kelarcount=0
        
    def init_window(self):
        self.master.title("Tugas Praktikum")
        self.pack(fill=tk.BOTH,expand=1)
        
        label1=tk.Label(self,text="Tugas Praktikum\nKomputasi Terstruktur")
        label1.pack()
        
        MyMenu=tk.Menu(self.master)
        self.master.config(menu=MyMenu)
        
        helpmenu=tk.Menu(MyMenu,tearoff=False)
        helpmenu.add_command(label="About",command=self.AboutButton)
        MyMenu.add_cascade(label="Help",menu=helpmenu)
        
        self.tkvar=tk.StringVar(self)
        self.pilihan=["Nomor 1","Nomor 2","Nomor 3"]
        self.tkvar.set("Nomor 1")
        popupMenu=tk.OptionMenu(self,self.tkvar,*self.pilihan)
        popupMenu.config(width=10)
        popupMenu.place(anchor=tk.CENTER,x=70,y=65)
        
        self.GoButton=tk.Button(self.master,text="GO",command=self.GOBUTTON)
        self.GoButton.place(anchor=tk.W,x=150,y=65)
        
        self.master.bind('<Up>',self.UPKEY)
        self.master.bind('<Down>',self.DOWNKEY)
        self.master.bind('<Return>',self.ENTERKEY)
        
    def AboutButton(self):
        if self.aboutcount==0:
            self.aboutcount=1
            self.top=tk.Toplevel()
            self.top.geometry("210x50")
            self.top.title("About Me")
            msg=tk.Label(self.top,text="Muhammad Rifky Yusdiansyah\n1506671423")
            msg.pack()
            self.top.protocol("WM_DELETE_WINDOW",self.CommandTopLevel)
   
    def GOBUTTON(self):
        if self.iswindowactive==0:
            self.iswindowactive=1
            self.GoButton['state']=tk.DISABLED
            if self.tkvar.get()=="Nomor 1":
                self.root=tk.Tk()
                self.root.geometry("600x400")
                self.root.minsize(600,400)
                self.app=Nomor1(self.root)
                self.root.protocol("WM_DELETE_WINDOW",self.CloseWindow)
                self.app.mainloop()
            elif self.tkvar.get()=="Nomor 2":
                self.root=tk.Tk()
                self.root.geometry("600x400")
                self.root.minsize(600,400)
                self.app=Nomor2(self.root)
                self.root.protocol("WM_DELETE_WINDOW",self.CloseWindow)
                self.app.mainloop()
            else:
                try:
                    import PIL
                    import graphviz
                    self.root=tk.Tk()
                    self.root.geometry("600x400")
                    self.root.minsize(600,400)
                    self.app=Nomor3V2.Nomor3(self.root)
                    self.root.protocol("WM_DELETE_WINDOW",self.CloseWindow)
                    self.app.mainloop()
                except:
                    self.top2=tk.Toplevel()
                    try:winsound.PlaySound('SystemAsterisk',winsound.SND_ALIAS|winsound.SND_ASYNC)
                    except:pass
                    self.top2.geometry("300x50")
                    self.top2.minsize(300,50)
                    msg=tk.Label(self.top2,text="We can't find Pillow or/and graphviz module\nWe run Nomor3V1 instead of Nomor3V2")
                    msg.pack()
                    self.root=tk.Tk()
                    self.root.geometry("600x400")
                    self.root.minsize(600,400)
                    self.app=Nomor3V1.Nomor3(self.root)
                    self.root.protocol("WM_DELETE_WINDOW",self.CloseWindow)
                    self.app.mainloop()
                    
    def CloseWindow(self):
        self.GoButton['state']=tk.NORMAL
        self.iswindowactive=0
        self.root.destroy()
        try:
            self.app.top.destroy()
        except:
            pass
    
    def CommandTopLevel(self):
        self.aboutcount=0
        self.top.destroy()
        
    def DOWNKEY(self,event):
        if self.pilihan.index(self.tkvar.get())+1<len(self.pilihan):
            tmp=self.pilihan.index(self.tkvar.get())+1
            self.tkvar.set(self.pilihan[tmp])
            
    def UPKEY(self,event):
        if self.pilihan.index(self.tkvar.get())-1>=0:
            tmp=self.pilihan.index(self.tkvar.get())-1
            self.tkvar.set(self.pilihan[tmp])  
    
    def ENTERKEY(self,event):
        if self.GoButton['state']==tk.NORMAL:
            self.GOBUTTON()
            
    def KELAR(self):
        try:
            winsound.PlaySound('SystemAsterisk',winsound.SND_ALIAS|winsound.SND_ASYNC)
        except:
            pass
        if self.kelarcount==0:
            self.kelarcount+=1
            self.top1=tk.Toplevel()
            self.top1.geometry("210x50")
            self.top1.minsize(210,50)
            msg=tk.Label(self.top1,text="KELAR TUGAS GUA COY\nKasih 100, cape pake tkinter")
            msg.pack()
            self.top1.protocol("WM_DELETE_WINDOW",self.BENERANKELAR)
            self.master.protocol("WM_DELETE_WINDOW",self.BENERANKELAR)
    
    def BENERANKELAR(self):
        self.top1.destroy()
        self.master.destroy()        
        try:self.root.destroy()
        except:pass
        try:self.top2.destroy()
        except:pass
