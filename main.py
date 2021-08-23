from tkinter import *
from tkinter import ttk , filedialog
from PIL import ImageTk , Image
import os

root = Tk()

def open_file() -> None:
    global my_image
    filename = filedialog.askopenfilename(initialdir=os.getcwd() , title='Please choose an image' , filetypes=(('jpg files' , '*.jpg') , ('png files' , '*.png') , ('internet files' , '*.svg')))
    image = ImageTk.PhotoImage(Image.open(filename))
    image_label = Label(image=image)
    image_label.pack()

Open_an_image = ttk.Button(root ,text='Open an image' ,width=20, padding=10 , command=open_file)

Open_an_image.pack()

root.geometry('500x500')
root.mainloop()