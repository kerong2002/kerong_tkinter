#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
window =Tk()
window.title('my window')
window.geometry('200x150')

width_combobox = ttk.Combobox(window)
width_combobox['values'] = tuple([i for i in range(4, 37)])
width_combobox.pack(pady=10)
width_combobox.current(0)

window.mainloop()