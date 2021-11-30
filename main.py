from tkinter import Tk, Label, Button, Entry, StringVar, END, W, E, messagebox
from tkinter.ttk import Frame, Style
from confunc import download_server_Tk, get_config
import psutil

class Main(Tk):
    def init(self):
        self.mem = psutil.virtual_memory() # Getting the current system memory
        self.mini_mem = 2500 * 1024 * 1024 # 2.5 GB
        self.title("My Application")
        self.screen_height = self.winfo_screenheight()
        self.screen_width = self.winfo_screenwidth()
        self.gm1 = int(self.screen_width * .6)
        self.gm2 = int(self.screen_height * .6)
        self.gm3 = int(self.screen_width * .25)
        self.gm4 = int(self.screen_height * .2)
        self.geometry("%sx%s+%s+%s" % (self.gm1, self.gm2, self.gm3, self.gm4))   
        self.resizable(False, False)
        self.configure(bg="#7289DA")
        if self.mem.total < self.mini_mem and get_config("memory_check") is True:
            messagebox.showinfo(
                "Memory Warning",
                "You have enough memory to run minecraft servers on your computer",
                icon="warning",
                )
        

    def start(self):
        self.init()
        self.mainloop()

App = Main()
App.start()