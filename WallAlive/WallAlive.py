import ctypes
import os
import platform
import sys
import time
import winreg as register
from sys import executable

user = os.path.expanduser('~')
SPI_SET_WALLPAPER = 20


# Sets the path for image directory to be used.
def path():
    try:
        directory = input('Set the path for image directory: ')
        return user + directory
    except OSError:
        print('Sorry, Directory does not exist')
        exit()


# Sets the time duration for slide show between two images.
def delay():
    try:
        timer = int(input('Enter the delay time in seconds: '))
        if timer == 0:
            print('Sorry but the minimum delay has to be greater than 0')
        else:
            return timer
    except sys.exc_info():
        print(sys.exc_info()[1])
        exit()


# Starts displaying all the images contained within the image directory.
def run(directory, timer):
    try:
        if int(platform.python_version()[0]) >= 3:
            ctypes.windll.user32.SystemParametersInfoW(SPI_SET_WALLPAPER, 0, directory, 0)
            time.sleep(timer)
        elif int(platform.python_version()[0]) < 3:
            ctypes.windll.user32.SystemParametersInfoA(SPI_SET_WALLPAPER, 0, directory, 0)
            time.sleep(timer)
    except sys.exc_info():
        print(sys.exc_info()[1])
        exit()


# Updates the Windows registry with 'Wall Alive' key. This makes sure that the program starts up once the system is
# booted.
def regedit():
    subKey = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
    script = user + 'PycharmProjects/Wall_Alive/Wallpaper.py'
    python = os.path.join(os.path.dirname(executable), 'python.exe')

    hKey = register.OpenKey(register.HKEY_CURRENT_USER, subKey, 0, register.KEY_SET_VALUE)

    register.SetValueEx(hKey, 'Wall Alive', 0, register.REG_SZ, '"{0}" "{1}"'.format(python, script))

    register.CloseKey(hKey)
