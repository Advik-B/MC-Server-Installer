#!/usr/bin/env python3

# importing GUI modules
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import themed_tk

# import the other stuff
import os
import confunc
import shutil
import subprocess
import json_util
import sys
import psutil
from PIL import Image, ImageTk
from random import randint
from threading import Thread

all_processes = []
mem = psutil.virtual_memory() # Getting the current system memory
mini_mem = 2500 * 1024 * 1024 # 2.5 GB

# The current working dirctory
cwd = os.getcwd()

# gui instance
gui = themed_tk.ThemedTk()

#changing the background
gui.focus_force()
gui.config(background='#2b2d37')

# setting the screen title
gui.wm_title('Minercaft Server Installer')

# setting the icon
icons = [
    os.path.join(os.path.join(cwd, 'assets/pictures/icons'), icon)
    for icon in os.listdir(os.path.join(cwd, 'assets/pictures/icons'))
]

gui.iconbitmap(icons[randint(0, len(icons)) - 1]) # Just to make a dynamic icon 😂

# processing where the screen should appear 
screen_width = int(gui.winfo_screenwidth())
screen_height = int(gui.winfo_screenheight())
app_height = int(screen_height * .6)
app_width = int(screen_width * .5)
app_gm_1 = int(screen_width * .25)
app_gm_2 = int(screen_height * .1)

# resize the screen accoding to the above process
gui.geometry(f'{app_width}x{app_height}+{app_gm_1}+{app_gm_2}')

# Disallow resizing the gui-screen
gui.resizable(False, False)

# Setting the theme to `plastik`
gui.set_theme('plastik')

# <code>
versions = []
with open('versions.json') as raw_json:
    ver = json_util.convert_json(data=raw_json.read(), mode=1)

    versions.extend(ver['stable'])
    versions.extend(ver['snapshots'])

    binFont = ['Vendara', 18]

    del ver



    valid_img = ImageTk.PhotoImage(
        image=Image.open(
            'assets/pictures/valid.png'
            ),
        )
    invalid_img = ImageTk.PhotoImage(
        image=Image.open(
            'assets/pictures/invalid.png'
            ),
        )
    ok_img = ImageTk.PhotoImage(
        image=Image.open(
            'assets/pictures/hua.png'
        ),
    )
gorb = Button(gui, image=valid_img, border=0, activebackground='#2b2d37', background='#2b2d37')


def _check_version():
    def valid():
        messagebox.showinfo(':::: INFO ::::','The version %s is valid' % ver.get())
    def invalid():
        messagebox.showerror(':::: ERROR ::::', 'The version %s is invalid!' % ver.get())
    def hua():
        messagebox.showinfo(':::: INFO ::::', 'No version has been provided')
    while True:
        if ver.get().replace(' ','').replace('\n','') == '':
            gorb.config(image=ok_img, command=hua)
            Next_btn.config(state=DISABLED)
            continue
        if ver.get() not in versions:
            gorb.config(image=invalid_img, command=invalid)
            Next_btn.config(state=DISABLED)
            
        elif ver.get() in versions:
            gorb.config(image=valid_img, command=valid)
            Next_btn.config(state='!disabled')

def _check_path():
    def valid(var):
        messagebox.showinfo(':::: INFO ::::', 'The server will installed in:\n\t%s' % var)
    def hua(var):
        messagebox.showwarning(':::: WARNING ::::', 'The directory does not exist\nit will be created in %s' % var)
    def invalid(var):
        messagebox.showerror(':::: ERROR ::::', 'The path %s is invalid' % var)
        
    while True:
        path = path_folder.get()
        if os.path.isdir(path):
            if os.listdir(path) == []:
                valid_invalid_ver.config(image=valid_img, command=lambda:valid(path))
                Next_btn.config(state='!disabled')
            else:
                valid_invalid_ver.config(image=invalid_img, command=lambda:invalid(path))
                Next_btn.config(state='disabled')
        else:
            valid_invalid_ver.config(image=ok_img, command=lambda:hua(path))
            Next_btn.config(state='!disabled')
            continue

# Mutithreading
#: t1
t1 = Thread(target=_check_version)
t1.setName('Version validator')
all_processes.append(t1)
#: t2
t2 = Thread(target=_check_path)
t2.setName('Install-Path validator')
all_processes.append(t2)

ver = StringVar()
versions_ = ttk.Combobox(gui, values=versions, textvariable=ver, background='#2b2d37', foreground='#2b2d37')
Title = ttk.Label(gui,
                  text='Please choose your server version.',
                  font=binFont, background='#2b2d37',
                  foreground='white')#TODO: change `server` to `minecraft`

path_lbl = ttk.Label(gui,
                  text='Path of the server',
                  font=binFont,
                  foreground='white',
                  background='#2b2d37')

path_folder = ttk.Entry(gui,
                        foreground='#2b2d37',
                        font=['Ubuntu Mono', 15],
                        width=50
                        )
valid_invalid_ver = Button(gui, image=valid_img, border=0, activebackground='#2b2d37', background='#2b2d37')

Next_btn = ttk.Button(gui, text='Next')

Title.grid(row=1, column=0, padx=150)
versions_.grid(row=2, column=0, pady=15)
gorb.grid(row=2, column=0, sticky=E, columnspan=1000)
path_lbl.grid(row=3, column=0)
path_folder.grid(row=4, column=0)
valid_invalid_ver.grid(row=4, column=1)

# </code>

# making the windows appear
if __name__ == '__main__': # Making shure that the file is run directly
    if mem.total < mini_mem:
        messagebox.showwarning(':::: WARNING ::::', 'WARNING: Not enough memory to run Minecraft servers\n\t   The servers will be slow and laggy!')
    
    # Starting the threads

    for process in all_processes: print('Starting:', process.getName()); process.daemon=True; process.start()
        
    # Mainloop
    gui.mainloop()
    
    #: Post processing
    
    # Update and Stopping all the threads
    for process in all_processes: process.join(.1); process.is_alive(); print('Terminating:', process.getName())
    sys.exit(0)