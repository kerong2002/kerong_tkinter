from tkinter import *
tk = Tk()
Label(tk, text="HELLO").pack(side=TOP)
fr=Frame(tk)
fr.pack(side=TOP, fill=BOTH, expand=True)
print("frame size before update: ", fr.winfo_width(), fr.winfo_height())
fr.update()
print("frame size after update: ", fr.winfo_width(), fr.winfo_height())
tk.mainloop()