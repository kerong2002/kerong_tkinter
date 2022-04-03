#2022-03-16 陳科融
#papper scissors stone
win_combination = [["2", "1"], ["3","2"], ["1","3"]]
from tkinter import *
from random import randint
window=Tk()
window.title("Tic-tac-toe")
window.configure(bg='skyblue')
window.geometry("900x700+100+50")
data=[' ','剪刀','石頭','布']
round=[0,0,0]
all_round=StringVar()
all_round.set('')
text1=StringVar()
text1.set('')
def s_touch(event):
    global round
    B=str(randint(1,3))
    A='1'
    if A == B:
        text1.set('電腦出'+data[int(B)]+'平手')
        round[0]+=1        
    elif [A, B] in win_combination:
        text1.set('電腦出'+data[int(B)]+'你贏了')
        round[1]+=1  
    else:
        text1.set('電腦出'+data[int(B)]+'你輸了')
        round[2]+=1  
    all_round.set('目前'+str(round[0])+'平手'+str(round[1])+'勝'+str(round[2])+'敗')
def r_touch(event):
    global round
    B=str(randint(1,3))
    A='2'
    if A == B:
        text1.set('電腦出'+data[int(B)]+'平手')
        round[0]+=1  
    elif [A, B] in win_combination:
        text1.set('電腦出'+data[int(B)]+'你贏了')
        round[1]+=1  
    else:
        text1.set('電腦出'+data[int(B)]+'你輸了')
        round[2]+=1
    all_round.set('目前'+str(round[0])+'平手'+str(round[1])+'勝'+str(round[2])+'敗')  
def p_touch(event):
    global round
    B=str(randint(1,3))
    A='3'
    if A == B:
        text1.set('電腦出'+data[int(B)]+'平手')
        round[0]+=1
    elif [A, B] in win_combination:        
        text1.set('電腦出'+data[int(B)]+'你贏了')
        round[1]+=1
    else:
        text1.set('電腦出'+data[int(B)]+'你輸了')
        round[2]+=1
    all_round.set('目前'+str(round[0])+'平手'+str(round[1])+'勝'+str(round[2])+'敗')  
png_papper=PhotoImage(file=r"C:\Users\krame\OneDrive\桌面\練習程式py\tkinter\papper.png") 
papper=Button(image=png_papper)
papper.bind("<Button-1>",p_touch)
papper.place(y=100,x=2)
png_scissors=PhotoImage(file=r"C:\Users\krame\OneDrive\桌面\練習程式py\tkinter\scissors.png") 
scissors=Button(image=png_scissors)
scissors.bind("<Button-1>",s_touch)
scissors.place(y=100,x=500)
png_stone=PhotoImage(file=r"C:\Users\krame\OneDrive\桌面\練習程式py\tkinter\stone.png") 
stone=Button(image=png_stone)
stone.bind("<Button-1>", r_touch)
stone.place(y=400,x=250)
show=Label(window,textvariable=text1,font=('arial', 20),bg="skyblue").place(y=3,x=330)
the_round=Label(window,textvariable=all_round,font=('arial', 20),bg="skyblue",fg = 'red').place(y=40,x=330)
window.mainloop()