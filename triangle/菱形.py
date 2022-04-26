#2022-03-30 陳科融
#正三角形
from tkinter import *
from random import randint
window=Tk()
window.title("Tic-tac-toe")
window.configure(bg='skyblue')
window.geometry("800x700+400+100")
n=int(input())
savei=n*20
for i in range(n + 1):
    Label(window, text='  '*(n-i)+'*  '*i,font='20',bg='skyblue').place(y=i*20, x=0)
for i in range(n,0,-1):
    Label(window, text='  '*(i)+'*  '*(n-i), font='20', bg='skyblue').place(y=savei+i * 20, x=0)
    # print(' ' * (n - i) + '*' * (2 * i - 1))
#             Label(window, text='*', font='20', bg='skyblue').place(y=y*20, x=x*20)
#         else:
#             Label(window, text=' ', font='20', bg='skyblue').place(y=y * 20, x=x * 20)
#         print('({},{})'.format(x,y),end='')
#     print()
window.mainloop()