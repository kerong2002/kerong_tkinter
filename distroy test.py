#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 下午1:23
# @Author  : wangying
# @Site    :
# @File    : 测试.py
# @Software: PyCharm


from tkinter import *
from tkinter import ttk

jason_file_path = '测试数据.txt'


def new_window():
    print("新建窗口")
    otherFrame = Toplevel()
    otherFrame.geometry("400x300+200+200")
    otherFrame.title("otherFrame")
    handler = lambda: onCloseOtherFrame(otherFrame)
    Text(otherFrame, width=300, height=200)

    btn = Button(otherFrame, text="保存文件", command=handler)
    btn.pack()
    # w1.insert(1.0, read_jason_data())
    # w1.pack()
    pass


def onCloseOtherFrame(otherFrame):
    """"""
    otherFrame.destroy()
    show()


def show():
    """
    shows main frame
    """
    root.update()
    root.deiconify()


def read_jason_data():
    with open(jason_file_path) as f:
        jason_data = f.read()
        return jason_data


def write_jason_data(data):
    with open(jason_file_path, 'w') as f:
        f.write(data)


def showText():
    w1.insert(1.0, read_jason_data())
    w1.pack()
    pass


def hiddenText():
    write_jason_data(w1.get(1.0, END))
    w1.delete(1.0, 'end')
    w1.pack_forget()
    pass


root = Tk()
root.geometry('600x300+200+200')

Button(root, text='新建窗口', command=new_window, ).pack(side='left')

Button(root, text='显示', command=showText, ).pack(side='left')
Button(root, text='保存', command=hiddenText, ).pack(side='left')

w1 = Text(root, width=300, height=200)
# w1.pack_forget()
w1.pack(side='left')

root.mainloop()

