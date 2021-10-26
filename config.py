#! This is the config file. 
#! DO NOT CHANGE IT UNLESS YOU KNOW WHAT YOU ARE DOING!
#! NOTE: I get all the files from https://mcversions.net/
#TODO: Add some config shit here

#TEMP: BEGINING: All the code below this is temp and will be removed
from bs4 import BeautifulSoup
import requests

download_pattern = 'https://mcversions.net/download/%s'

needed_class = 'text-xs whitespace-nowrap py-3 px-8 bg-green-700 hover:bg-green-900 rounded text-white no-underline font-bold transition-colors duration-200'

r = requests.get('https://mcversions.net/download/1.17.1')
r2 = BeautifulSoup(r.text, features='html.parser')
class__ = r2.find_all(class_=needed_class)
print(class__)
#TEMP: END: All the code form this line starts counting