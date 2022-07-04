from tkinter import *#載入函式庫
window = Tk()#建立一個視窗
window.geometry("510x670+400+70")
Button(window,text="FLAT",width=10,height=5,relief=FLAT).pack()
Button(window,text="GROOVE",width=10,height=5,relief=GROOVE).pack()
Button(window,text="RAISED",width=10,height=5,relief=RAISED).pack()
Button(window,text="RIDGE",width=10,height=5,relief=RIDGE).pack()
Button(window,text="SOLID",width=10,height=5,relief=SOLID).pack()
Button(window,text="SUNKEN",width=10,height=5,relief=SUNKEN).pack()
window.mainloop()#執行
