import time
from tkinter import *
import tkinter.ttk

window= Tk()
window.geometry("400x200+400+300")
def show():
    for i in range(100):
        # 每次更新加1
        progressbarOne['value'] = i + 1
        # 更新画面
        window.update()
        time.sleep(0.09)

progressbarOne = tkinter.ttk.Progressbar(window)
progressbarOne.pack(pady=20)
# 进度值最大值
progressbarOne['maximum'] = 100
# 进度值初始值
progressbarOne['value'] = 0

button = tkinter.Button(window, text='Running', command=show)
button.pack(pady=5)

window.mainloop()
