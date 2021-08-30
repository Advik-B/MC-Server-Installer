from versions.default import *

class Magma(Server):
    def __init__(version_number:str) -> str:
        

        versions = {

            '1.12':'https://www.mediafire.com/file/0t95jcbgint6bod/Magma-761933c-STABLE-server.jar/file',
            '1.12.2':'https://www.mediafire.com/file/un8i590pylhxx3r/Magma-dd991e7-DEV-server.jar/file',

        }

        versions['stable'] = versions['1.12']
        versions['dev'] = versions['1.12.2']

        version = versions.keys()
        if version_number in version:
            download_url = versions[version_number]
            return download_url
        else:
            print()
            print(f'The version "{version_number}" is not found!')
            print()
            return "about:blank"