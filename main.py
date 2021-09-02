from threading import *
from versions.fabric import *
from versions.forge import *
from versions.paper import *
from versions.magma import * 
from versions.bukkit import *
from versions.spigot import *
from versions.default import *
from versions.mohist import *
from function.most_used import *
from sounds import *
from getpass import getpass
from getch import *
import tempfile
import shutil

#Functions
def clear() -> None:
    """Will clear the screen"""
    os.system("cls")

def eula() -> str:
    with open('./LICENSE' , mode='r') as f:
        content = f'{"Please read and accept the license agreement below to continue.".center(80)}\n\n\n{f.read()}'
        print(content.center(80))
        return content

def failed_to_agree() -> 1:
    error()
    print()
    __str = f'-^-^-^-^-^-^-^-^-^-YOU NEED TO AGREE TO THE ABOVE AGREEMENT!-^-^-^-^-^-^-^-^-^-'
    getpass(__str.center(80))
    return 1

def list_versions():
    for key , val in data.items():
        print(key,'|',val)
        print('------------')

def cls():
    """Will clear the screen"""
    clear()

def check_versions(type , version):
    print(type(version))

def gettempfol(mode:bool=True):
    __temp_fol = str(tempfile.gettempdir().replace('\\' , '/').__add__('/server-pycache'))
    
    try:
        os.mkdir(__temp_fol)
    except:
        pass


    return  __temp_fol

# Defining things
global data
global data2
global current_version
data = {'1':'vanilla', '2':'bukkit', '3':'spigot', '4':'paper', '5':'forge', '6':'fabric', '7':'magma', '8':'mohist'}
desktop = str(os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')).replace('\\' , '/')

for __key , __value in data.items():
    data2 = {__value:__key}

while True:
    clear()
    error()
    eula()
    try:
        conf = open('./settings.conf' , 'r')
    except FileNotFoundError:
        conf = open('./settings.conf' , 'w+')

    if conf.read() == 'true':
        break
    else:
        pass
    answer = str(prinput('Do agree to the above license/agreement [Y/N]')).casefold()
    if  answer == 'n':
        exit(failed_to_agree())
    elif answer == 'y':
        print()
        conf.write('true')
        break
    else:
        continue #looping

button()
cls()
print()

while True:
    cls()
    print('Choose your server-type!\n')
    list_versions()
    version = input('>>> ')
    try:
        current_version = data[version.casefold()]
        del version
        break
    except KeyError:
        error()
        continue

button()
cls()
print()

# Getting the versions
versions = {

    'bukkit': Bukkit,
    'spigot': Spigot,
    'paper' : Paper,
    'forge' : Forge,
    'fabric': Fabric,
    'magma' : Magma,
    'mohist': Mohist,

    }

version = versions.get(current_version)


while True:
    cls()
    print('What version do you want')
    get_version = input('>>> ')
    sel_version = version.getlink(get_version)
    if sel_version == 'about:blank':
        print('Server not found')
        error()
        continue
    else:
        print()
        server_path_temp = gettempfol().__add__(f'/{get_version}')
        try:
            os.mkdir(server_path_temp)
        except FileExistsError:
            os.remove(server_path_temp)
            os.mkdir(server_path_temp)

        if version == Fabric or version == Forge:
            Server.zip_download(sel_version , folder_path=server_path_temp)
        else:
            Server.download(sel_version , folder_path=server_path_temp)
        ding()
        break

cls()
print()

while True:
    cls()
    print('Do you want to install the server on a custom folder? [Y/N]')
    y_or_n = input('>>> ')
    if y_or_n.casefold() == 'y':
        print()
        print('What is the path of your folder? [FULL PATH!]? ')
        custom_path = input('>>> ')
        custom_path = custom_path.replace('"' , '').replace("'", '')
        
        if os.path.isdir(custom_path) == False:
            os.mkdir(custom_path)
        else:
            pass
        return_path = shutil.move(server_path_temp , custom_path)
        print()
        print(f'Your server is located in :"{return_path}"!')
        print()
        ding()
        break
    elif y_or_n.casefold() == 'n':
        if os.path.isdir(desktop.__add__('/py-server')) == False:
            os.mkdir(desktop.__add__('/py-server'))
        else:
            pass

        return_path = (shutil.move(server_path_temp , desktop.__add__('/py-server'))).replace('\\' , '/')
        print(f'Your server is located in "{return_path}"!')
        break

print('\n'*2)
pause_exit(0 ,  'Press any key to exit !')