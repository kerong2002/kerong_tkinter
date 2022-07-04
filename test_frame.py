from tkinter import *
import time

win = Tk()

cou = 0
##可將區塊做註解跟解註解做做看比較
##----------Frame----------
test_Frame = None
def reset():
    start_time = time.time()
    global test_Frame, cou
    if (test_Frame != None):
        test_Frame.destroy()
    test_Frame = Frame()
    for i in range(16):
        for j in range(30):
            Button(test_Frame, text=str(cou), width=2, height=1).grid(row=i, column=j)
    test_Frame.grid(row=1, column=0)
    cou += 1
    end_time = time.time()
    print(end_time - start_time)
Button(text="reset", command=reset).grid(row=0, column=0)
reset()

##-------------------------

##----------Not Use Frame----------
##def reset():
##    start_time = time.time()
##    global cou
##    test_Frame = Frame()
##    for i in range(16):
##        for j in range(30):
##            Button(text=str(cou), width=2, height=1).grid(row=i+1, column=j)
##    test_Frame.grid(row=1, column=0)
##    cou += 1
##    end_time = time.time()
##
##    print(end_time-start_time)
##
##Button(text="reset", command=reset).grid(row=0, column=0, columnspan=30)
##reset()
##---------------------------------

