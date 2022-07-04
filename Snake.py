#2022-06-08 陳科融
#snake
from tkinter import *
import tkinter.messagebox
from threading import Timer
from tkinter import ttk
from random import randint
import random
game_X_size=15      #場地寬度
game_Y_size=15      #場地高度
window=Tk()
window.title("snake")
window.configure(bg='skyblue')
window.geometry("720x660+300+90")

# print(game_Label)
score=0                 #分數
scoreVar=StringVar()    #分數var
scoreVar.set('Score : '+str(score)) #放置分數
def game_new_set():
    global  snake_size,snake_speed,active_x,active_y,btn,score,game_start,game_over,t,save_food_x,save_food_y,ok,body_eat,counter,reset,game_Label
    game_Label = []
    for y in range(game_Y_size):
        for x in range(game_X_size):
            game_Label.append([x, y])
    snake_size=2       #蛇蛇剛開始的長度
    snake_speed=0.2    #蛇蛇剛開始的速度
    active_x=0         #行動x軸
    active_y=0         #行動y軸
    btn=[]             #場地Label
    game_start=-1      #偵測遊戲開始沒
    game_over=-1       #偵測遊戲結束沒
    t = None           #時間
    save_food_x = -1
    save_food_y = -1
    ok = -1
    body_eat = -1
    counter = 1
    reset = -1
game_new_set()
'''=====================<計時器>======================'''

def change_time():
    global counter,btn,t,snake,snake_size,game_over,score,snake_speed,save_food_y,save_food_x,ok,game_over_Label,body_eat,counter,reset
    if(reset==1):
        return
    if(game_start==-1 or game_over==1):                     #是否結束
        return
    save_tail_x=snake[len(snake)-1][0]                      #儲存最後的x
    save_tail_y=snake[len(snake)-1][1]                      #儲存最後的y
    # print(snake)
    if(save_tail_y==save_food_y and save_tail_x==save_food_x):      #尾巴是吃到食物
        ok=1
        # print('{},{}'.format(save_tail_x, save_tail_y))
        # print('ok')
    # print('{},{}'.format(save_tail_x,save_tail_y))          #印出尾巴
    # else:
    if (Food_chose[1] == snake[0][1] and Food_chose[0] == snake[0][0]):
        # print('eat')
        save_food_y = Food_chose[1]
        save_food_x = Food_chose[0]
        score += 1
        snake_speed -= 0.01
        scoreVar.set('Score : ' + str(score))
        food_random()
    btn[snake[len(snake) - 1][1]][snake[len(snake) - 1][0]].config(bg='#f1d5ff')  # 消除之前的位置
    if(active_x!=0):
        insert_x=snake[0][0] + active_x
        if ([insert_x, snake[0][1]] in snake and counter>2):
            body_eat=1
            # print('eat body')
        snake.insert(0, [insert_x, snake[0][1]])    #方法二用插入的
        snake.pop()  # 移除最後一項
    elif(active_y!=0):
        insert_y=snake[0][1]+active_y
        if ([snake[0][0],insert_y]in snake and counter>2):
            body_eat = 1
            # print('eat body')
        snake.insert(0, [snake[0][0],insert_y])
        snake.pop()                                     #移除最後一項

    # print(snake)
    # for i in range(len(snake) - 1, 0, -1):  # 建置過慢方法一
    #     snake[i][0] = snake[i - 1][0]
    #     snake[i][1] = snake[i - 1][1]
    if(ok==1):
        snake.append([save_food_x,save_food_y])
        save_food_x = -1
        save_food_y = -1
        ok=-1
    if(snake[0][0]>=15 or snake[0][0]<0 or snake[0][1]>=15 or snake[0][1]<0 or body_eat==1):
        print('gameover')
        game_over_Label=Label(window,text='GAMEOVER',font=('arial', 20),fg='red')
        game_over_Label.place(x=300, y=30)
        game_over=1
        pause()
        return
    btn[snake[0][1]][snake[0][0]].config(bg='black')
    counter=counter+1
    t = Timer(snake_speed, change_time)
    t.start()
'''======================<暫停>======================'''
def pause():
    global t
    t.cancel()
'''=========================<裝飾器>============================'''
def handlerAdaptor(fun, **kwds):
	'''事件處裡函數的配飾器，相當於一個中介'''
	return lambda event,fun=fun,kwds=kwds: fun(event, **kwds)
'''=========================<吃到動作>=========================='''
def button_click(event,x,y):
    global active_x,active_y,game_start
    if(game_start==-1):
        t = Timer(snake_speed, change_time)
        t.start()
    game_start=1
    if(x!=0 and active_x==0):       #防止回頭反吃
        active_x=x
        active_y=0
    elif(y!=0 and active_y==0):     #防止回頭反吃
        active_y=y
        active_x=0
'''============================<建置場地>======================='''
def set_space():
    global text_color, test_Frame, frame1
    '''=========================<配置外框>============================'''
    frame1 = Frame(bg="#302f33", bd=1, relief=SUNKEN, width=200, height=100)
    for y in range(game_Y_size):
        btn.append([])
        for x in range(game_X_size):
            btn[y].append(Label(frame1, width=5, height=2, relief=RAISED, anchor='center'))
            btn[y][x].config(bg='#f1d5ff')
            btn[y][x].grid(row=y, column=x)
            window.bind("<KeyPress-Up>",   handlerAdaptor(button_click, x=0, y=-1))     #方向鍵上
            window.bind("<KeyPress-Down>", handlerAdaptor(button_click, x=0, y=1))    #方向鍵下
            window.bind("<KeyPress-Left>", handlerAdaptor(button_click, x=-1,y=0))    #方向鍵左
            window.bind("<KeyPress-Right>",handlerAdaptor(button_click, x=1, y=0))     #方向鍵右
            window.bind("<w>",handlerAdaptor(button_click, x=0, y=-1))     #W向上
            window.bind("<s>",handlerAdaptor(button_click, x=0, y=1))    #S向下
            window.bind("<a>",handlerAdaptor(button_click, x=-1,y=0))    #A向左
            window.bind("<d>",handlerAdaptor(button_click, x=1, y=0))     #D向右
    frame1.place(x=50, y=90)
set_space()
'''=====================<食物鍵置>======================'''
snake=[[7,7],[7,6]]
food_map=[]
Food_chose=[]
def food_random():
    global btn,food_map,Food_chose,game_Label,snake
    food_map = [i for i in game_Label if i not in snake] #去除重複
    # print(food_map)
    Food_chose = random.choice(food_map)
    # print(Food_chose)
    # if(Food_chose[1]):
    #     print('not')
    btn[Food_chose[1]][Food_chose[0]].config(bg='red')

food_random()
'''============================<建置蛇蛇>========================'''
def snake_run():
    head_x = snake[0][0]  # 獲取頭部的x軸
    head_y = snake[0][1]  # 獲取頭部的y軸
    btn[head_y][head_x].config(bg='black')
    btn[snake[1][1]][snake[1][0]].config(bg='black')
snake_run()
def set_score():
    global score_label
    score_label=Label(window,textvariable=scoreVar,font=('arial', 20),bg="skyblue",fg='red')
    score_label.place(x=50,y=30)
set_score()
def refresh(event):
    global  snake_size,snake_speed,active_y,active_x,btn,score,game_start,game_over,snake,game_over_Label,t,save_food_y,save_food_x,ok,body_eat,counter,frame1,reset,game_Label
    del snake[:]
    del game_Label[:]
    snake.append([7, 7])
    snake.append([7, 6])
    reset=1
    if(t!=None):
        pause()
    frame1.destroy()
    if(game_over==1):
        game_over_Label.destroy()
    game_new_set()
    del food_map[:]
    # print(snake)
    del Food_chose[:]

    del btn [:]
    set_space()
    score = 0  # 分數
    scoreVar.set('Score : ' + str(score))  # 放置分數
    snake_run()
    set_score()
    food_random()
    reset=-1
    print('refresh')
restart_game=Button(window,text='restart',font=('arial', 20),bg="#ff5c0f",fg='black')
restart_game.bind("<Button-1>",refresh)#左鍵
restart_game.place(x=560,y=30)
window.mainloop()