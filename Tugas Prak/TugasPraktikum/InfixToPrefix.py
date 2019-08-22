# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 09:24:13 2018

@author: Muhammad Rifky Y
"""

from UsedADT import Stack

class ITP:
    def __init__(self,txt,hitung=False):
        txt=txt.replace(" ","")
        self.txt=txt
        self.outtxt=""
        self.op=[["+","-"],["*","/"],["^"],["(",")"]]
        if hitung:
            self.txt=self.txt[::-1]
            self.ev()
        else:
            self.topostfix()
    
    def __str__(self):
        return self.outtxt
    
    def someoperator(self,i):
        for j in range(4):
            if self.txt[i] in self.op[j]:
                return 1
        return 0
    
    def someoperand(self,i):
        try:
            eval(self.txt[i])
            return True
        except:
            return False
    
    def topostfix(self):
        a={}
        a['0']=Stack()
        count=0
        tmp=""
        for i in range(len(self.txt)):
            con=self.someoperator(i)
            try:
                if self.txt[i]=="." or self.txt[i+1]==".":
                    if self.txt[i]=="." and bool(self.someoperator(i+1)):
                        eval()
                else:
                    eval(self.txt[i])
                    eval(self.txt[i+1])
                con=2
            except IndexError:
                if con==0:
                    if tmp=="":
                        self.outtxt+=self.txt[i]
                    else:
                        self.outtxt+=tmp+self.txt[i]+"("
                    break
            except:pass
            
            if con==0:
                if tmp=="":
                    self.outtxt+=self.txt[i]+" "
                else:
                    self.outtxt+=tmp+self.txt[i]+"("
                    tmp=""
                continue
            
            elif con==1:
                if self.txt[i]==")":
                    count+=1
                    a[str(count)]=Stack()
                elif self.txt[i]=="(":
                    while len(a[str(count)])!=0:
                        self.outtxt+=a[str(count)].pop()
                    count-=1
                  
                elif len(a[str(count)])!=0:
                    for j in range(3):
                        if a[str(count)].last() in self.op[j]:
                            kasta_old=j
                        if self.txt[i] in self.op[j]:
                            kasta_new=j
                    if kasta_old>kasta_new:
                        self.outtxt+=a[str(count)].pop()
                        a[str(count)].push(self.txt[i])
                    else:
                        a[str(count)].push(self.txt[i])
                    continue
                else:
                    a[str(count)].push(self.txt[i])
                    continue
            else:
                if tmp=="":
                    tmp+=")"+self.txt[i]
                else:
                    tmp+=self.txt[i]
        while len(a['0'])!=0:
            self.outtxt+=a['0'].pop()
        self.outtxt=self.outtxt[::-1]
        self.outtxt=self.outtxt.replace(" ","")
        return self.outtxt
    
    def ev(self):
        try:
            a=Stack()
            dalamkurung=False
            for i in range(len(self.txt)):
                if self.txt[i]=="(" or self.txt[i]==")":
                    dalamkurung= not dalamkurung
                    if dalamkurung:
                        tmp=""
                    else:
                        a.push(tmp)
                    continue
                if dalamkurung:
                  if tmp=="":
                      tmp+=self.txt[i]
                  else:
                      tmp=self.txt[i]+tmp
                  continue
                if self.someoperand(i):
                    a.push(self.txt[i])
                else:
                    sometxt=self.txt[i]
                    sometxt=sometxt.replace("^","**")
                    operasi=a.pop()+sometxt+a.pop()
                    a.push(str(eval(operasi)))
            if len(a)>1:
                self.outtxt="Prefix salah"
                return self.outtxt
            else:
                self.outtxt=a.pop()
                return eval(self.outtxt)
        except ZeroDivisionError:
            self.outtxt="Menghasilkan pembagi 0"
            return self.outtxt
        except:
            self.outtxt="Prefix salah"
            return self.outtxt