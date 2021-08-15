import subprocess
import os
import requests
from bs4 import BeautifulSoup

class Server():
    def download(link:str , folder_path=None)  -> None:


        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
            }
        MediaUrl = link

        url = MediaUrl
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser')

        url = soup.find("a", class_="popsok").get('href')
        r = requests.get(url)
        if folder_path != None:
            file_path = folder_path.__add__('/server.jar').replace('\\' , '/')
        else:
            file_path = ('./server.jar')

        print ("File Name : " + soup.find("div", class_="filename").get_text())
        print (soup.find("ul", class_="details").get_text())

        with open(file_path, 'wb') as f:
            f.write(r.content)
            print('Sucessfully downloaded the server file!')

    def runserver(server_folder=None , run_command=None , server_file_name=None) -> None:
        cwd = os.getcwd()
        path = server_folder
        eula = str(os.path.join(path , 'eula.txt')).replace('\\' , '/')
        global eula_content

        if server_folder == None:
            if server_file_name == None:
                server_file_name = 'server.jar'
            if run_command == None:
                run_command = 'java -Xmx1024M -Xms1024M -jar'  
                  
            eula_content = "#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n#Sun Aug 15 09:55:51 IST 2021\neula=true"
            with open(eula, mode='w+') as f:
                f.write(eula_content)

            subprocess.Popen(f'{run_command} {server_file_name} nogui' , cwd=(os.getcwd()))
        elif server_folder != None:
            if server_file_name == None:
                server_file_name = 'server.jar'

            if run_command == None:
                run_command = 'java -Xmx1024M -Xms1024M -jar'
            eula_content = "#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n#Sun Aug 15 09:55:51 IST 2021\neula=true"
            with open(eula, mode='w+') as f:
                f.write(eula_content)
            subprocess.Popen(f'{run_command} {server_file_name} nogui' , cwd=path)