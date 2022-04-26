#2022-04 13 陳科融
#1A2B
from tkinter import *
from random import randint
window=Tk()
window.title("1A2B")
window.configure(bg='skyblue')
window.geometry("600x200+300+200")
input=StringVar()
result=StringVar()
result.set('')
rand_number=[]
set_number=[]
for i in range(1,10):
    set_number.append(i)
for i in range(0, 4):
    rand_number.append(set_number.pop(randint(0, int(len(set_number)-1))))
print(rand_number)
def button_event():
    done=[0,0,0,0]
    A=0
    B=0
    if input.get() != '':
        for y in range(4):
            for x in range(4):
                # print(rand_number[y],input.get()[x],end=' ')
                if(y==x and rand_number[y]==int(input.get()[x])):
                    done[y]=1
                    A=A+1
                elif(done[y]!=1 and rand_number[y]==int(input.get()[x])):
                    B=B+1
        print("A={},B={}".format(A,B))
        if(A!=4):
            result.set("結果為A={},B={},請繼續猜".format(A,B))
        else:
            result.set('Bingo~~~')
            mybutton.config(state="disable")
the_game=Label(window,text="歡迎來到1A2B game，請輸入四個號碼",font=('arial', 20),bg="skyblue").place(y=0,x=50)
myentry=Entry(window,textvariable=input,font=('arial', 20))
myentry.place(x=80,y=40,width=300,height=40)
mybutton = Button(window, text='button', command=button_event)
mybutton.place(x=400,y=45,width=70,height=40)
ans=Label(window,textvariable=result,font=('arial', 20),bg="skyblue",fg='red').place(x=100,y=90,height=30)
window.mainloop()