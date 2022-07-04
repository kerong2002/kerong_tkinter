#2022-03-30 陳科融
#打地鼠
from tkinter import *
from random import randint
window=Tk()
window.title("geomyidae")
window.configure(bg='skyblue')
window.geometry("600x700+700+100")
from threading import Timer
how_many_time=4     #一回合多快
text1=StringVar()   #地鼠數量
stage_game_run=1    #回合數
state_what=StringVar()
state_what.set('stage'+str(stage_game_run))#回合數設定
counter=1           #時間計數
btn=[]
t = None
# labelText = StringVar()
# labelText.set(str(counter))
all_get=0           #得分
score=StringVar()
score.set(str(all_get))#得分設定
other_num=0         #隨機的地鼠數量
#=====================<隨機的地鼠數量>=======================
def setset():
    global other_num
    other_num=randint(6,15)
    text1.set('地鼠數量'+str(other_num-1))
#====================================================
#========================<開始玩>=======================
def play(x,y):
    global other_num,game_ans,counter,all_get,stage_game_run
    if(x==-1 and y==-1):
        if(counter%how_many_time==0):
            clear_set()
            setset()
            set_number()
            stage_game_run+=1
            state_what.set('stage'+str(stage_game_run))
        if(counter==how_many_time*5):
            pause()
    else:
        for i in range(len(game_ans)):
            if(y*10+x==game_ans[i]):
                btn[y][x].config(text=' ',state='disable')
                other_num-=1
                text1.set('地鼠數量'+str(other_num-1))
                all_get+=1
                score.set(str(all_get))
#====================================================
#========================<停止>=======================
def pause():
    global window
    global t
    t.cancel()
#====================================================
#========================<清除>=======================
def clear_set():
    for i in range(len(gg)):
        gg.pop()
    for i in range(len(game_num)):
        game_num.pop()
    for i in range(len(game_ans)):
        game_ans.pop()
    for i in range(len(game_set)):
        game_set.pop()
#====================================================
def change_time():
    global labelText
    global counter
    global t
    t = Timer(1, change_time)
    if(counter!=how_many_time*5):
        play(-1,-1)
        t.start()
    elif(counter>=how_many_time*5):
        state_what.set('end')
        for y in range(10):
            for x in range(10):
                btn[y][x].config(state='disable')
    counter = counter + 1
#=====================<產生亂數>=========================
gg=[]
game_num=[]
game_ans=[]
game_set=[]
def set_number():
    for y in range(10):
        game_set.append([])
        for x in range(10):
            game_set.append(0)
            game_num.append(y*10+x)
    for i in range(other_num):
        game_ans.append(game_num.pop(randint(0,int(len(game_num)-1))))
    for y in range(10):
        gg.append([])
        for x in range(10):
            gg[y].append(' ')
    for y in range(10):
        for x in range(10):
            for s in range(other_num-1):
                if(game_ans[s]==y*10+x):
                    gg[y][x]='🐭'
    set_button()
#====================================================
#=====================<設定按鈕>=========================
def set_button():
    for y in range(10):
        btn.append([])
        for x in range(10):
            btn[y].append(Button(window,width = 5,height = 3))
            btn[y][x].config(text=gg[y][x],bg='pink',command = lambda x = x,y = y:play(x,y))
            if(gg[y][x]!='X'):
                btn[y][x].config(state='disable')
            if(gg[y][x]!=' '):
                btn[y][x].config(state='normal')
            btn[y][x].grid(row = y,column = x)
#====================================================
stage_game=Label(window,textvariable=state_what,font=('arial', 20),bg="skyblue").place(y=600,x=20)
the_game=Label(window,textvariable=text1,font=('arial', 20),bg="skyblue").place(y=600,x=120)
win_score=Label(window,textvariable=score,font=('arial', 20),bg="skyblue").place(y=650,x=20)
t = Timer(1, change_time)
t.start()
setset()
set_number()
window.mainloop()