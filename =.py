from tkinter import *
from tkinter import ttk
from tkinter.font import *

root = Tk()
dat = Label()
root.geometry('200x200')
def getData(
    the_button:StringVar
    ):
    print(the_button.get())
    return the_button.get()

def setData(
    data
    ):
    dat.config(text=data)
    dat.pack()


gender = StringVar(root , 'GGG')

b1 = ttk.Radiobutton(
    root,
    text='Male',
    var=gender,
    value='male'
    ).pack(anchor='center')

b1 = ttk.Radiobutton(
    root,
    text='Female',
    var=gender,
    value='female'
    ).pack(anchor='center')

GETDATA = ttk.Button(
    text='Get var',
    command=lambda:setData(getData(the_button=gender))
    )

GETDATA.pack()
root.mainloop()