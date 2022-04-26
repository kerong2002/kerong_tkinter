#2022-03-30 陳科融
#正三角(左)
from tkinter import *
from random import randint
window=Tk()
window.title("Tic-tac-toe")
window.configure(bg='skyblue')
window.geometry("800x700+400+100")
N=int(input())
for i in range(0,N+1):
    Label(window,text='   '*((N-i))+'* '*i,font='20',bg='skyblue').place(y =i*20,x=2)
window.mainloop()