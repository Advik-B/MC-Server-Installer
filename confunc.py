#!/usr/bin/env python3
#: DO NOT CHANGE IT UNLESS YOU KNOW WHAT YOU ARE DOING!
#: This is the config and functions file. Thats why it is called confunc

#NOTE: I get all the files from https://mcversions.net/

if __name__ == '__main__':
    print('You are running this file directly. Please import it instead!')
    exit(-1)

from bs4 import BeautifulSoup
from tkinter.ttk import Progressbar
from tkinter import messagebox
import cloudscraper
import yaml

requests = cloudscraper.create_scraper()

class VersionError(Exception): """The selected version is invalid or unavailable"""
class LinkNotFound(Exception): """The page exists but the server links does not exist"""

def get_server_link(version:str) -> str:
    global requests
    """Gets a server download link with the version given
    
    ---

    Args:
    -
    
        version (str): The version number. In a `str` instance

    Raises:
    -
    
        VersionError: If the version is not found. or is invalid

    Returns:
    -
    
        str: The direct download link.
    """
    download_pattern = 'https://mcversions.net/download/%s'

    # Classes for webpage
    link_class = 'text-xs whitespace-nowrap py-3 px-8 bg-green-700 hover:bg-green-900 rounded text-white no-underline font-bold transition-colors duration-200'
    error_class = 'error-details'

    r = requests.get(download_pattern % version)

    soup = BeautifulSoup(r.text, features='html.parser')
    try:
        return soup.find_all(class_=link_class)[0]['href']
    except IndexError:
        error = soup.find_all(class_=error_class)
        if len(error) == 0:
            raise LinkNotFound('The version %s is valid. but it does not have a server link.' % version)
        else:
            raise VersionError('The version %s is not valid' % version)

def download_server(version:str, output_folder:str=None):
    global requests
    import os
    from clint.textui import progress
    url = get_server_link(version)
    r = requests.get(url, stream=True)
    if output_folder is None:
        output_folder = os.getcwd()
        
    path = os.path.join(output_folder, 'server.jar')
    with open(path, 'wb') as f:
        total_length = int(r.headers.get('content-length', 0))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
            if chunk:
                f.write(chunk)
                f.flush()

def download_server_Tk_ST(version:str, bar:Progressbar, output_folder:str=None):
    global requests
    """
    Download The minecraft server(Single Threaded)
    
    ---
    
    Args:
    -
    
        version (str): The mineceaft version
        bar (Progressbar): The progress-bar
        output_folder (str, optional): The output-folder. Defaults to None.
    """
    import os
    from clint.textui import progress
    try:
        url = get_server_link(version)
    except VersionError:
        messagebox.showerror('Error', 'Could not find a matching server for %s' % version)
        return
    r = requests.get(url, stream=True)
    if output_folder is None:
        output_folder = os.getcwd()
    bar.done = False
    path = os.path.join(output_folder, 'server.jar')
    with open(path, 'wb') as f:
        total_length = int(r.headers.get('content-length', 0))
        bar.config(maximum=total_length)
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
            if chunk:
                f.write(chunk)
                f.flush()
                bar.step(1024)
    messagebox.showinfo('Done', 'The server has been downloaded.')
    bar.done = True

def download_server_Tk(version:str, bar:Progressbar, output_folder:str=None):
    """Download The minecraft server(Multi Threaded)
    
    ---
    Args:
    -
    
        version (str): The mineceaft version
        bar (Progressbar): The progress-bar
        output_folder (str, optional): The output-folder. Defaults to None.
    """
    from threading import Thread
    t = Thread(target=lambda: download_server_Tk_ST(version, bar, output_folder))
    t.daemon = True
    t.start()

def get_config(conf):
    config = {
        
        'memory_check': True,
               
    }
    try:
        with open('config.yml', 'r') as f:
            config_ = yaml.safe_load(f)
        return config_[conf]
    except FileNotFoundError:
        print('The config file is not found. Creating a new one.')
        with open('config.yml', 'w') as f:
            yaml.dump(config, f)
        return config[conf]
