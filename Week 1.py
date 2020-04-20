#!/usr/bin/python3

from PIL import Image
import os, sys

path = "./images/"
new_path='/opt/icons/'
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if item == '.DS_Store':
            continue
        elif os.path.isfile(path+item):
            im = Image.open(path+item)
            im.resize((128,128)).convert('RGB').save(new_path+item, 'JPEG')
            im2 = Image.open(new_path + item)
            im2.rotate(90).convert('RGB').save(new_path + item, 'JPEG')
resize()


