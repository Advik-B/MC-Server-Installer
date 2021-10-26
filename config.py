#!/usr/bin/env python3
#: This is the config file. 
#: DO NOT CHANGE IT UNLESS YOU KNOW WHAT YOU ARE DOING!


#NOTE: I get all the files from https://mcversions.net/
#TODO: Add some config shit here

#TEMP: BEGINING: All the code below this is temp and will be removed
from bs4 import BeautifulSoup
import requests

class VersionError(Exception): pass # This is a one-line class. Just to make an error instance

def get_server(version:str) -> str:
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
        link = soup.find_all(class_=link_class)[0]['href']# This will get the pure link
    except IndexError:
        print('Oh boy! it looks like there is no server download button here.')
    
    error = soup.find_all(class_=error_class)


    if len(error) == 0:
        return link
    else:
        raise VersionError('The version %s is not valid' % version)


get_server('1.8.sdf9')
#TEMP: END: All the code form this line starts counting