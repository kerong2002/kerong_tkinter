import tkinter

root = tkinter.Tk()
textFirst = "歡迎登入"
Logo = tkinter.Label(root,  text=textFirst, compound=tkinter.BOTTOM)
Logo.pack()

labelFrame = tkinter.LabelFrame(root, text="登入框")

accountLabel = tkinter.Label(labelFrame, text="帳號")
accountLabel.grid(row=0, column=0)

accountEntry = tkinter.Entry(labelFrame)
accountEntry.grid(row=0, column=1)

passWd = tkinter.Label(labelFrame, text="密碼")
passWd.grid(row=1, column=0)

passWdEntry = tkinter.Entry(labelFrame, show="*")
passWdEntry.grid(row=1, column=1)

labelFrame.pack(padx=10, pady=5, ipadx=5, ipady=5)

root.mainloop()

