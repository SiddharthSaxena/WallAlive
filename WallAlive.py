import glob
import src

formats = ['*.jpg', '*.png', '*.bmp', '*.gif', '*.tif', '*.tiff']
wall = src.Wallpaper.Wallpaper()

directory = wall.path()
timer = wall.delay()

# For the images to be displayed indefinitely, the configuration has to be run in an infinite loop.
while 1:
    for format in formats:
        pictureDirectory = glob.glob(directory + format)
        for picture in pictureDirectory:
            wall.run(picture, timer)

# Find a way as to how to run the script in background.
# Use platform configuration, and convert images to bmp for windows 8 and lower. A program was available on the
# internet.
# Add the regedit.exe program from the Downloads folder and add it to the setup.py
