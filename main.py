from tkinter import *
from tkinter import ttk , messagebox , filedialog
from tkinter.font import Font
import sounds
root = Tk()
root.geometry('750x500')
Ubuntu_mono = Font(
    family='Ubuntu Mono',
    weight='normal',
    slant='roman',
    underline=0,
    overstrike=0)

my_label = ttk.Button(root,  text='Hello 0' , command=sounds.button , width=20)
my_label.pack()
root.mainloop()