#!usr/bin/python
import os
import sys
import time


class Wallpaper:
    # Sets the path for image directory to be used.
    def path(self):
        try:
            directory = raw_input('Enter the file path for wallpaper directory:')
            return directory
        except OSError:
            print 'Sorry, Directory does not exist'
            exit()

    # Sets the time duration for slide show between two images.
    def timer(self):
        try:
            timer = int(raw_input('Enter the delay time in seconds:'))
            if timer == 0:
                print 'Sorry but the minimum delay has to be greater than 0'
            else:
                return timer
        except sys.exc_info():
            print sys.exc_info()[1]
            exit()

    # Determines whether gsettings exist in linux distribution or not. Replace the path 'gsetttings' with the one where your gsettings file is stored.
    def gsettings(self):
        gsettings = os.system('sh /home/siddharth/Desktop/gsettings')
        if gsettings != '':
            return None
        else:
            print 'Sorry but gsettings were not found in your computer'
            exit()

    # Starts displaying all the images contained within the image directory.
    def run(self, directory, picture, timer):
        path = 'gsettings set org.gnome.desktop.background picture-uri file://' + directory + picture
        os.system(path)
        time.sleep(timer)
