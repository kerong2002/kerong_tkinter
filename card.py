#2022-03-30 陳科融
#配對game
from tkinter import *
from time import *
from random import randint
window=Tk()
window.title("Tic-tac-toe")
window.configure(bg='skyblue')
window.geometry("1400x700+100+100")
pair=26
text1=StringVar()
text1.set('剩餘配對數為'+str(pair))
btn=[]
'''============================<發牌隨機>==================================='''
card=[]
suit=['♠','♥','♦','♣']
suit_card=[]
for i in range(0,13):
    for j in range(0,4):
        suit_card.append(suit[j]+str(i+1))
for i in range(0,13):
    for j in range(0,4):
        card.append(suit_card.pop(randint(0,int(len(suit_card)-1))))
'''========================================================================='''
'''==============================<執行>====================================='''
savenum=0
savex=0
savey=0
run=0
datax=[0,0]
datay=[0,0]
errorN=0
def play(x,y):
    global run,card,savenum,savex,savey,datax,datay,errorN,pair
    if(run==0):
        if(errorN==1):
            btn[datay[0]][datax[0]].config(text='?',state='normal',bg="orange")
            btn[datay[1]][datax[1]].config(text='?',state='normal',bg="orange")
            errorN=0
        btn[y][x].config(text=card[y*13+x-1],bg="red")
        savex=x
        savey=y
        savenum=int(card[y*13+x-1][1:3])#數字，花色去掉
        run=1
        print('done1')
    elif(run==1):
        if(savex==x and savey==y):
            run=1#點到同樣的按鈕
        else:
            print('done2')
            if(savenum==int(card[y*13+x-1][1:3])):
                btn[y][x].config(text=card[y*13+x-1])
                btn[y][x].config(state='disable',bg="skyblue")
                btn[savey][savex].config(state='disable',bg="skyblue")
                pair=pair-1
                text1.set('剩餘配對數為'+str(pair))
                print('the same')
            else:
                datax[0]=savex
                datax[1]=x
                datay[0]=savey
                datay[1]=y
                btn[y][x].config(text=card[y*13+x-1],bg="red")
                errorN=1
            run=0
'''========================================================================='''
def set_button():
    for y in range(4):
        btn.append([])
        for x in range(13):
            btn[y].append(Button(window,width = 6,height = 4))
            btn[y][x].config(text='?',font=('arial', 20),bg="orange",command = lambda x = x,y = y:play(x,y))
            btn[y][x].grid(row = y,column = x)
the_game=Label(window,textvariable=text1,font=('arial', 20),bg="skyblue").place(y=600,x=100)
set_button()
window.mainloop()