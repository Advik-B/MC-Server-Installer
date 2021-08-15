from default import *


class Spigot(Server):
    def getlink(version_number:str) -> str:
        global versions

        versions = {

            '1.10':'https://www.mediafire.com/file/lot0p12ts5xh15g/spigot-1.10-R0.1-SNAPSHOT-latest.jar/file',

            '1.10.2':'https://www.mediafire.com/file/v8mmdtu8lbuvlcy/spigot-1.10.2-R0.1-SNAPSHOT-latest.jar/file',

            '1.11.1':'https://www.mediafire.com/file/aaswf8qqeuw6zw3/spigot-1.11.1.jar/file',

            '1.11.2':'https://www.mediafire.com/file/cks1tmwgmhdz59r/spigot-1.11.2.jar/file',

            '1.11':"https://www.mediafire.com/file/7m03qwyeigy50fy/spigot-1.11.jar/file",

            '1.12.1':'https://www.mediafire.com/file/jcdxfta78i9sgvb/spigot-1.12.1.jar/file',

            '1.12.2':"https://www.mediafire.com/file/kjnnj1i2qv30j2g/spigot-1.12.2.jar/file",

            '1.12':'https://www.mediafire.com/file/9e0fybuymwqvh70/spigot-1.12.jar/file',

            '1.13.1':'https://www.mediafire.com/file/u4ldh0o83ckweb3/spigot-1.13.1.jar/file',

            '1.13.2':'https://www.mediafire.com/file/6tdwcnvffbr77br/spigot-1.13.2.jar/file',

            '1.13':'https://www.mediafire.com/file/mra2jye2986uim3/spigot-1.13.jar/file',

            '1.14.1':'https://www.mediafire.com/file/9njc51qlh9zzi1t/spigot-1.14.1.jar/file',

            '1.14.2':'https://www.mediafire.com/file/mdbwmbaj811y94q/spigot-1.14.2.jar/file',

            
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