from tkinter import *
window=Tk()
window.title('lamda_test')
window.configure(bg='skyblue')
window.geometry("340x500+900+200")
btn=[]
def play(i):
    print(i)
for i in range(5):
    btn.append(Button(window,width=5,heigh=3))
    btn[i].config(text=i,command=play)
    btn[i].place(y=0,x=i*50)
window.mainloop()