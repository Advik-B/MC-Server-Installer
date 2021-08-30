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

#defining things
def clear() -> None:
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
    clear()

global data
global data2

data = {'1':'vanilla', '2':'bukkit', '3':'spigot', '4':'paper', '5':'forge', '6':'fabric', '7':'magma', '8':'mohist'}

for __key , __value in data.items():
    data2 = {__value:__key}

eula()

while True:
    answer = str(prinput('Do agree to the above license/agreement [Y/N]')).casefold()
    if  answer == 'n':
        exit(failed_to_agree())
    elif answer == 'y':
        print()
        break
    else:
        clear()
        error()
        eula()
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
        break
    except KeyError:
        
        continue

button()
cls()
print()

while True:
    cls()
    print('What version do you want')