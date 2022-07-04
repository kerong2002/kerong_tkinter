#2022-05-11 陳科融
#colorgame
from tkinter import *
import random
from random import randint
window=Tk()
window.title("english")
window.configure(bg='skyblue')
window.geometry("800x600+500+100")
game_X_size=3
game_Y_size=3
color_btn=[]
color_number='e242ff'
def random_color():
    for y in range(game_Y_size):
        color_btn.append([])
        for x in range(game_X_size):
            color_btn[y].append('#'+color_number)
random_color()
# print(color_btn)
btn=[]
def button_set():
    frame1 = Frame(bg="#302f33", bd=1, relief=SUNKEN, width=200, height=100)
    for y in range(game_Y_size):
        btn.append([])
        for x in range(game_X_size):
            btn[y].append(Button(frame1, width=5, height=3, relief=RAISED))
            btn[y][x].config(text=' ', font='30', bg=color_btn[y][x])
            btn[y][x].grid(row=y, column=x)
    frame1.place(x=30,y=80)
button_set()
window.mainloop()