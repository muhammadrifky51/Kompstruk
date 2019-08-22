# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 19:34:15 2018

@author: Muhammad Rifky Y
"""

import tkinter as tk
import sys
sys.path.insert(0,'TugasPraktikum')
from MainWindow import MainWindow
    
root=tk.Tk()
root.geometry("200x100")
root.resizable(False,False)
app=MainWindow(root)
root.protocol("WM_DELETE_WINDOW",app.KELAR)
app.mainloop()