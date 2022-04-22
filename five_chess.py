#2022-04-22 陳科融
#五子棋
from tkinter import *
window=Tk()
window.title("five_chess")
window.configure(bg='skyblue')
window.geometry("800x720+400+60")
game_X_size=15  #場地寬度
game_Y_size=15  #場地高度
btn=[] #按鈕
game_chess=[]   #紀錄出現的棋子
white_or_black = 0
win_text=StringVar()
win_text.set('')
'''=====<初始化場地>======'''
def set_game_chess():
    for y in range(game_Y_size):
        game_chess.append([])
        for x in range(game_Y_size):
            game_chess[y].append(' ')
set_game_chess()
'''=======<遊玩>========='''
def play(x,y):
    global white_or_black,game_chess
    if(white_or_black==0 and game_chess[y][x]==' '):
        btn[y][x].config(text='⚪')
        game_chess[y][x]='⚪'
        white_or_black=1
    elif(white_or_black==1 and game_chess[y][x]==' '):
        btn[y][x].config(text='⚫')
        game_chess[y][x] = '⚫'
        white_or_black = 0
    # ================<<橫的>>==========================
    row_win_O = []
    row_win_X = []
    for x in range(game_X_size):
        row_win_O.append('⚪')
    for x in range(game_X_size):
        row_win_X.append('⚫')
    for y in range(2,game_Y_size-2):
        for x in range(2,game_X_size-2):
            for ay in range(y-2,y+3):
                horizontal_O=0  #橫的白棋
                horizontal_X=0  #橫的黑棋
                for ax in range(x-2,x+3):
                    if(game_chess[ay][ax]=='⚪'):
                        horizontal_O+=1
                    if(game_chess[ay][ax] =='⚫'):
                        horizontal_X += 1
                if(horizontal_O==5):
                    win_text.set('white win')
                    exit()
                    return
                if(horizontal_X==5):
                    win_text.set('black win')
                    exit()
                    return
    # ================<<直的>>==========================
    for y in range(2,game_Y_size-2):
        for x in range(2,game_X_size-2):
            for ax in range(x - 2, x + 3):
                vertical_O=0  #橫的白棋
                vertical_X=0  #橫的黑棋
                for ay in range(y - 2, y + 3):
                    if(game_chess[ay][ax]=='⚪'):
                        vertical_O+=1
                    if(game_chess[ay][ax] =='⚫'):
                        vertical_X+= 1
                if(vertical_O==5):
                    win_text.set('white win')
                    exit()
                    return
                if(vertical_X==5):
                    win_text.set('black win')
                    exit()
                    return
    # ================<<向左斜的>>==========================
    for y in range(2,game_Y_size-2):
        for x in range(2,game_X_size-2):
            left_incline_O = 0  # 橫的白棋
            left_incline_X = 0  # 橫的黑棋
            for ay in range(y - 2, y + 3):
                for ax in range(x - 2, x + 3):
                    if(y-x==ay-ax and game_chess[ay][ax]=='⚪'):
                        left_incline_O+=1
                    elif(y-x==ay-ax and game_chess[ay][ax] =='⚫'):
                        left_incline_X+= 1
                    else:
                        continue
                if(left_incline_O==5):
                    win_text.set('white win')
                    exit()
                    return
                if(left_incline_X==5):
                    win_text.set('black win')
                    exit()
                    return
    # ================<<向右斜的>>==========================
    for y in range(2, game_Y_size - 2):
        for x in range(2, game_X_size - 2):
            pick=x+y
            right_incline_O = 0  # 橫的白棋
            right_incline_X = 0  # 橫的黑棋
            for ay in range(y - 2, y + 3):
                for ax in range(x - 2, x + 3):
                    if (pick== ay+ax and game_chess[ay][ax] == '⚪'):
                        right_incline_O += 1
                    elif (pick== ay+ax and game_chess[ay][ax] == '⚫'):
                        right_incline_X += 1
                    else:
                        continue
                if (right_incline_O== 5):
                    win_text.set('white win')
                    exit()
                    return
                if (right_incline_X== 5):
                    win_text.set('black win')
                    exit()
                    return
#================<終止>====================
def exit():
    for y in range(game_Y_size):
        for x in range(game_X_size):
            btn[y][x].config(state="disabled")
def clear_button(event):
    del game_chess[:]
    set_game_chess()
    win_text.set(' ')
    for y in range(game_Y_size):
        for x in range(game_X_size):
            btn[y][x].config(state='normal')
    set_chess_button()
def restart():
    rest = Button(window, text="restart", width=5, height=2)
    rest.bind("<Button-1>", clear_button)  # 左鍵
    rest.place(y=10,x=(42*game_X_size+50))
restart()
'''======<設定按鈕>======'''
def set_chess_button():
    for y in range(game_Y_size):
        btn.append([])
        for x in range(game_X_size):
            btn[y].append(Button(window,width = 5,height = 2,bg='Tan'))
            btn[y][x].config(text=game_chess[y][x], command=lambda x=x, y=y: play(x, y))
            btn[y][x].place(y=y*42+70, x=x*42+50)
Label(window, textvariable=win_text,font='160',height='3',bg='skyblue').place(y = 10,x =(42*game_X_size+50)/2)
'''======<初始化>======='''
set_chess_button()
window.mainloop()