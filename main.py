from tkinter import *
from tkinter import ttk , messagebox , filedialog
from tkinter.font import Font
import sounds
from font import *
root = Tk()
class Fonts():
    def __init__(self) -> None:
        Ubuntu_mono = Font(
            family='Ubuntu Mono',
            weight='normal',
            slant='roman',
            underline=0,
            overstrike=0,
            size=24
            )

        Bahnschrift = Font(
            family='Bahnschrift',
            weight='normal',
            slant='roman',
            underline=0,
            overstrike=0,
            size=24
            )
root.geometry('750x500')
my_label = ttk.Label(root,  text='Welcome', font=Bahnschrift)
my_label.pack()
root.mainloop()