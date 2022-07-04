#2022-03-16 陳科融
#圈圈叉叉pro
from tkinter import *
window=Tk()
window.title("Tic-tac-toe")
window.configure(bg='skyblue')
window.geometry("1000x1000+100+100")
text1=StringVar()
text1.set('')
done=0
btn=[]
run=0
state=[]
X_start=3
Y_start=3
def play(x,y):
    global run,done,X_start,Y_start
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
    row_win_O=[]
    row_win_X=[]
    for x in range(X_start):
        row_win_O.append(1)
    for x in range(X_start):
        row_win_X.append(-1)
    for y in range(Y_start):
        if(state[y]==row_win_O):
            text1.set('O win')
            exit()
        elif(state[y]==row_win_X):
            text1.set('X win')
            exit()
# ================<<直的>>==========================
        cnt_X=0
        cnt_O=0
        for x in range(Y_start):
            if(state[x][y]==1):
                cnt_O+=1
            if(state[x][y]==-1):
                cnt_X+=1
            if(cnt_O==Y_start):
                text1.set('O win')
                exit()
            elif(cnt_X==Y_start):
                text1.set('X win')
                exit()
#================<<斜的>>==========================
    oblique_X=0
    oblique_O=0
    for y in range(Y_start):
        if(state[y][y]==1):
            oblique_O+=1
        if(state[y][y]==-1):
            oblique_X+=1
        if(oblique_O==Y_start):
            text1.set('O win')
            exit()
        elif(oblique_X==Y_start):
            text1.set('X win')
            exit()
#================<<斜的>>==========================
    shout_X=0
    shout_O=0
    for y in range(Y_start):
        for x in range(X_start):
            if((y+x)==Y_start-1 and state[y][x]==1):
                shout_O+=1
            if((y+x)==Y_start-1 and state[y][x]==-1):
                shout_X+=1
            if(shout_O==Y_start):
                text1.set('O win')
                exit()
            elif(shout_X==Y_start):
                text1.set('X win')
                exit()
    if(done==Y_start*X_start):
        text1.set('平手')
        exit()

#================<終止>====================
def exit():
    global Y_start,X_start
    for y in range(Y_start):
        for x in range(X_start):
            btn[y][x].config(state="disabled")
#================<變化>====================
def set_size(event):
    global X_start,Y_start,btn,state,done,frame1
    frame1.destroy()
    X_start=X_start+1
    Y_start=Y_start+1
    del state[:]
    del btn[:]
    set_button()
#==================<清除>=======================
def clear_button(event):
    global X_start,Y_start,btn,state,done,frame1,btn
    frame1.destroy()
    del state[:]
    del btn[:]
    text1.set("")
    done = 0
    set_button()
def min_size(event):
    global X_start,Y_start,btn,state,done,frame1
    frame1.destroy()
    X_start=X_start-1
    Y_start=Y_start-1
    del state[:]
    del btn[:]
    set_button()
def set_button():
    global frame1,X_start,Y_start,state
    text1.set("")
    frame1 = Frame(bg="#302f33", bd=5, relief=SUNKEN, width=200, height=100)
    for y in range(X_start):
        btn.append([])
        state.append([])
        for x in range(Y_start):
            state[y].append(0)
            btn[y].append(Button(frame1,width = 10,height = 5))
            btn[y][x].config(command = lambda x = x,y = y:play(x,y))
            btn[y][x].grid(row = y,column = x)
    frame1.place(y=120,x=20)
def set_min():
    global Y_start,text1
    before = Button(window, text="min", width=10, height=4)
    before.bind("<Button-1>", min_size)  # 左鍵
    before.place(y=50, x=20)
def set_next():
    global Y_start,text1
    next=Button(window,text="max",width=10,height=4)
    next.bind("<Button-1>",set_size)#左鍵
    next.place(y=50,x=190)
def restart():
    global Y_start,text1
    rest=Button(window,text="restart",width=10,height=4)
    rest.bind("<Button-1>",clear_button)#左鍵
    rest.place(y=50,x=105)
    text1.set("")
the_game = Label(window, textvariable=text1, font=('arial', 20), bg="skyblue").place(y=16,x=100)
set_next()
set_min()
restart()
set_button()
window.mainloop()