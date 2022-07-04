#2022-05-11 陳科融
#
from tkinter import *
window=Tk()
window.title("Tic-tac-toe")
window.configure(bg='skyblue')
window.geometry("800x600+500+100")
english_label=StringVar()
english_label.set('')
def play():
    print('play')
myentry=Entry(window,textvariable=input,font=('arial', 20))
myentry.place(x=80,y=200,width=300,height=40)
mybutton = Button(window, text='button', command=play)
mybutton.place(x=400,y=45,width=70,height=40)
english=Label(window,text='english',font=('arial', 20),bg="skyblue",fg='red')
english.place(x=100,y=40,height=30)
chinese=Label(window,text='中文',font=('arial', 20),bg="skyblue",fg='red')
chinese.place(x=100,y=140,height=30)
window.mainloop()