import os
import shutil
import ctypes
from ctypes import wintypes
from zipfile import ZipFile
import sys
import ntpath
try:
    import winreg
except ImportError:
    import _winreg as winreg

user32 = ctypes.WinDLL('user32', use_last_error=True)
gdi32 = ctypes.WinDLL('gdi32', use_last_error=True)

FONTS_REG_PATH = r'Software\Microsoft\Windows NT\CurrentVersion\Fonts'

HWND_BROADCAST = 0xFFFF
SMTO_ABORTIFHUNG = 0x0002
WM_FONTCHANGE = 0x001D
GFRI_DESCRIPTION = 1
GFRI_ISTRUETYPE = 3

def install_font(src_path):
    with ZipFile(f'{src_path}/fonts.zip' , 'r') as zip:
        zip.printdir()
        zip.extractall(f'{src_path}')
        print('Done!')

    # copy the font to the Windows Fonts folder
    dst_path = os.path.join(os.environ['SystemRoot'], 'Fonts',
                            os.path.basename(src_path))
    shutil.copy(src_path, dst_path)
    # load the font in the current session
    if not gdi32.AddFontResourceW(dst_path):
        os.remove(dst_path)
        raise WindowsError('AddFontResource failed to load "%s"' % src_path)
    # notify running programs
    user32.SendMessageTimeoutW(HWND_BROADCAST, WM_FONTCHANGE, 0, 0,
                               SMTO_ABORTIFHUNG, 1000, None)
    # store the fontname/filename in the registry
    filename = os.path.basename(dst_path)
    fontname = os.path.splitext(filename)[0]
    # try to get the font's real name
    cb = wintypes.DWORD()
    if gdi32.GetFontResourceInfoW(filename, ctypes.byref(cb), None,
                                  GFRI_DESCRIPTION):
        buf = (ctypes.c_wchar * cb.value)()
        if gdi32.GetFontResourceInfoW(filename, ctypes.byref(cb), buf,
                                      GFRI_DESCRIPTION):
            fontname = buf.value
    is_truetype = wintypes.BOOL()
    cb.value = ctypes.sizeof(is_truetype)
    gdi32.GetFontResourceInfoW(filename, ctypes.byref(cb),
                               ctypes.byref(is_truetype), GFRI_ISTRUETYPE)
    if is_truetype:
        fontname += ' (TrueType)'
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, FONTS_REG_PATH, 0,
                        winreg.KEY_SET_VALUE) as key:
        winreg.SetValueEx(key, fontname, 0, winreg.REG_SZ, filename)