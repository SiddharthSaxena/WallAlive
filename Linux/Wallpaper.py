#!usr/bin/python
import os
import Wall

wall = Wall.Wallpaper()

directory = wall.path()
timer = wall.timer()
wall.gsettings()

# For the images to be displayed indefinitely, the configuration has to be run in an infinite loop.
while 1:
    pictureDirectory = os.listdir(directory)
    for picture in pictureDirectory:
        wall.run(directory, picture, timer)
