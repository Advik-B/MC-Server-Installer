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
import platform
import json_util
import psutil
from PIL import Image, ImageTk
from random import randint

mem = psutil.virtual_memory() # Getting the current system memory
mini_mem = 2500 * 1024 * 1024 # 2.5 GB
print(mem)

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
icons = []
for icon in os.listdir(os.path.join(cwd, 'assets/pictures/icons')):
    icons.append(os.path.join(os.path.join(cwd, 'assets/pictures/icons'), icon))
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
raw_json = open('versions.json')

ver = json_util.convert_json(data=raw_json.read(), mode=1)

versions.extend(ver['stable'])
versions.extend(ver['snapshots'])

binFont = ['Vendara', 18]

del ver
raw_json.close()

ver = StringVar()
versions_ = ttk.Combobox(gui, values=versions, textvariable=ver, background='#2b2d37', foreground='#2b2d37')
Title = ttk.Label(gui, text='Please choose your server version.', font=binFont, background='#2b2d37', foreground='white')#TODO: change `server` to `minecraft`

Title.grid(row=1, column=0, padx=150)
versions_.grid(row=2, column=0, pady=15)

# </code>

# making the windows appear
if __name__ == '__main__': # Making shure that the file is run directly
    if mem.total < mini_mem:
        messagebox.showwarning(':::: WARNING ::::', 'WARNING: Not enough memory to run Minecraft servers\n\t   The servers will be slow and laggy!')
    gui.mainloop()