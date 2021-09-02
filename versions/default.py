import os
try:
    import subprocess
    import requests
    from bs4 import BeautifulSoup
    from zipfile import ZipFile
except ModuleNotFoundError:
    os.system('python -m pip install -r requirements.txt')
    import subprocess
    import requests
    from bs4 import BeautifulSoup
    from zipfile import ZipFile


class Server():
    """
    
    forge and fabric require you use the `zip_download` command

    """
    
    def download(link:str , folder_path=None)  -> None:

        """
    
        forge and fabric require you use the `zip_download` command

        """


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
        r = requests.get(url , stream=True)
        if folder_path != None:
            file_path = folder_path.__add__('/server.jar').replace('\\' , '/')
        else:
            file_path = ('./server.jar')

        print ("Server-Type : " + soup.find("div", class_="filename").get_text())
        print (soup.find("ul", class_="details").get_text())

        print('Downloading, please wait.')
        with open(file_path,'wb') as f:
            for chunk in r.iter_content(chunk_size=1000):
                if chunk:
                    f.write(chunk)
        print()
        print('Download completed!')

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
    
    def zip_download(link:str , folder_path=None) -> None:
        """
    
            forge and fabric require you use the `zip_download` command

        """

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
        r = requests.get(url ,stream=True)
        if folder_path != None:
            file_path = folder_path.__add__('/server.zip').replace('\\' , '/')
        else:
            file_path = ('./server.zip')

        print ("Server-Type : " + soup.find("div", class_="filename").get_text())
        print (soup.find("ul", class_="details").get_text())

        print('Downloading, please wait.')
        with open(file_path,'wb') as f:
            for chunk in r.iter_content(chunk_size=1000):
                if chunk:
                    f.write(chunk)
        print()
        print('Download completed!')

        # importing required modules
        from zipfile import ZipFile
        
        # specifying the zip file name
        
        # opening the zip file in READ mode
        with ZipFile(file_path, 'r') as zip:
            # printing all the contents of the zip file
            # extracting all the files
            zip.extractall(folder_path)
        os.remove(file_path)