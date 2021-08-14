import requests
from bs4 import BeautifulSoup

class bukkit():
    def get_link(self , version_number:str) -> str:
        versions = {}
    
    def download(self) -> None:


        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
            }
        MediaUrl = 'http://www.mediafire.com/file/nbl3q4tx8l4tyto/Python_in_Arabic.txt/file'

        url = MediaUrl
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser')

        url = soup.find("a", class_="popsok").get('href')
        r = requests.get(url)

        print ("File Name : " + soup.find("div", class_="filename").get_text())
        print (soup.find("ul", class_="details").get_text())

        with open(soup.find("div", class_="filename").get_text(), 'wb') as f:
            f.write(r.content)
            print('Done ...')