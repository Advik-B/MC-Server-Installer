from versions.default import *
from tkinter import *
from tkinter import ttk
from threading import Thread
import pygame.mixer
import time

pygame.mixer.init()
s1 = Tk()
def run():
    s1.mainloop()

s1.title('Server installer')
s1.geometry('740x635')
s1.iconbitmap('./assets/pictures/icon.ico')

def keep_alive():
    t = Thread(target=run)
    t.start()