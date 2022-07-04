from tkinter import *#載入函式庫
root = Tk() #建立一個視窗
for bordwidth in [0,1,2,3,4]:#建立五個按鈕
    Button(root,
    text = bordwidth,#顯示數字
    bd = bordwidth).pack()#邊框粗細設置
root.mainloop() #執行
