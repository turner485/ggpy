# import libarys 
from psd_tools import PSDImage
import json
import csv
from pathlib import Path
import os
import codecs

# create absolute path for linux windows
path = Path.cwd()
absolute = (str(path))

psd_file_path = input('please enter the file path:')

psd_name = input('PSD name:') + '.psd'

if psd_name:
    for file in os.listdir(psd_file_path):
        if psd_name in file:
            psd_name = file
            path_of_psd = Path(psd_file_path).joinpath(file)
            break

""" if input is none finds any psd file in directory """
if not psd_name:
    for file in os.listdir(psd_file_path):
        if '.psb' in file or '.psd' in file:
            psd_name = file
            path_of_psd = Path(psd_file_path).joinpath(file)
            break

if not path_of_psd:
    path_of_psd = Path(psd_file_path).joinpath(psd_file_path)

print('*CAUTION* please use hyphens instead of underscores\nexample == 2019-07-05-AW19-C1-R1-Homepage-UK \n')

image_namespace = input('naming convention:')

# user_directory = absolute + './resources/'
user_directory = absolute 
psd = PSDImage.open(path_of_psd)
os.makedirs(Path(psd_file_path).joinpath('./images/'), exist_ok=True)

artboardDesktop = ""

desktopArtboard, tabletArtboard, mobileArtboard = None, None, None

desktop = '1600'
tablet = '1200'
mobile = '768'

for i in psd:
    if 'DESKTOP'.lower() in i.name.lower() and i.kind == "artboard" and i.visible:
        desktopArtboard = i
        # print(i)
    if '1200'.lower() in i.name.lower() and i.kind == "artboard" and i.visible: 
        tabletArtboard = i
        # print(i)
    if 'MOBILE'.lower() in i.name.lower() and i.kind == "artboard" and i.visible:
        mobileArtboard = i
        # print(i)

def hero_images(p, size):
    hero_namespace = "hero"
    counter = []
    try:
        for layer in reversed(list(p.descendants())):   
            if "HERO".lower() in layer.name.lower() and layer.visible:
                for images in reversed(list(layer)):
                    if images.kind == 'group' and "Image".lower() in images.name.lower():
                        try:
                            counter.append(images)
                            image = images.compose()
                            image.convert('RGB').save(
                                Path(psd_file_path).joinpath('images', f'{image_namespace}-{hero_namespace}-0{str(len(counter))}-{size}.jpg'), quality=85)
                            print(f'exporting hero image {str(len(counter))}...')
                        except AttributeError:
                            pass                      
    except:
        pass
            
def tablet_images(p, size):
    tablet_hero_namespace = "hero-tablet"
    try:
        for layer in reversed(p):
            if "HERO".lower() in layer.name.lower():
                for images in layer:
                    if images.kind == 'group' and "Image".lower() in images.name.lower():
                        try:
                            image = images.compose()
                            image.convert('RGB').save(
                                Path(psd_file_path).joinpath('images', f'{image_namespace}-{tablet_hero_namespace}-{size}.jpg'), quality=85)
                            print('exporting tablet images...')
                        except AttributeError:
                            pass                      
    except:
        pass

def mobile_images(p, size):
    counter = []
    mobile_hero_namespace = "hero-mobile"
    try:
        for layer in reversed(list(p.descendants())):
            if layer.kind == 'group' and "Image".lower() in layer.name.lower():
                try:
                    counter.append(layer)
                    image = layer.compose()
                    image.convert('RGB').save(
                        Path(psd_file_path).joinpath('images', f'{image_namespace}-{mobile_hero_namespace}-0{str(len(counter))}-{size}.jpg'), quality=85)
                    print(f'exporting mobile image {str(len(counter))}...')
                except AttributeError:
                    pass
    except:
        pass

def new_psd(layer):
    file_psd = Path(user_directory).joinpath(layer.filename)
    layer.save(file_psd)
    load = PSDImage.open(file_psd)
    image = load.compose()
    return image

def remove_file(f):
    os.remove(Path(user_directory).joinpath(f))

def baby_right_left(p, size):
    try:
        for layer in reversed(p):
            if layer.name.lower() == "TOP BANNER".lower() and layer.kind == "group":
                for top in layer:
                    if top.name.lower() == "LEFT".lower() and top.kind == "group":
                        for images in top:
                            if images.name.lower() == "Image".lower() and images.kind == "group":
                                try:
                                    images = images.compose()
                                    images.convert('RGB').save(
                                        Path(psd_file_path).joinpath('images', f'{image_namespace}-{size}-left.jpg'), quality=85)
                                    print('exporting left image...')
                                except AttributeError:
                                    pass

                    if top.name.lower() == "RIGHT".lower() and top.kind == "group":
                        for images in top:
                            if images.name.lower() == "Image".lower() and images.kind == "group":
                                try:
                                    images = images.compose()
                                    images.convert('RGB').save(
                                        Path(psd_file_path).joinpath('images', f'{image_namespace}-{size}-right.jpg'), quality=85)
                                    print('exporting right image...')
                                except AttributeError:
                                    pass             
    except:
        pass

def new_in_images(p, size):
    newin_namespace = "newin"
    counter = []
    remove_psd_list = []
    try:
        for layer in reversed(p):
            if 'new in'.lower() in layer.name.lower():
                try:
                    for a in reversed(list(layer.descendants())):
                        if a.kind == 'smartobject':
                            counter.append(layer)  # Add 1 to counter
                            layer = a.smart_object
                            remove_psd_list.append(layer.filename)  # Add temp psd to list
                            image = new_psd(layer)
                            image.convert('RGB').save(
                            Path(psd_file_path).joinpath('images', f'{image_namespace}-{newin_namespace}-0{str(len(counter))}-{size}.jpg'), quality=85)
                            remove_file(layer.filename)
                            print(f'exporting new in {str(len(counter))} image...')  

                except AttributeError:
                    pass
    except:
        pass
                        
def right_left(p, size):
    try:
        for layer in reversed(p):
            if layer.name.lower() == "LEFT".lower() and layer.kind == "group":
                for images in layer:
                    if images.name.lower() == "Image".lower() and images.kind == "group":
                        try:
                            image = images.compose()
                            image.convert('RGB').save(
                                Path(psd_file_path).joinpath('images', f'{image_namespace}-{size}-left.jpg'), quality=85)
                            print('exporting bottom left image...')
                        except AttributeError:
                            pass

            if layer.name.lower() == "RIGHT".lower() and layer.kind == "group":
                for images in layer:
                    if images.name.lower() == "Image".lower() and images.kind == "group":
                        try:
                            image = images.compose()
                            image.convert('RGB').save(
                                Path(psd_file_path).joinpath('images', f'{image_namespace}-{size}-right.jpg'), quality=85)
                            print('exporting bottom right image...')
                        except AttributeError:
                            pass             
    except:
        pass


def bottom_block(p, size):
    try:
        for layer in reversed(list(p.descendants())):
            if 'bottom block'.lower() in layer.name.lower() and layer.kind == "group":
                for images in layer:
                    try:
                        if images.name.lower() == "Image".lower() and images.kind == "group":
                            image = images.compose()
                            image.convert('RGB').save(
                                Path(psd_file_path).joinpath('images', f'{image_namespace}-{size}-bottom-blocks.jpg'), quality=85)
                            print('exporting bottom image...') 
                    except AttributeError:
                        pass
    except:
        pass
hero_images(desktopArtboard, size=desktop)
tablet_images(tabletArtboard, size=tablet)
mobile_images(mobileArtboard, size=mobile)
baby_right_left(desktopArtboard, size=desktop)
new_in_images(desktopArtboard, size=desktop)
right_left(desktopArtboard, size=desktop)
bottom_block(desktopArtboard, size=desktop)

