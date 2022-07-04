import tkinter

def show(*args):
    stringLabel.set(stringEntry.get())
    print("数据：", stringEntry.get())

root = tkinter.Tk()
stringEntry = tkinter.StringVar()
entry = tkinter.Entry(root, textvariable=stringEntry)
entry.pack(padx=5, pady=10)
stringEntry.trace("w", show)

stringLabel = tkinter.StringVar()
label = tkinter.Label(root, textvariable=stringLabel)
stringLabel.set("同步显示")
label.pack(padx=5, pady=10)


root.mainloop()
