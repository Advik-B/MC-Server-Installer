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

#defining things
global mode
mode = False


eula()
while True:
    answer = str(prinput('Do agree to the above license/agreement [Y/N]')).casefold()
    if  answer == 'n':
        exit(failed_to_agree())
    elif answer == 'y':
        print()
        mode = True
        break
    else:
        clear()
        error()
        eula()
        continue #looping

if mode == True:
    pass