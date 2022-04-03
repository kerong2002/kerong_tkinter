#2022-03-09 陳科融
#計算機
from tkinter import *
window=Tk()
window.title("calculate")
window.configure(bg='skyblue')
window.geometry("340x500+900+200")

answer = StringVar()
answer.set("0")
text=""
Entry(window,textvariable=answer, font=('arial', 20)).place(x=15,y=15,width=300,height=40)

number = ["C","/","*","-",
          "7","8","9","+",
          "4","5","6","+",
          "1","2","3","=",
          "0","0",".","="]
def touch(event):
    global text
    if event.widget["text"]=="=":
        answer.set(str(eval(text)))
    elif event.widget["text"]=="C":
        answer.set('0')
        text=""
    else:
        text+=event.widget["text"]
        answer.set(text)
y=1
x=0
for i in range(0,20):
    if(i==7 or i==15):
        size=9
    else:
        size=4
    if(i==11 or i==19):
        y+=1
        x=0 
        continue
    if(i==17):
        x+=1
        continue
    if(i==16):
        row=18
    else:
        row=8
    b1=Button(window,#視窗名稱
    text = number[i],#顯示字串
    width = row,#按鍵寬度
    height=size,
    font=('arial', 10),
    bg="orange")
    b1.bind("<Button-1>", touch)#左鍵
    b1.place(y=80*y,x=80*x+10) #按鍵位置
    x+=1
    if((x%4)==0):
        y+=1
        x=0

window.mainloop()