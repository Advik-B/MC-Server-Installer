import requests
from bs4 import BeautifulSoup

class bukkit():
    def get_link(self , version_number:str) -> str:
        global versions

        versions = {

            "1.0.0":"https://www.mediafire.com/file/qggkbn2uombgzwb/craftbukkit-1.0.0-SNAPSHOT.jar/file",

            "1.10":"https://www.mediafire.com/file/4muyx3rb98awvw6/craftbukkit-1.10-R0.1-SNAPSHOT-latest.jar/file",

            "1.10.2":"https://www.mediafire.com/file/o08fbh02ww2nq40/craftbukkit-1.10.2-R0.1-SNAPSHOT-latest.jar/file",

            "1.11.2":"https://www.mediafire.com/file/q1vrwe5elv54uuu/craftbukkit-1.11.2.jar/file",

            "1.11":"https://www.mediafire.com/file/z9ltk0q3j6nkckr/craftbukkit-1.11.jar/file",

            "1.12.1":"https://www.mediafire.com/file/tn0rd9q5ag0myzv/craftbukkit-1.12.1.jar/file",

            "1.12.2":"https://www.mediafire.com/file/5lr743des9lxtna/craftbukkit-1.12.2.jar/file",

            "1.12":"https://www.mediafire.com/file/qyko6n15qw5afkc/craftbukkit-1.12.jar/file",

            "1.13.1":"https://www.mediafire.com/file/dk1besx741fwksv/craftbukkit-1.13.1.jar/file",

            "1.13.2":"https://www.mediafire.com/file/t2lkvsk99iq0yat/craftbukkit-1.13.2.jar/file",

            "1.13":'https://www.mediafire.com/file/2rz969qsrzqef0z/craftbukkit-1.13.jar/file',

            '1.14':'https://www.mediafire.com/file/ioytx5z1mhy893f/craftbukkit-1.14-R0.1-SNAPSHOT.jar/file',

            '1.14.2':'https://www.mediafire.com/file/duo23noczmdpxwh/craftbukkit-1.14.2-R0.1-SNAPSHOT.jar/file',

            '1.14.3':'https://www.mediafire.com/file/sausc668quk9r3y/craftbukkit-1.14.3-R0.1-SNAPSHOT.jar/file',

            '1.14.4':'https://www.mediafire.com/file/9d207zqzwnygvso/craftbukkit-1.14.4-R0.1-SNAPSHOT.jar/file',

            '1.15':'https://www.mediafire.com/file/f3s3e3djyyvnrg4/craftbukkit-1.15-R0.1-SNAPSHOT.jar/file',

            '1.15.1':'https://www.mediafire.com/file/qv4b4d702wgtaaw/craftbukkit-1.15.1-R0.1-SNAPSHOT.jar/file',

            '1.15.2':'https://www.mediafire.com/file/w4e46yw6uckcti8/craftbukkit-1.15.2.jar/file',

            '1.16.1':'https://www.mediafire.com/file/fqdrne6f94t0ssv/craftbukkit-1.16.1.jar/file',

            '1.16.2':'https://www.mediafire.com/file/tde6gqja0p8u5jn/craftbukkit-1.16.2.jar/file',

            '1.16.3':'https://www.mediafire.com/file/cfw0z21ch0x9pru/craftbukkit-1.16.3.jar/file',

            '1.16.5':'https://www.mediafire.com/file/7ygmx9kx6avrcg6/craftbukkit-1.16.5.jar/file'
            }
        self.versions = versions

    def download(self , link:str) -> None:


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

        print ("File Name : " + soup.find("div", class_="filename").get_text())
        print (soup.find("ul", class_="details").get_text())

        with open(soup.find("div", class_="filename").get_text(), 'wb') as f:
            f.write(r.content)
            print('Done ...')