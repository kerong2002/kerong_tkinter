#2022-03-11 陳科融
#骰寶
from tkinter import *
window=Tk()
window.title("game")
window.configure(bg='skyblue')
window.geometry("650x500+400+200")
small_B=PhotoImage(file=r"C:\Users\krame\OneDrive\桌面\練習程式py\tkinter\small.PNG")
B_small=Button(image=small_B).pack()
png_111=PhotoImage(file=r"C:\Users\krame\OneDrive\桌面\練習程式py\tkinter\111.PNG") 
B_111=Button(image=png_111).pack()
png_222=PhotoImage(file=r"C:\Users\krame\OneDrive\桌面\練習程式py\tkinter\222.PNG") 
B_222=Button(image=png_222).pack()
png_333=PhotoImage(file=r"C:\Users\krame\OneDrive\桌面\練習程式py\tkinter\333.PNG") 
B_333=Button(image=png_333).pack()
png_any=PhotoImage(file=r"C:\Users\krame\OneDrive\桌面\練習程式py\tkinter\any.PNG") 
B_any=Button(image=png_any).pack()
png_444=PhotoImage(file=r"C:\Users\krame\OneDrive\桌面\練習程式py\tkinter\444.PNG") 
B_444=Button(image=png_444).pack()
png_555=PhotoImage(file=r"C:\Users\krame\OneDrive\桌面\練習程式py\tkinter\555.PNG") 
B_555=Button(image=png_555).pack()
png_666=PhotoImage(file=r"C:\Users\krame\OneDrive\桌面\練習程式py\tkinter\666.PNG") 
B_666=Button(image=png_666).pack()
# #===========================================<game>==========================================================
# number = ["小","小","小","111","111","any","any","any","any","444","444","大","大","大",
#           "小","小","小","222","222","any","any","any","any","555","555","大","大","大",
#           "小","小","小","333","333","any","any","any","any","666","666","大","大","大",
#           "4","5","6","7","8","9","10","11","12","13","14","15","16","17",
#           " ","1","1","2","2","3","3","4","4","5","5","6","6"," "]
# small_B=Button(window,text ="小",
#                         width =15,#按鍵寬度
#                         height=10,#按鍵高度
#                 font=('arial', 10),#按鍵字形
#                     bg="orange")#按鍵顏色
# small_B.place(y=5,x=5)
# big_B=Button(window,text ="大",
#                         width =15,#按鍵寬度
#                         height=10,#按鍵高度
#                 font=('arial', 10),#按鍵字形
#                     bg="orange")#按鍵顏色
# big_B.place(y=5,x=500)
# y=1
# x=0
# for i in range(0,70):
#     b1=Button(window,#視窗名稱
#     text = number[i],#顯示字串
#     width =5,#按鍵寬度
#     height=5,
#     font=('arial', 10),
#     bg="orange")
#     # b1.bind("<Button-1>", touch)#左鍵
#     x=i%14
#     b1.place(y=80*y,x=80*x+10) #按鍵位置
#     if(i%14==0):
#         y+=1
window.mainloop()