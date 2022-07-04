# -*- coding:utf-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import *
root = Tk()
root.geometry("360x360+150+150")
root.update()
x = root.winfo_x()
y = root.winfo_y()
var = StringVar()
#用toplevel調整調色盤
t1 = Toplevel()
t1.geometry("+%d+%d" %(x+250,y+100))
#隱藏toplevel
t1.withdraw()
#顯示調色盤
def display_palette():
    (rgb,hx)=askcolor(parent=t1)
    root.config(bg=hx)
    var.set(hx)
    h1=hx[1:3]
    h2=hx[3:5]
    h3=hx[5:7]
    s1.set(int(h1,16))
    s2.set(int(h2,16))
    s3.set(int(h3,16))
#通過尺度條課度值調整顏色
def updatecolor_scale(args):
    red = s1.get()
    green = s2.get()
    blue = s3.get()
    mycolor="#%02x%02x%02x"%(red,green,blue)
    root.config(bg=mycolor)
    var.set(mycolor)
#通過輸入值調整顏色
def updatecolor_entry(args):
    hexcolor = var.get()
    if not hexcolor.startswith('#',0,1):
        messagebox.showwarning(message='請以#開始')
    if len(hexcolor) != 7:
        messagebox.showwarning(message='輸入數值在"#000000-#FFFFFF"之間')
    try:
        h1=hexcolor[1:3]
        h2=hexcolor[3:5]
        h3=hexcolor[5:7]
        s1.set(int(h1,16))
        s2.set(int(h2,16))
        s3.set(int(h3,16))
        root.config(bg=hexcolor)
    except:
        root.config(bg='#FFFFFF')
        s1.set(255)
        s2.set(255)
        s3.set(255)
#設計尺度條定位初始值
s1 = Scale(root,from_=0,to=255,length=230,command=updatecolor_scale,orient='horizontal')
s2 = Scale(root,from_=0,to=255,length=230,command=updatecolor_scale,orient='horizontal')
s3 = Scale(root,from_=0,to=255,length=230,command=updatecolor_scale,orient='horizontal')
s1.set(255)
s2.set(255)
s3.set(255)
#通過尺度條數值轉換成16進制顏色表示
hexs1=hex(s1.get()).lstrip('0x')
hexs2=hex(s2.get()).lstrip('0x')
hexs3=hex(s3.get()).lstrip('0x')
var.set('#'+hexs1+hexs2+hexs3)
l=Label(root,text='color(16)請輸入:')
e=Entry(root,width=20,textvariable=var)
e.bind('<Return>',updatecolor_entry)
b=Button(root,text='顯示調色盤',command=display_palette)
#各主鍵定位
s1.grid(row=0,columnspan=2,sticky='w')
s2.grid(row=1,columnspan=2,sticky='w')
s3.grid(row=2,columnspan=2,sticky='w')
l.grid(row=3,column=0,sticky='w')
e.grid(row=3,column=1,sticky='w')
b.grid(row=4,sticky='w')
root.mainloop()