from tkinter import *#載入函式庫
#函式，使Button消失
def hide_me(event):
    print('done')
    event.widget.place_forget()
root = Tk()#建立視窗
b1=Button(root, text="Click")#顯示字串
b1.bind("<Button-1>", hide_me)#事件，當按下滑鼠#左鍵一下，呼叫函式
b1.place(y=20,x=30)#建立Button
root.mainloop()
