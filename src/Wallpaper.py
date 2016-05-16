import ctypes
import os
import platform
import sys
import time

user = os.path.expanduser('~')
SPI_SET_WALLPAPER = 20


class Wallpaper:
    # Sets the path for image directory to be used.
    def path(self):
        try:
            directory = input('Set the path for image directory: ')
            return user + directory
        except OSError:
            print('Sorry, Directory does not exist')
            exit()

    # Sets the time duration for slide show between two images.
    def delay(self):
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
    def run(self, directory, timer):
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
