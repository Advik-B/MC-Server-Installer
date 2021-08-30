from tkinter import *
from tkinter import ttk
from threading import Thread
from font import *
from sounds import *
import function.warn
import time
import os
global exit_code
exit_code = 10
def init() -> None:
    """Starts screen 1"""
    s1 = Tk()    
    #Defining
    statement = 'Please read and accept the license agreement below to continue.'
    script_path = str(str(os.getcwd()).__add__('/function/scripts')).replace('\\' , '/')
    def warning() -> None:
        function.warn.warning_send(script_path)
     
        exit_code=1
        print('DIS AGGRED')

        exit(1)
    def close() -> None:
        exit_code=0
        print('AGGRED')
        exit(0)

    bg = PhotoImage(file = "./assets/pictures/background.png")

    # Show image using label
    label1 = Label( s1, image = bg)
    label1.place(x=-1 , y=0)
    # ----------------------------------------------------->
    # Screen-1 ( Agreement )
    s1.geometry('750x550')
    s1.title('You know what you have to do.')
    # Loading the agreement/license into memory
    global Agreement_content
    with open('./LICENSE' , 'r') as license:
        Agreement_content=f'{statement.upper()}\n\n{str(license.read())}'
    # Creating the textbox to put the license text in.
    Agreement = Text(s1 , pady=10 , padx=10,borderwidth=5)
    # Inserting the license content in the text-box
    Agreement.insert(INSERT , Agreement_content)
    # Disableing the text box to make it read only
    Agreement.config(state=DISABLED)

    # making buttons
    I_disagree = ttk.Button(s1 , text='I disagree' , command=warning ,width=15)
    I_agree = ttk.Button(s1 , text='I accept' , command=close , width=15)
    Agreement.pack(pady=20)
    I_agree.pack(ipady=2 , ipadx=20, anchor='center', pady=10 , padx=10)
    I_disagree.pack(ipady=2 , ipadx=20, anchor='center',pady=10 , padx=10)
    s1.mainloop()

def quit__():
    while True:
        if exit_code == 0:
            return 0
        elif exit_code == 1:
            return 1