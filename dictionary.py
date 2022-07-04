# text_color={'1':'green','2':'blue'}
# print(text_color['1'])
from tkinter import *

top =Tk()

B1 = Button(top, text ="FLAT", relief=FLAT )
B2 = Button(top, text ="RAISED", relief=RAISED )
B3 = Button(top, text ="SUNKEN", relief=SUNKEN )
B4 =Button(top, text ="GROOVE", relief=GROOVE )
B5 = Button(top, text ="RIDGE", relief=RIDGE )

B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
top.mainloop()