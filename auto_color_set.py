from tkinter import *
import tkinter.colorchooser

def xz():
    color=tkinter.colorchooser.askcolor()
    colorstr=str(color)
    print('打印字符串%s 切掉后=%s' % (colorstr,colorstr[-9:-2]))
    lb.config(text=colorstr[-9:-2],background=colorstr[-9:-2])

root = Tk()

lb = Label(root,text='請關注颜色的變化')
lb.pack()
btn=Button(root,text='弹出颜色選擇對話框',command=xz)
btn.pack()
root.mainloop()