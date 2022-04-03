#2022-03-16 陳科融
#圈圈叉叉
from tkinter import *
window=Tk()
window.title("Tic-tac-toe")
window.configure(bg='skyblue')
window.geometry("340x500+900+200")
text1=StringVar()
text1.set('')
done=0
btn=[]
run=0
state=[[0,0,0],[0,0,0],[0,0,0]]
def play(x,y):
    global run,done
    if(run==0):
        btn[y][x].config(text="O")
        btn[y][x].config(state="disabled")
        state[y][x]+=1
        run=1
        done+=1
    elif(run==1):
        btn[y][x].config(text="X")
        btn[y][x].config(state="disabled")
        state[y][x]-=1
        run=0
        done+=1
#================<<橫的>>==========================
    for y in range(3):
        if(state[y]==[1,1,1]):
            text1.set('O win')
            exit()
        elif(state[y]==[-1,-1,-1]):
            text1.set('X win')
            exit()
#================<<直的>>==========================
        cnt_X=0
        cnt_O=0
        for x in range(3):
            if(state[x][y]==1):
                cnt_O+=1
            if(state[x][y]==-1):
                cnt_X+=1
            if(cnt_O==3):
                text1.set('O win')
                exit()
            elif(cnt_X==3):
                text1.set('X win')
                exit()
#================<<斜的>>==========================
    oblique_X=0
    oblique_O=0 
    for y in range(3):
        if(state[y][y]==1):
            oblique_O+=1
        if(state[y][y]==-1):
            oblique_X+=1
        if(oblique_O==3):
            text1.set('O win')
            exit()
        elif(oblique_X==3):
            text1.set('X win')
            exit()
#================<<斜的>>==========================
    if(state[2][0]==state[1][1]==state[0][2]==1):
        text1.set('O win')
        exit()
    elif(state[2][0]==state[1][1]==state[0][2]==-1):
        text1.set('X win')
        exit()
    if(done==9):
        text1.set('平手')
def exit():
    for y in range(3):
        for x in range(3):
            btn[y][x].config(state="disabled")
the_game=Label(window,textvariable=text1,font=('arial', 20),bg="skyblue").grid(row=7,column=1)
for y in range(3):
    btn.append([])
    for x in range(3):
        btn[y].append(Button(window,width = 10,height = 5))
        btn[y][x].config(command = lambda x = x,y = y:play(x,y))
        btn[y][x].grid(row = y,column = x)
window.mainloop()