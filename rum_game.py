from tkinter import *
window = Tk()
window.title("configure")
window.configure(bg='skyblue')
window.geometry("600x700+400+50")
count=0
def touch(x,y):
    global count
    count+=1
    btn[y][x].configure(text='touch')
btn=[]
for y in range(5):
    btn.append([])
    for x in range(5):
        btn[y].append(Button(window, width=10, height=5))
        btn[y][x].config(text='now',command=lambda x=x, y=y:touch(x,y))
        btn[y][x].place(x=x*100+50,y=y*100+50)
window.mainloop()