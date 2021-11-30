from tkinter import Tk, W, E, messagebox, ttk, filedialog, Frame
from confunc import download_server_Tk, get_config
import psutil
import json
import os
import random
import tkcode

class Main(Tk):
    def init(self):
        self.mem = psutil.virtual_memory() # Getting the current system memory
        self.mini_mem = 2500 * 1024 * 1024 # 2.5 GB
        self.title("Minecraft Server Installer")
        self.screen_height = self.winfo_screenheight()
        self.screen_width = self.winfo_screenwidth()
        self.gm1 = int(self.screen_width * .6)
        self.gm2 = int(self.screen_height * .6)
        self.gm3 = int(self.screen_width * .25)
        self.gm4 = int(self.screen_height * .2)
        self.geometry(
            "%sx%s+%s+%s" % (
            self.gm1,
            self.gm2,
            self.gm3,
            self.gm4
                            ),
                      )
        
        self.resizable(False, False)
        self.configure(bg="#7289DA")
        self.load_icon()
        # Binding the close button to the close function
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.ver = self.load_versions()
        self.versions = self.ver['stable']
        self.version = ttk.Combobox(self,
                                    values=self.versions,
                                    width=20,
                                    state="readonly",
                                    font=("Consolas", 12),
                                    )
        self.version_lbl = ttk.Label(self,
                                     text="Version: ",
                                     font=("Helvetica", 16),
                                     background="#7289DA",
                                     foreground="black")
        self.filter__lbl = ttk.Label(self,
                                   text="Filter: ",
                                   font=("Helvetica", 16),
                                   background="#7289DA",
                                   foreground="black")
        self.filter_ = ttk.Combobox(self,
                                values=["Stable", "Snapshot"],
                                state="readonly",
                                width=30,
                                font=("Consolas", 12),
            )
        self.output_lbl = ttk.Label(self,
                                    text="Output Folder: ",
                                    font=("Helvetica", 16),
                                    foreground="black",
                                    background="#7289DA",
                                    )
        self.output_ = ttk.Entry(self,
                                 font=("Consolas", 12),
                                 width=60,
                                 )
        self.output_bt= ttk.Button(self,
                                   text="Browse",
                                   command=self.output_browse,
                                   width=10,    
                                    )
        self.mainframe = Frame(self,
                               background="#7289DA",
            )
        # MainFrame
        self.download_bt = ttk.Button(self.mainframe,
                                      text="Start Download!",
                                      command=self.download_server,
                                      width=20,
                                      )
        self.progress_bar = ttk.Progressbar(self.mainframe,
                                            orient="horizontal",
                                            length=self.gm1 // 2,
                                            mode="determinate",
                                            maximum=100,
                                            value=0,
                                            )
        self.progress_bar_lbl = ttk.Label(self.mainframe,
                                          text="Progress: ",
                                          font=("Helvetica", 16),
                                          foreground="black",
                                          background="#7289DA",
                                          )
        self.license_ = tkcode.CodeEditor(self.mainframe,
                                  font=("Consolas", 12),
                                  foreground="black",
                                  background="#7289DA",
                                  language="Brainfuck",
                                  height=18,
                                  state="disabled",
                                  highlighter="custom_theme.json",
                                  )
        
        self.filter_.current(0)
        self.version.current(0)
        self.license_.configure(state="normal",)
        self.license_.insert(1.0, self.load_license())
        self.license_.configure(state="disabled")
        
        self.filter_.bind("<<ComboboxSelected>>", self.filter_change)
        self.version_lbl.grid(row=0, column=0, sticky=W, padx=10, pady=10)
        self.version.grid(row=0, column=1, sticky=E, pady=10)
        self.filter__lbl.grid(row=0, column=2, sticky=W, padx=10, pady=10)
        self.filter_.grid(row=0, column=3, sticky=W, pady=10)
        self.output_lbl.grid(row=1, column=0, sticky=W, padx=10, pady=10, ipadx=85,columnspan=2)
        self.output_.grid(row=1, column=1, sticky=E, pady=10, padx=10, columnspan=3)
        self.output_bt.grid(row=1, column=10, sticky=E, pady=10,  columnspan=4)
        self.mainframe.grid(row=2, column=0, sticky=W, pady=10, columnspan=10)
        # MAINFRAME GRID
        self.progress_bar_lbl.grid(row=0, column=0, sticky=W, padx=10, pady=10)
        self.progress_bar.grid(row=0, column=1, sticky=E, pady=10, padx=10)
        self.download_bt.grid(row=0, column=2, sticky=W, pady=10, padx=10, columnspan=100)
        self.license_.grid(row=1, column=0, sticky=E, pady=10, padx=10, columnspan=3)
        if self.mem.total < self.mini_mem and get_config("memory_check") is True:
            messagebox.showinfo(
                "Memory Warning",
                "You have enough memory to run minecraft servers on your computer",
                icon="warning",
                )

    @staticmethod
    def load_versions():
        with open('versions.json', 'r') as f:
            return json.load(f)

    def filter_change(self, event):
        print('Filter changed to:', self.filter_.get())
        # Never gonna use this. I'll just leave it here for now. just in case.
        # API_URL = "https://launchermeta.mojang.com/mc/game/version_manifest.json"
        if self.filter_.get() == "Stable":
            self.versions = self.ver['stable']
        elif self.filter_.get() == "Snapshot":
            self.versions = self.ver['snapshots']
        self.version['values'] = self.versions
        self.version.current(0)
     
    def close(self):
        try:
            if (
                self.progress_bar.done is False
                and messagebox.askyesno(
                    "Close Warning",
                    "Are you sure you want to close? Download in progress!. You will not be able to resume the download.",
                )
                is True
                or self.progress_bar.done is not False
            ):
                self.destroy()
            else:
                return
        except AttributeError:
            self.destroy()
 
    def load_icon(self):
        icons = os.listdir(
            os.path.join(
                os.getcwd(),
                "assets",
                "pictures",
                "icons"),
                           )
        icon = os.path.join(
            os.getcwd(),
            'assets',
            'pictures',
            'icons',
            random.choice(icons),
            )
        self.iconbitmap(icon)

    def load_license(self):
        with open('LICENSE', 'r') as f:
            license = f.read()
        return license

    def output_browse(self):
        folder = filedialog.askdirectory(parent=self,
                                         title='Select Output Folder',
                                         initialdir=os.path.expanduser('~'),
                                         mustexist=True,)
        if folder:
            self.output_.delete(0, 'end')
            self.output_.insert(0, folder)

    def download_server(self):
        version = self.version.get()
        output = self.output_.get()
        self.progress_bar.done = False
        download_server_Tk(version, self.progress_bar, output)

    def start(self):
        self.init()
        self.mainloop()

def main():
    app = Main()
    app.start()

if __name__ == '__main__':
    main()