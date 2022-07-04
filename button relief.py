
from  tkinter  import   *
root  =  Tk()
root.geometry("360x380+600+200")
def pick():
    bn1.config(relief=SUNKEN)
 # flat, groove, raised, ridge, solid, or sunken
bn1=Button(root,text  =   ' hello button ' ,relief = GROOVE,command=pick)
bn1.pack()
root.mainloop()
