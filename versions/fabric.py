from default import *

class Fabric(Server):
    def getlink(version_number:str) -> str:
        global versions

        versions = {
            '1.14':'https://www.mediafire.com/file/kmc9pl2c8l4iivw/1.14.zip/file',

            '1.15':'https://www.mediafire.com/file/u2ny4aodnnerlol/1.15.zip/file',

            '1.16':'https://www.mediafire.com/file/fss23rtr02330rt/1.16.zip/file',

            '1.17':'https://www.mediafire.com/file/6tm454cljfwgzrn/1.17.zip/file'
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