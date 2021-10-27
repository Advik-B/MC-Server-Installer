#!/usr/bin/env python3

# importing GUI modules
from tkinter import *
from ttkthemes import themed_tk
from tkinter import ttk

# import the other stuff
import os
import confunc
import shutil
import subprocess
import platform
import json_util
from random import randint

# The current working dirctory
cwd = os.getcwd()

# gui instance
gui = themed_tk.ThemedTk()

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

# <code>
versions = []
raw_json = open('versions.json')

ver = json_util.convert_json(data=raw_json.read(), mode=1)

versions.extend(ver['stable'])
versions.extend(ver['snapshots'])

del ver
raw_json.close()

ver = StringVar()
versions_ = ttk.Combobox(gui, values=versions, state='readonly', textvariable=ver)
Title = ttk.Label(gui, text='Please choose you minecraft version.')
# </code>

# making the windows appear
if __name__ == '__main__': # Making shure that the file is run directly
    gui.mainloop()