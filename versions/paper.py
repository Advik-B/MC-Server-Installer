from versions.default import *

class Paper(Server):
    def __init__(version_number:str) -> str:
        

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