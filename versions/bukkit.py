from versions.default import *

class Bukkit(Server):
    def getlink(version_number:str) -> str:
        

        versions = {

            "1.0":"https://www.mediafire.com/file/qggkbn2uombgzwb/craftbukkit-1.0.0-SNAPSHOT.jar/file",

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

            '1.16.5':'https://www.mediafire.com/file/7ygmx9kx6avrcg6/craftbukkit-1.16.5.jar/file',

            '1.17.1':'https://www.mediafire.com/file/82m7dmmr5zucms2/craftbukkit-1.17.1.jar/file',

            '1.17':'https://www.mediafire.com/file/zgxj5vj1rzagd0w/craftbukkit-1.17.jar/file',

            '1.5':'https://www.mediafire.com/file/vedvarjpk94pjkm/craftbukkit-1.5-R0.1-20130317.180842-21.jar/file',

            '1.5.1':'https://www.mediafire.com/file/059tkqx8f6lucvv/craftbukkit-1.5.1-R0.2-SNAPSHOT.jar/file',

            '1.5.2':'https://www.mediafire.com/file/fkhxs9lmfjpeke2/craftbukkit-1.5.2-R1.0.jar/file',

            '1.6.1':'https://www.mediafire.com/file/bvm5uaj6jwzhtfv/craftbukkit-1.6.1-R0.1-SNAPSHOT.jar/file',

            '1.6.2':'https://www.mediafire.com/file/7wufblk1pxx9hoz/craftbukkit-1.6.2-R0.1-SNAPSHOT.jar/file',

            '1.6.4':'https://www.mediafire.com/file/zbiaup01m60muho/craftbukkit-1.6.4-R2.0.jar/file',

            '1.7.10':'https://www.mediafire.com/file/08q8kt9ew4gp3uo/craftbukkit-1.7.10-R0.1-20140808.005431-8.jar/file',

            '1.7.2':'https://www.mediafire.com/file/ygrbvn740d7e7xh/craftbukkit-1.7.2-R0.4-20140216.012104-3.jar/file',

            '1.7.5':'https://www.mediafire.com/file/vo3wf2syjrd69ej/craftbukkit-1.7.5-R0.1-20140402.020013-12.jar/file',

            '1.7.8':'https://www.mediafire.com/file/t9zin87c41jexpr/craftbukkit-1.7.8-R0.1-SNAPSHOT.jar/file',

            '1.7.9':'https://www.mediafire.com/file/qrdipu15pp8eemg/craftbukkit-1.7.9-R0.2-SNAPSHOT.jar/file',

            '1.8':'https://www.mediafire.com/file/6tg00x0z1k8kfrr/craftbukkit-1.8-R0.1-SNAPSHOT-latest.jar/file',

            '1.8.3':'https://www.mediafire.com/file/a8d2j3g5dxgbsk2/craftbukkit-1.8.3-R0.1-SNAPSHOT-latest.jar/file',

            '1.8.5':'https://www.mediafire.com/file/8f78h29eauwj6nj/craftbukkit-1.8.5-R0.1-SNAPSHOT-latest.jar/file',

            '1.8.6':'https://www.mediafire.com/file/e6h81q5l06p7cb0/craftbukkit-1.8.6-R0.1-SNAPSHOT-latest.jar/file',

            '1.8.7':'https://www.mediafire.com/file/4b1hbyzhhs3bw5g/craftbukkit-1.8.7-R0.1-SNAPSHOT-latest.jar/file',

            '1.8.9':'https://www.mediafire.com/file/1bll4cwxlilhsdu/craftbukkit-1.8.8-R0.1-SNAPSHOT-latest.jar/file',

            '1.9':'https://www.mediafire.com/file/mw0rdz23aj9r7qg/craftbukkit-1.9-R0.1-SNAPSHOT-latest.jar/file',

            '1.9.2':'https://www.mediafire.com/file/3ez9jng9iynmter/craftbukkit-1.9.2-R0.1-SNAPSHOT-latest.jar/file',

            '1.9.4':'https://www.mediafire.com/file/tflz6u8dppbb6hk/craftbukkit-1.9.4-R0.1-SNAPSHOT-latest.jar/file'
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