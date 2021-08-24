from logging import warn
from tkinter import *
from tkinter import ttk , messagebox , filedialog
from tkinter.font import Font
from font import *
from sounds import *
import function.warn
import os
root = Tk()
#Defining
statement = 'Please read and accept the license agreement below to continue.'
script_path = str(str(os.getcwd()).__add__('/function/scripts')).replace('\\' , '/')
def warning():
    function.warn.warning_send(script_path)
    exit()

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
root.geometry('750x550')
root.title('You know what you have to do.')
# Loading the agreement/license into memory
global Agreement_content
with open('./LICENSE' , 'r') as license:
    Agreement_content=f'{statement.upper()}\n\n{str(license.read())}'
# Creating the textbox to put the license text in.
Agreement = Text(root , pady=10 , padx=10,borderwidth=5)
# Inserting the license content in the text-box
Agreement.insert(INSERT , Agreement_content)
# Disableing the text box to make it read only
Agreement.config(state=DISABLED)

# making buttons
I_disagree = ttk.Button(root , text='I disagree' , command=warning ,width=15)
I_agree = ttk.Button(root , text='I accept' , command=lambda:print('Yay') , width=15)


if __name__ == '__main__':
    Agreement.pack(pady=20)
    I_agree.pack(ipady=2 , ipadx=20, anchor='center', pady=10 , padx=10)
    I_disagree.pack(ipady=2 , ipadx=20, anchor='center',pady=10 , padx=10)
    root.mainloop()