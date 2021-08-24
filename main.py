from tkinter import *
from tkinter import ttk , messagebox , filedialog
from tkinter.font import Font
from font import *
import os
root = Tk()
#Defining the fonts
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
#creating the background
bg = PhotoImage(file = "./assets/pictures/background.png")
  
# Show image using label
label1 = Label( root, image = bg)
label1.place(x=-1 , y=0)
# ----------------------------------------------------->
# Screen-1 ( Agreement )
root.geometry('750x500')
Agreement_Heading = ttk.Label(root,  text='Please read and accept the licence agreement below to continue.', font=Fonts.Vendara_mini , background='')
# Loading the agreement/license into memory
global Agreement_content
with open('./LICENSE' , 'r') as license:
    Agreement_content=str(license.read())
# Creating the textbox to put the license text in.
Agreement = Text(root)
# Inserting the license content in the text-box
Agreement.insert(INSERT , Agreement_content)
# Disableing the text box to make it read only
Agreement.config(state=DISABLED)


if __name__ == '__main__':
    Agreement_Heading.pack()
    Agreement.pack(pady=20)

    root.mainloop()