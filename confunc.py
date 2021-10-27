#!/usr/bin/env python3
#: This is the config and functions file. 
#: DO NOT CHANGE IT UNLESS YOU KNOW WHAT YOU ARE DOING!


#NOTE: I get all the files from https://mcversions.net/


if __name__ == '__main__':
    print(f'Hey you running this file as {__name__}. Which means that you are running this file directly. Please import it instead!')
    exit(-1)
from bs4 import BeautifulSoup
import requests

class VersionError(Exception): """The selected version is invalid or unavailable"""
class LinkNotFound(Exception): """The page exists but the server links does not exist"""

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
        return link
    except IndexError:
        error = soup.find_all(class_=error_class)
        if len(error) == 0:
            raise LinkNotFound('The version %s is valid. but it does not have a server link.' % version)
        else:
            raise VersionError('The version %s is not valid' % version)

def download_server():
