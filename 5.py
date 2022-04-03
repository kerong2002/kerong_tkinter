#2022-03-30 陳科融
#配對game
from tkinter import *
from random import randint
window=Tk()
window.title("Tic-tac-toe")
window.configure(bg='skyblue')
window.geometry("600x700+700+100")
text1=StringVar()
other_num=int(50)
text1.set('剩餘配對次數'+str(other_num))
done=0
btn=[]
run=0
state=[]
savelast=[]
def play(x,y):
    global run,done,X_start,Y_start,savelast,other_num,savex,savey
    if(run==0):
        btn[y][x].config(state="disabled")
        savey=y
        savex=x
        savelast=game_ans[y*10+x-1]
        run=run+1
    elif(run==1):
        if(game_ans[y*10+x-1]==savelast):
            other_num=other_num-1
            btn[y][x].config(state="disabled")
            text1.set('剩餘配對次數'+str(other_num))
            print("done")
        else:
            btn[savey][savex].config(state="normal")
            print('not')
        run=0
game_num=[]
game_ans=[]
def set_number():
    for i in range(10):
        for j in range(10):
            game_num.append(j)
    # print(game_num)
    for i in range(0,len(game_num)):
        game_ans.append(game_num.pop(randint(0,int(len(game_num)/10))))
    
    # print(game_ans)
def set_button():
    for y in range(10):
        btn.append([])
        state.append([])
        for x in range(10):
            state[y].append(0)
            btn[y].append(Button(window,width = 4,height = 3))
            btn[y][x].config(text=game_ans[y*10+x-1],command = lambda x = x,y = y:play(x,y))
            btn[y][x].grid(row = y,column = x)
the_game=Label(window,textvariable=text1,font=('arial', 20),bg="skyblue").place(y=600,x=100)
set_number()
set_button()
window.mainloop()