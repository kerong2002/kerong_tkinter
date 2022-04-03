#2022-03-09 陳科融
#時鐘
from tkinter import *
import time
kerong=Tk()
kerong.title("time")
kerong.configure(bg='black')
kerong.geometry("750x200+500+200")
set1=Label(kerong,
    font=("arial", 60, "bold")
    , bg="black", fg="white")
set1.pack(anchor="center", fill="both", expand=1)
mode="clock"

def show():
    if (mode=="clock"):
        save=time.strftime('%p %H:%M:%S')
    else:
        save=time.strftime('%Y年 %m月 %d日')
    set1.config(text=save)
    set1.after(1000, show)
def mouse_touch(event):
    global mode
    if(mode=="clock"):
        mode="date"
    else:
        mode="clock"
set1.bind("<Button>", mouse_touch)
show()
mainloop()