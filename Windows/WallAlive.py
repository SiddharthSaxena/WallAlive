import ctypes
import os
import platform
import sys
import time
import winreg as register
from sys import executable
from PIL import ImageFile
from shutil import copyfile

user = os.path.expanduser('~')
SPI_SET_WALLPAPER = 20


# Sets the path for image directory to be used.
def path():
    try:
        directory = input('Set the path for image directory: ' + user + '\\')
        return user + '\\' + directory + '\\'
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
    except ValueError:
        print('Please enter a valid number')
        exit()


# Starts displaying all the images contained within the image directory.
def run(directory, timer):
    try:
        if int(platform.python_version()[0]) >= 3:
            ctypes.windll.user32.SystemParametersInfoW(SPI_SET_WALLPAPER, 0, directory, 3)
            time.sleep(timer)
        elif int(platform.python_version()[0]) < 3:
            ctypes.windll.user32.SystemParametersInfoA(SPI_SET_WALLPAPER, 0, directory, 3)
            time.sleep(timer)
    except sys.exc_info():
        print(sys.exc_info()[1])
        exit()


# Updates the Windows registry with 'Wall Alive' key. This makes sure that the program starts up once the system is
# booted.
def regedit():
    subKey = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
    script = user + '\\WallAlive\\Wallpaper.py'
    python = os.path.join(os.path.dirname(executable), 'python.exe')
    hKey = register.OpenKey(register.HKEY_CURRENT_USER, subKey, 0, register.KEY_SET_VALUE)
    register.SetValueEx(hKey, 'WallAlive', 0, register.REG_SZ, '"{0}" "{1}"'.format(python, script))
    register.CloseKey(hKey)


# Installs WallAlive module.
def install():
    temp = os.path.join(user + '\\WallAlive\\WallAlive')
    if not os.path.exists(temp):
        os.makedirs(temp)
    currentDirectory = os.getcwd()
    currentDirectoryList = currentDirectory.split('\\')
    currentDirectoryList.append('WallAlive')
    nextDirectory = '\\'.join(currentDirectoryList)

    copyfile(nextDirectory + '\\WallAlive.py', user + '\\WallAlive\\WallAlive\\WallAlive.py')
    copyfile(nextDirectory + '\\__init__.py', user + '\\WallAlive\\WallAlive\\__init__.py')
    copyfile(currentDirectory + '\\Wallpaper.py', user + '\\WallAlive\\Wallpaper.py')
