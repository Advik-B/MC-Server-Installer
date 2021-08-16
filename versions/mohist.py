from versions.default import *

class Mohist(Server):
    def getlink(version_number:str) -> str:
        global versions

        versions = {

            '1.12':'https://www.mediafire.com/file/26u8agck00p8mhj/mohist-1.12.2-248-server.jar/file',

            '1.16':'https://www.mediafire.com/file/gviczn6hncjahdk/mohist-1.16.5-758-server.jar/file',

            '1.7':'https://www.mediafire.com/file/c698ezv2l8zopm2/Mohist-1.7.10-40-server.jar/file'
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