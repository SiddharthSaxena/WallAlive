import glob
import os
import WallAlive

user = os.path.expanduser('~')
formats = ['*.jpg', '*.png', '*.bmp', '*.gif', '*.tif', '*.tiff']

wall = WallAlive.WallAlive
temp = os.path.join(user + '\\WallAlive\\WallAlive\\WallAlive.py')
if not os.path.exists(temp):
    wall.install()
wall.regedit()
directory = wall.path()
timer = wall.delay()

# For the images to be displayed indefinitely, the configuration has to be run in an infinite loop.
while 1:
    for format in formats:
        pictureDirectory = glob.glob(directory + format)
        for picture in pictureDirectory:
            wall.run(picture, timer)
