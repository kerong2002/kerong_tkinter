from tkinter import *

app = Tk()
app.geometry("400x150+200+200")
frame1 = Frame(bg="orange", bd=10, relief=SUNKEN)
frame1.pack(side = "left")
button1 = Button(frame1, text = "button1"); button1.pack(side = "top")
button2 = Button(frame1, text = "button2"); button2.pack(side = "bottom")
button3 = Button(frame1, text = "button3"); button3.pack(side = "left")
button4 = Button(frame1, text = "button4"); button4.pack(side = "right")

frame2 = Frame(bg = "blue"); frame2.pack(side = "right")
button5 = Button(frame2, text = "button5", font = "Consolas")
button5.grid(row = 0, column = 0)
button6 = Button(frame2, text = "button6"); button6.grid(row = 0, column = 1)
button7 = Button(frame2, text = "button7"); button7.grid(row = 1, column = 1)
button8 = Button(frame2, text = "button8"); button8.grid(row = 2, column = 0)
button9 = Button(frame2, text = "button9"); button9.grid(row = 2, column = 2)

frame3 = Frame(bg = "green", bd = 5); frame3.pack(side = "bottom")
label1 = Label(frame3, text = "..hi..\nHello.", bg = "cyan", font = "Consolas"); label1.pack()
app.mainloop()
