#2022-04-19 陳科融
#踩地雷
from tkinter import *
from random import randint
import random
window=Tk()
window.title("bomb")
window.configure(bg='skyblue')
window.geometry("800x600+700+70")
bomb_number=10  #炸彈
game_Y_size=9   #高度
game_X_size=9   #寬度
btn=[]
number_list=[]
the_game=[]
appear_chess=[]
appear_flag=[]
can_play=True
time_end=False
bomb_number_cnt=bomb_number #剩餘
win_answer=[]
is_win=False
stop_now=False
can_paly=0
def clear_array():
    del chess[:]
    del the_game[:]
    del appear_chess[:]
    del appear_flag[:]
    del win_answer[:]
    del bomb[:]
    del btn[:]
def smile_do(event):
    global begin,can_play,counter,time_end,bomb_number_cnt,can_paly
    can_paly=0
    bomb_number_cnt=bomb_number
    remain_bomb.set(str(bomb_number_cnt))
    begin=0
    counter = 0
    time_end=False
    labelText.set(str(counter))
    can_play=True
    change_smile.set('🙂')
    clear_array()
    new_set_chess()
    boom_set()
    new_set_number()
    win_set()
    new_play_game()
    set_button()
    print('smile')
'''=========================<計時器>========================='''
from threading import Timer
t = None
counter = 0
def change_time():
    global stop_now
    global labelText
    global counter
    global t
    global is_win
    if(stop_now==True):
        return
    if(time_end==False and is_win==False and can_paly==1):
        counter = counter + 1
        labelText.set(str(counter))
        cnt_win=0
        for i in range(game_Y_size):
            if(appear_chess[i]==win_answer[i]):
                cnt_win+=1
        if(cnt_win==game_Y_size):
            is_win=True
            change_smile.set('😎')
            return
        t = Timer(1, change_time)
        t.start()
    elif(time_end==True):
        return
'''========================<建置棋盤>========================='''
chess=[]
def new_set_chess():
    global chess
    for y in range(game_Y_size):
        chess.append([])
        the_game.append([])
        appear_chess.append([])
        appear_flag.append([])
        win_answer.append([])
        for x in range(game_X_size):
            chess[y].append(' ')
            the_game[y].append(' ')
            appear_chess[y].append('')
            appear_flag[y].append('')
            win_answer[y].append('')
new_set_chess()
'''=========================================================='''
'''==========================<炸彈>==========================='''
bomb=[]
def boom_set():
    bomb.append(random.sample(range(0, game_Y_size*game_X_size),bomb_number))
    for i in range(bomb_number):
        y=int(int(bomb[0][i])/game_X_size)
        x=int(int(bomb[0][i])%game_X_size)
        chess[int(y)][int(x)]='💣'
boom_set()
'''=========================================================='''
'''========================<建置數字>========================='''
def new_set_number():
    for y in range(game_Y_size):
        for x in range(game_X_size):
            if(chess[y][x]=='💣'):
                continue
            elif(chess[y][x]!='💣'):
                Y_start=0
                X_start=0
                found=0
                for i in range(y-1,y+2):
                    if(i<0):
                        continue
                    if(i>=game_Y_size):
                        continue
                    for j in range(x-1,x+2):
                        if(j<0):
                            continue
                        if(j>=game_X_size):
                            continue
                        if(chess[i][j]=='💣'):
                            found+=1
                if(found!=0):
                    chess[y][x]=str(found)
new_set_number()
'''=========================================================='''
'''================<搜尋空白演算法>============================'''

def  flood_fill(y,x):
    if(x < game_X_size-1):
        if(chess[y][x+1] == ' ' and appear_chess[y][x+1]!=' '):
            btn[y][x+1].config(text=chess[y][x+1], bg='GhostWhite')
            appear_chess[y][x+1] = chess[y][x+1]
            flood_fill(y,x+1)
        elif(chess[y][x+1] != ' ' and chess[y][x+1]!='💣' ):
            btn[y][x + 1].config(text=chess[y][x + 1], bg='GhostWhite')
            appear_chess[y][x + 1] = chess[y][x + 1]
    if(x > 0):
        if(chess[y][x-1]==' ' and appear_chess[y][x-1] != ' '):
            btn[y][x-1].config(text=chess[y][x-1], bg='GhostWhite')
            appear_chess[y][x-1] = chess[y][x-1]
            flood_fill(y,x-1)
        elif (chess[y][x-1]!= ' ' and chess[y][x-1]!= '💣'):
            btn[y][x-1].config(text=chess[y][x-1], bg='GhostWhite')
            appear_chess[y][x-1] = chess[y][x-1]
    if (y < game_Y_size - 1):
        if (chess[y + 1][x] == ' ' and appear_chess[y + 1][x]!= ' '):
            btn[y + 1][x].config(text=chess[y + 1][x], bg='GhostWhite')
            appear_chess[y + 1][x] = chess[y + 1][x]
            flood_fill(y + 1, x)
        elif (chess[y + 1][x]!= ' ' and chess[y + 1][x]!= '💣'):
            btn[y + 1][x].config(text=chess[y + 1][x], bg='GhostWhite')
            appear_chess[y + 1][x]= chess[y + 1][x]
    if(y > 0):
        if(chess[y - 1][x] == ' ' and appear_chess[y - 1][x]!= ' '):
            btn[y-1][x].config(text=chess[y-1][x], bg='GhostWhite')
            appear_chess[y-1][x] = chess[y-1][x]
            flood_fill(y-1,x)
        elif (chess[y-1][x]!= ' ' and chess[y-1][x]!= '💣'):
            btn[y-1][x].config(text=chess[y-1][x], bg='GhostWhite')
            appear_chess[y-1][x]= chess[y-1][x]
'''========================================================='''
begin=0
def play(event,x,y):
    global t,begin,time_end,appear_flag,bomb_number_cnt,can_paly
    if(event):
        can_paly=1
    if(begin==0):#開始計數
        t = Timer(1, change_time)
        t.start()
        begin=1
    global can_play,time_end
    if(can_play==True and appear_flag[y][x]!='🚩'):
        if(chess[y][x]!='💣'):
            btn[y][x].config(text=chess[y][x],bg='GhostWhite')
            appear_chess[y][x]=chess[y][x]
            # 特別處理
            if(chess[y][x]==' '):
                flood_fill(y,x)
        elif(chess[y][x]=='💣'):
            time_end=True
            can_play=False
            for ay in range(game_Y_size):
                for ax in range(game_X_size):
                    if(the_game[ay][ax]=='🚩' and chess[ay][ax]!='💣'):
                        btn[ay][ax].config(text='❌')
                    elif(chess[ay][ax]=='💣'):
                        if(the_game[ay][ax]!='🚩'):
                            btn[ay][ax].config(text=chess[ay][ax],bg='GhostWhite')
            change_smile.set('😱')
    # print(appear_chess)
def handlerAdaptor(fun, **kwds):
	'''事件處裡函數的配飾器，相當於一個中介'''
	return lambda event,fun=fun,kwds=kwds: fun(event, **kwds)
flag_cnt=0
def flag(event,x,y):
    global appear_flag,bomb_number_cnt
    if (can_play == True and appear_chess[y][x]==''):
        if(appear_flag[y][x]==''):
            btn[y][x].config(text='🚩')
            appear_flag[y][x]='🚩'
            the_game[y][x]='🚩'
            bomb_number_cnt-=1
            remain_bomb.set(str(bomb_number_cnt))
        elif(appear_flag[y][x]=='🚩'):
            btn[y][x].config(text=' ')
            appear_flag[y][x]=''
            the_game[y][x]=' '
            bomb_number_cnt += 1
            remain_bomb.set(str(bomb_number_cnt))
def win_set():
    for y in range(game_Y_size):
        print(chess[y])
    for y in range(game_Y_size):
        for x in range(game_X_size):
            if(chess[y][x]!='💣'):
                win_answer[y][x]=chess[y][x]
win_set()
change_smile=StringVar()
change_smile.set('🙂')
remain_bomb=StringVar()
remain_bomb.set(str(bomb_number_cnt))
labelText = StringVar()
labelText.set(str(counter))
def new_play_game():
    Label(window, textvariable=remain_bomb,font='80',height='3',bg='skyblue').grid(row = 0,column =0)
    Label(window, textvariable=labelText,font='80',height='3',bg='skyblue').grid(row = 0,column = game_X_size-1)
    smile=Button(window,textvariable=change_smile,font='100',bg='GhostWhite')
    smile.bind("<Button-1>",smile_do)#左鍵
    smile.grid(row = 0,column = int(game_X_size/2))
new_play_game()
def set_button():
    for y in range(game_Y_size):
        btn.append([])
        for x in range(game_X_size):
            btn[y].append(Button(window,width = 5,height = 3))
            btn[y][x].bind("<Button-3>",handlerAdaptor(flag,x=x,y=y))
            btn[y][x].bind("<Button-1>",handlerAdaptor(play,x=x,y=y))
            btn[y][x].config(text=' ', bg='LightPink', fg='black')
            btn[y][x].grid(row = y+5,column = x)
set_button()
window.mainloop()