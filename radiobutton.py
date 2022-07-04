from random import randint
window=tk()
window.title("english")
window.configure(bg='skyblue')
window.geometry("800x600+500+100")
v =IntVar()  #第一個變動整數變數
v.set(0)
for i in range(0,2,1):
    radio_button=Radiobutton(window,variable = v,value = i)
    radio_button.grid(row=2,column=i)
window.mainloop()