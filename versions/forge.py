from versions.default import *

class Forge(Server):
    def getlink(version_number:str) -> str:
        global versions

        versions = {}

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