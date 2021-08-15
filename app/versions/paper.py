import subprocess
import os
import requests
from bs4 import BeautifulSoup


class Paper():
    def getlink(version_number:str) -> str:
        global versions

        versions = {

            '1.10.2':'https://www.mediafire.com/file/1ds9hhiuvhazn5e/paper-1.10.2-916.jar/file',

            '1.11.2':'https://www.mediafire.com/file/eeidpu8dcg0h23v/paper-1.11.2-1104.jar/file',

            '1.12.2':"https://www.mediafire.com/file/qhop9drado0wwax/paper-1.12.2-1618.jar/file",

            '1.13.2':'https://www.mediafire.com/file/c0a19hcqag70mcc/paper-1.13.2-655.jar/file',

            '1.14.4':'https://www.mediafire.com/file/818earslka4fjoy/paper-1.14.4-243.jar/file',

            '1.15.2':'https://www.mediafire.com/file/zsdkqs8s2ae4z2h/paper-1.15.2-391.jar/file',

            '1.16.5':'https://www.mediafire.com/file/pfyj4n1lbc2grm7/paper-1.16.5-786.jar/file',

            '1.17.1':'https://www.mediafire.com/file/6dzmfryu6f7lbwk/paper-1.17.1-186.jar/file',

            '1.8.9':'https://www.mediafire.com/file/346u26k0t169x7t/paper-1.8.8-443.jar/file',

            '1.9.4':'https://www.mediafire.com/file/p4qbs1z59emqsy6/paper-1.9.4-773.jar/file'
        }
        version = versions.keys()
        if version_number in version:
            download_url = versions[version_number]
            return download_url
        else:
            print()
            print(f'The version "{version_number}" is not found!')
            print()
            return "about:blank"

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

Paper.download(link=(Paper.getlink('1.12.2')) , folder_path='C:/Users/advik/Desktop/temp')

Paper.runserver(server_folder='C:/Users/advik/Desktop/temp')