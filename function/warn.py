import platform
import subprocess
from threading import Thread
def main(path):
    print(path)

    if 'darwin' in platform.system().casefold() or 'mac' in platform.system().casefold() or 'osx' in platform.system().casefold():
        subprocess.Popen('sh mac.sh', shell=True , cwd=path)

    elif 'linux' in platform.system().casefold():

        subprocess.Popen('sh linux.sh', shell=True , cwd=path)

    elif 'windows' in platform.system().casefold():

        subprocess.Popen('windows.cmd', shell=True , cwd=path)

def warning_send(path):
    target = Thread(target=lambda:main(path= path))
    target.start()