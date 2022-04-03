#2022-03-02 陳科融
#pascale triangle
from tkinter import *
from math import comb
N=int(input())
window=Tk()
window.title("triangle")
window.geometry("800x800+700+200")
for i in range(0,N+1):
    for j in range(0,i+1):
        Label(window,text=comb(i,j)).grid(row = i,column =(N-i)+2*j)
        # Label(window, text=comb(i,j)).place(y=i*40, x=j*40 + ((N+1-i)*20))
window.mainloop()