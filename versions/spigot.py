from versions.default import *

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

            '1.14.3':'https://www.mediafire.com/file/5la5pf16e51dogb/spigot-1.14.3.jar/file',

            '1.14.4':'https://www.mediafire.com/file/lfz01psjwol1yal/spigot-1.14.4.jar/file',

            '1.14':'https://www.mediafire.com/file/jdmrjjhlggd94vp/spigot-1.14.jar/file',

            '1.15.1':'https://www.mediafire.com/file/99zg8e9w7w47crz/spigot-1.15.1.jar/file',

            '1.15.2':'https://www.mediafire.com/file/wg7ftags71q9prj/spigot-1.15.2.jar/file',

            '1.15':'https://www.mediafire.com/file/r86qlz2bau1pcgj/spigot-1.15.jar/file',

            '1.16.1':'https://www.mediafire.com/file/i4ko4d4tcg0gits/spigot-1.16.1.jar/file',

            '1.16.2':'https://www.mediafire.com/file/7k8hte1dpyrv1vk/spigot-1.16.2.jar/file',
            
            '1.16.3':'https://www.mediafire.com/file/x6w878ikd5hmzuv/spigot-1.16.3.jar/file',

            '1.16.4':'https://www.mediafire.com/file/nsj197tejjb2dmv/spigot-1.16.4.jar/file',

            '1.16.5':'https://www.mediafire.com/file/3xvbme1lsi1ku77/spigot-1.16.5.jar/file',

            '1.17.1':'https://www.mediafire.com/file/f4vjs1x91lzdcrn/spigot-1.17.1.jar/file',

            '1.17':'https://www.mediafire.com/file/w4u3si7l3uk9gi5/spigot-1.17.jar/file',

            '1.4.6':'https://www.mediafire.com/file/bpw16aa4mftm9f6/spigot-1.4.6-R0.4-SNAPSHOT.jar/file',

            '1.4.7':'https://www.mediafire.com/file/qw1x1t59oryfjud/spigot-1.4.7-R1.1-SNAPSHOT.jar/file',

            '1.5.1':'https://www.mediafire.com/file/6ihc745pxp9upik/spigot-1.5.1-R0.1-SNAPSHOT.jar/file',

            '1.5.2':'https://www.mediafire.com/file/iql2va0dy2vbxj8/spigot-1.5.2-R1.1-SNAPSHOT.jar/file',

            '1.6.2':'https://www.mediafire.com/file/toks4drsbukcw9f/spigot-1.6.2-R1.1-SNAPSHOT.jar/file',

            '1.6.4':'https://www.mediafire.com/file/0nwqqw02o20qvj9/spigot-1.6.4-R2.1-SNAPSHOT.jar/file',

            '1.7.1':'https://www.mediafire.com/file/z0ipojgo5e6z3se/spigot-1.7.10-SNAPSHOT-b1657.jar/file',

            '1.7.2':'https://www.mediafire.com/file/0gteikk6ex09lcd/spigot-1.7.2-R0.4-SNAPSHOT-1339.jar/file',

            '1.7.5':'https://www.mediafire.com/file/hpw5tkk4m500o07/spigot-1.7.5-R0.1-SNAPSHOT-1387.jar/file',

            '1.7.8':'https://www.mediafire.com/file/edpusonnv4bybpx/spigot-1.7.8-R0.1-SNAPSHOT.jar/file',

            '1.7.9':'https://www.mediafire.com/file/sp7m3x41e0gn6qu/spigot-1.7.9-R0.2-SNAPSHOT.jar/file',

            '1.8':'https://www.mediafire.com/file/7ycabsfwr1cesrm/spigot-1.8-R0.1-SNAPSHOT-latest.jar/file',

            '1.8.3':'https://www.mediafire.com/file/7ycabsfwr1cesrm/spigot-1.8-R0.1-SNAPSHOT-latest.jar/file',

            '1.8.4':'https://www.mediafire.com/file/qrvra1pz5eao7t4/spigot-1.8.4-R0.1-SNAPSHOT-latest.jar/file',

            '1.8.5':'https://www.mediafire.com/file/ty67ouyz3acl9ai/spigot-1.8.5-R0.1-SNAPSHOT-latest.jar/file',

            '1.8.6':'https://www.mediafire.com/file/i48nutt89kummqz/spigot-1.8.6-R0.1-SNAPSHOT-latest.jar/file',

            '1.8.7':'https://www.mediafire.com/file/7w07vwrbjqc438w/spigot-1.8.7-R0.1-SNAPSHOT-latest.jar/file',

            '1.8.9':'https://www.mediafire.com/file/zksdyc9m0g0vy3x/spigot-1.8.8-R0.1-SNAPSHOT-latest.jar/file',

            '1.9':'https://www.mediafire.com/file/wt4x0655q9pmrrx/spigot-1.9-R0.1-SNAPSHOT-latest.jar/file',

            '1.9.2':'https://www.mediafire.com/file/zl0czzzk5v5tn6m/spigot-1.9.2-R0.1-SNAPSHOT-latest.jar/file',

            '1.9.4':'https://www.mediafire.com/file/bl0quxbkrmyoyoa/spigot-1.9.4-R0.1-SNAPSHOT-latest.jar/file'
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