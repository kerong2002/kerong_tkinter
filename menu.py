import tkinter


def show(event):
    label.config(text=event)


root = tkinter.Tk()
root.geometry('150x120')

# 建立最上层菜单
menuBar = tkinter.Menu(root)

# file菜单
menuFile = tkinter.Menu(menuBar, tearoff=False)
menuBar.add_cascade(label='file', menu=menuFile)
menuFile.add_command(label='New', command=lambda: show('New'))

# Save菜单与Save子菜单
menuSave = tkinter.Menu(menuFile, tearoff=False)
menuFile.add_cascade(label='Save', menu=menuSave)
menuSave.add_command(label='Save As', command=lambda: show('Save As'))
menuSave.add_command(label='Save Local', command=lambda: show('Save Local'))


menuFile.add_command(label='Exit', command=lambda: show('Exit'))

# 显示菜单对象
root.config(menu=menuBar)

label = tkinter.Label(root)
label.pack(padx=5, pady=10)

root.mainloop()
