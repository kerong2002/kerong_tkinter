# 2022-05-4 陳科融
#BAR
from tkinter import *
from threading import Timer
from random import randint
window = Tk()
window.title("6")
window.configure(bg='skyblue')
window.geometry("600x700+400+50")
game_x_size=7
game_y_size=7
time_check=25
all_title_win_money=0
your_chip=10000
x_run=[]
y_run=[]
can_play=True
first_random=randint(0,25)
money_rate={
0:30,
1:5,
2:20,
3:100,
4:10,
5:15,
6:20,
7:40
}
# print(money_rate[3])
'''填充循環'''
for i in range(game_x_size-1):
    y_run.append(0)
    x_run.append(i)
for i in range(game_x_size-1):
    y_run.append(i)
    x_run.append(game_x_size-1)
for i in range(game_x_size-1,0,-1):
    y_run.append(game_x_size-1)
    x_run.append(i)
for i in range(game_x_size-1,-1,-1):
    y_run.append(i)
    x_run.append(0)
save = 0
speed=0.08
'''flash'''
flash_t = None
flash_counter=1
big_small_time=1
def flash_change_time(y, x):
    global flash_counter,flash_t,big_small_time,all_title_win_money,win_money_total
    flash_counter = flash_counter + 1
    GO_game.config(state='disable')
    if(flash_counter%2==0):
        btn[y][x].config(bg='red')
    else:
        btn[y][x].config(bg='white')
    if(flash_counter==10):
        flash_t.cancel()
        Big_game.config( state='normal')
        Small_game.config(state='normal')
        End_game.config(state='normal')
        answer=[int(temp)for temp in btn_save_image_name[y][x] if temp.isdigit()]
        bet_money_result=[]
        for i in range(8):
            bet_money_result.append(0)
        for s in range(8):
            bet_money_result[photo_btn_chose[s]]=Bet_total[s]
        all_title_win_money=money_rate[answer[0]]*bet_money_result[answer[0]]
        if(all_title_win_money==0):
            GO_game.config(state='disable')
            Big_game.config(state='disable')
            Small_game.config(state='disable')
        win_money_total.configure(text='$%7d'%all_title_win_money)
        return
    flash_t= Timer(0.25, flash_change_time, [y, x])
    flash_t.start()
'''===============<繞起來>=================='''
t = None
counter =first_random
start_done=0
def change_time():
    global speed,t,start_done,save,counter,btn,flash_counter,flash_t,can_play
    can_play=False
    GO_game.config(state='disable')
    if(start_done==0):
        save=counter
        start_done=1
    counter = counter + 1
    if(counter%1==0):
        btn[y_run[counter%time_check]][x_run[counter%time_check]].config(bg='red')
    btn[y_run[counter%time_check-1]][x_run[counter%time_check-1]].config(bg='white')
    if((counter-save)%5==0):
        speed+=0.02
    if((counter-save)%(time_check+random_time)==0):
        speed = 0.06
        start_done=0
        flash_counter = 1
        t.cancel()
        flash_t = Timer(0.25, flash_change_time,[y_run[counter % time_check], x_run[counter % time_check]])
        flash_t.start()
        # GO_game.config(state='normal')
        can_play=True
        return
    t = Timer(speed, change_time)
    t.start()
button_cnt=0
button_t=None
button_flash_speed=0.07
def button_flash(x, y):
    global button_cnt,button_t,button_flash_speed,can_play,all_title_win_money,big_small_time
    button_cnt =button_cnt + 1
    set_to_know=0
    if(button_cnt%2==0):
        Big_game.config(bg='red')
        Small_game.config(bg='white')
        button_flash_speed+=0.02
        set_to_know =1
    else:
        Big_game.config(bg='white')
        Small_game.config(bg='red')
        set_to_know =0
    if(button_cnt%big_small_time==0):
        if(x==set_to_know):
            all_title_win_money *=2
            win_money_total.configure(text='$%7d' % all_title_win_money)
            button_t.cancel()
            big_small_time += randint(17, 23)
            Big_game.config(state='normal')
            Small_game.config(state='normal')
            button_flash_speed = 0.07
            End_game.config(state='normal')
            # can_play = True
        else:
            all_title_win_money=0
            win_money_total.configure(text='$%7d' % all_title_win_money)
            button_t.cancel()
            Big_game.config(state='disable')
            Small_game.config(state='disable')
            # GO_game.config(state='normal')
            End_game.config(state='normal')
            can_play=True
        return
    button_t= Timer(button_flash_speed, button_flash, [x, 5])
    button_t.start()
def double(x):
    global big_small_time,can_play
    can_play=False
    Big_game.config(state='disable')
    Small_game.config(state='disable')
    GO_game.config(state='disable')
    End_game.config(state='disable')
    big_small_time = randint(17, 23)
    button_t = Timer(0.1, button_flash, [x, 5])
    button_t.start()
def play():
    global  t,counter,random_time,button_cnt,button_flash_speed,can_play,Bet_total
    GO_game.config(state='disable')
    Big_game.config(state='disable')
    Small_game.config(state='disable')
    Clear_game.config(state='disable')
    set=0
    for i in range(8):
        set+=Bet_total[i]
    if(set==0):
        return
    if(can_play==False):
        return
    for i in range(8):
        Bet_btn[i].config(state='disable')
    Clear_game.config(state='disable')
    button_cnt = 0
    button_flash_speed=0.07
    Big_game.config(bg='white')
    Small_game.config(bg='white')
    random_time = randint(13, 19)
    t = Timer(1, change_time)
    t.start()
'''============================<下注>============================'''
def Bet_play(x):
    global Bet_total,Clear_game
    Clear_game.config(state='normal')
    if(Bet_total[x]<9):
        Bet_total[x]+=1
        Bet_money_label[x].configure(text=Bet_total[x])
    # print(Bet_total)
def clear_all_bet():
    global Bet_total,Bet_money_label
    # print('ddd')
    del Bet_total[:]
    for x in range(8):
        Bet_total.append(0)
        Bet_money_label[x].configure(text=Bet_total[x])
        Bet_money_label[x].configure(text=Bet_total[x])
def collect():
    global all_title_win_money,win_money_total,chip,your_chip,delete_money
    delete_money = 0
    for i in range(8):
        delete_money += Bet_total[i]
    your_chip -=delete_money
    your_chip+=all_title_win_money
    chip.configure(text=your_chip)
    Big_game.config(state='disable')
    Small_game.config(state='disable')
    Clear_game.config(state='normal')
    GO_game.config(state='normal')
    for i in range(8):
        Bet_btn[i].config(state='normal')
    End_game.config(state='disable')
    all_title_win_money=0
    win_money_total.configure(text='$%7d'%all_title_win_money)
'''===========================<配置麻阿台>========================='''
png_list=[5,6,4,1,1,4,2,0,0,1,1,5,5,6,7,7,1,2,2,4,3,4,1,7]
btn=[]
btn_save_image_name=[]
photo_save=[]
frame1 = Frame(bg="#e1971c", bd=5, relief=RAISED, width=490, height=410)
win_money=Label(frame1,text="WIN",bg='#e1971c',fg='red',font=('arial',20)).place(x=210,y=110)
win_money_total=Label(frame1,text='$%7d'%all_title_win_money,bg='#e1971c',fg='red',font=('arial',20))
win_money_total.place(x=190,y=145)
png_cnt=0
for y in range(game_y_size):
    btn.append([])
    btn_save_image_name.append([])
    for x in range(game_x_size):
        # pick = randint(0, game_x_size)
        # random_pick=randint(0,len(photo_save))
        btn[y].append(Label(frame1))
        if(x==0 or x==game_x_size-1):
            image_file = './/{}.png'.format(png_list[png_cnt])
            photo_save.append(PhotoImage(file=image_file))  # 透過PhotoImage轉
            btn[y][x].config(image=photo_save[png_cnt],borderwidth = 2,relief="groove")
            btn_save_image_name[y].append(image_file)
            png_cnt+=1
            btn[y][x].place(y=47 * y + 40, x=54 * x + 50)
        elif(y==0 or y==game_y_size-1):
            image_file = './/{}.png'.format(png_list[png_cnt])
            photo_save.append(PhotoImage(file=image_file))  # 透過PhotoImage轉
            btn[y][x].config(image=photo_save[png_cnt],borderwidth = 2,relief="groove")
            btn_save_image_name[y].append(image_file)
            png_cnt += 1
            btn[y][x].place(y=47 * y + 40, x=54 * x + 50)
        else:
            btn_save_image_name[y].append('')
frame1 .place(x=50,y=50)
'''============================<下注>========================================'''
frame2 = Frame(bg="#e1971c", bd=5, relief=RAISED, width=490, height=200)
Bet_btn=[]
photo_btn_save=[]
Bet_label_number=['100','40','30','20','20','15','10','5']
photo_btn_chose=[3,7,0,6,2,5,4,1]
Bet_label=[]
Bet_money_label=[]
Bet_total=[0,0,0,0,0,0,0,0]
for i in range(8):
    Bet_btn.append(Button(frame2, relief=RAISED, anchor='center'))
    Bet_label.append(Label(frame2,width=9,height=1))
    Bet_money_label.append(Label(frame2, width=8, height=2))
    if(i<4):
        Bet_label[i].config(bg='pink')
    else:
        Bet_label[i].config(bg='skyblue')
    Bet_label[i].config(text=Bet_label_number[i])
    Bet_label[i].place(y=20,x=i*56+6)
    Bet_money_label[i].config(text=Bet_total[i])
    Bet_money_label[i].place(y=50, x=i * 58 + 3)
    image_file = './/{}.png'.format(photo_btn_chose[i])
    photo_btn_save.append(PhotoImage(file=image_file))  # 透過PhotoImage轉
    Bet_btn[i].config(image=photo_btn_save[i], borderwidth=2, relief="groove",command = lambda x = i:Bet_play(x))
    Bet_btn[i].place(y=90,x=i*58+5)
Clear_game=Button(frame2,text="Clear",width=5,height=2,bg='purple',fg='white',state='disable',command = clear_all_bet)
Clear_game.place(x=420,y=144)
frame2.place(x=50,y=460)
Big_game=Button(frame1,text="Big",width=6,height=3)
Big_game.config(command = lambda x = 1:double(x),state='disable',bg='white')
Big_game.place(x=130,y=230)
Small_game=Button(frame1,text="Small",width=6,height=3,bg='white')
Small_game.config(command = lambda x = 0:double(x),state='disable')
Small_game.place(x=290,y=230)
End_game=Button(frame1,text="collect",width=5,height=2,bg='skyblue',state='disable',command = collect)
End_game.place(x=215,y=220)
chip=Label(frame2,text=your_chip,bg="blue",fg='white',font=('arial',18))
chip.place(x=5,y=150)
GO_game=Button(frame1,text="GO",width=5,height=2,bg='#ee2020',command =play)
# GO_game.bind(左鍵
GO_game.place(x=215,y=260)
window.mainloop()