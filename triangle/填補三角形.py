#2022-03-30 陳科融
#填補三角形
from tkinter import *
from random import randint
window=Tk()
window.title("Tic-tac-toe")
window.configure(bg='skyblue')
window.geometry("800x700+400+100")
N=int(input())
# frame1 = Frame(bg="#302f33", bd=5, relief=SUNKEN, width=200, height=100)
if(N>0):
    for y in range(1,N):
        for x in range(1,2*N):
            if((abs(N-x)+abs(N-y))==N-1):
                Label(window,text="*",bg='skyblue').place(y=30*y,x=30*x)
            elif((abs(N-x)+abs(N-y))<=N-1):
                Label(window,text="#",bg='skyblue').place(y=30*y,x=30*x)
            else:
                Label(window,text=" ",bg='skyblue').place(y=30*y,x=30*x)
            if(y==N-1):
                Label(window, text="*", bg='skyblue').place(y=30*N,x=30*x)

# frame1.place(x=10,y=100)
window.mainloop()
# while(1):
#     N=int(input())
#     if(N>0):
#         for y in range(1,N):
#             for x in range(1,2*N):
#                 if((abs(N-x)+abs(N-y))==N-1):
#                     print("*",end="")
#                 elif((abs(N-x)+abs(N-y))<=N-1):
#                     print("#",end="")
#                 else:
#                     print(" ",end="")
#             print()
#         if(N>=1):
#             print("* "*N)
#     else:
#         break