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
from getpass import getpass

def eula() -> str:
    with open('./LICENSE' , mode='r') as f:
        content = f'{"Please read and accept the license agreement below to continue.".center(80)}\n\n{f.read()}'
        print(content.center(80))
        return content

def fail():
    print()
    __str = f'-^-^-^-^-^-^-^-^-^-YOU NEED TO AGREE TO THE ABOVE AGREEMENT!-^-^-^-^-^-^-^-^-^-'
    getpass(__str.center(80))

eula()

if  str(prinput('Do agree to the above license/agreement [Y/N]')).casefold() == 'n':
    exit(fail())
else:
    print('ahdegauydgewg')