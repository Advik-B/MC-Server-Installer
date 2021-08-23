from tkinter import *
from tkinter import ttk , messagebox , filedialog
from tkinter.font import Font
from font import *
import sounds
import os
root = Tk()
class Fonts():
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
    
    Vendara = Font(
            family='Vendara',
            weight='normal',
            slant='roman',
            underline=0,
            size=24
            )

    Vendara_mini = Font(
            family='Vendara',
            weight='normal',
            slant='roman',
            underline=0,
            size=15
            )

    Ubuntu_mono_mini = Font(
        family='Ubuntu Mono',
        weight='normal',
        slant='roman',
        underline=0,
        overstrike=0,
        size=12
        )

root.geometry('750x500')
Agreement_Heading = ttk.Label(root,  text='Please read and accept the licence agreement below to continue.', font=Fonts.Vendara_mini)
Agreement = ttk.Entry(root)


if __name__ == '__main__':
    Agreement_Heading.pack()
    Agreement.pack(pady=20)

    root.mainloop()