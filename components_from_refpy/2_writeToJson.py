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

psd_name = input('PSD name:')

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

image_url_csv = absolute + '/resources/Media_gb_1.csv'
psd = PSDImage.open(path_of_psd)



outputDictionary = {'TopTitle': {},'Hero': {}, 'NewInBlock': {}, 'LeftBlock': {}, 'RightBlock': {}}

for i in reversed(list(psd.descendants())):
    if 'DESKTOP'.lower() in i.name.lower() and i.kind == "artboard" and i.visible:
        desktopArtboard = i

# --- Start of HERO block --- #
def get_hero_content():
    try:
        for layer in reversed(desktopArtboard):
            if "HERO".lower() in layer.name.lower() and layer.visible:
                outputDictionary['Hero']['Type'] = layer.name
                try:
                    for copy in layer:
                        if "Copy".lower() in copy.name.lower():
                            for text in copy:
                                if text.kind == 'type':       
                                    outputDictionary['Hero']['Text_One'] = copy[3].text
                                    outputDictionary['Hero']['Text_Two'] = copy[2].text       
                                if text.kind == 'group' and "cta".lower() in text.name.lower():
                                    for cta in text:  
                                        if cta.kind == "type":
                                            outputDictionary['Hero']['Button_Text'] = cta.text
                except AttributeError:
                    pass                              
        for image_url in open(image_url_csv):
            try:
                if 'hero-01' in image_url:
                    outputDictionary['Hero']['Image_One'] = image_url.strip()
                if 'hero-02' in image_url:
                    outputDictionary['Hero']['Image_Two'] = image_url.strip()
                if 'tablet' in image_url:
                    outputDictionary['Hero']['Tablet'] = image_url.strip()
                if 'mobile' in image_url:
                    outputDictionary['Hero']['Mobile'] = image_url.strip()
            except AttributeError:
                pass
    except:
        pass
#  --- End of HERO block --- #
#  --- Start of NEW IN block --- #
def get_newin_block_content(p):
    block = 'block '.lower() + str(p)
    outputDictionary['NewInBlock'][block] = {}
    try:
        for layer in reversed(desktopArtboard):
            if "NEW IN".lower() in layer.name.lower():
                try:
                    for copy in layer:
                        if block in copy.name.lower():
                            for cta in copy:
                                if cta.kind == 'type':
                                    outputDictionary['NewInBlock'][block]['Button_Text'] = cta.text
                except TypeError:
                    pass
                try:
                    for copy in layer:
                        if "Copy".lower() in copy.name.lower():
                            for title in copy:
                                if title.kind == 'type':
                                    outputDictionary['NewInBlock']['Title'] = title.text   
                except TypeError:
                    pass

        image_counter = 'newin-0' + str(p)
        for image_url in open(image_url_csv):
            try:
                if image_counter in image_url:
                    outputDictionary['NewInBlock'][block]['ImageSrc'] = image_url.strip()
            except AttributeError:
                pass
    except:
        pass
#  --- End of NEW IN block --- #
#  --- End of LEFT BOTTOM BLOCK block --- #
                                
def get_left_bottom_content():
    try:
        for layer in reversed(desktopArtboard):
            if layer.name.lower() == "LEFT".lower() and layer.kind == "group":
                try:
                    for copy in layer:
                        if "Copy".lower() in copy.name.lower():
                            for text in copy:
                                if text.kind == 'type':
                                    outputDictionary['LeftBlock']['Text_One'] = copy[1].text
                                    outputDictionary['LeftBlock']['Text_Two'] = copy[0].text
                except TypeError:
                    pass
    
        for image_url in open(image_url_csv):          
                try:                 
                    if 'left' in image_url:
                        outputDictionary['LeftBlock']["ImageSrc"] = image_url.strip()
                except AttributeError:
                    pass
    except:
        pass
#  --- End of block --- #
#  --- End of RIGHT BOTTOM BLOCK block --- #  
def get_right_bottom_content():
    try:
        for layer in reversed(desktopArtboard):
            if layer.name.lower() == "RIGHT".lower() and layer.kind == "group":
                for copy in layer:
                    try:
                        if "Copy".lower() in copy.name.lower():
                            for text in copy:
                                if text.kind == 'type':
                                    outputDictionary['RightBlock']['Text_One'] = copy[1].text
                                    outputDictionary['RightBlock']['Text_Two'] = copy[0].text              
                    except TypeError:
                        pass

        for image_url in open(image_url_csv):  
            try:
                if 'right' in image_url:
                    outputDictionary['RightBlock']["ImageSrc"] = image_url.strip()
            except AttributeError:
                pass
    except:
        pass
#  --- End of block --- #
#  --- End of BABY TILE --- #
def getBabyTitle():
    try:
        for layer in reversed(desktopArtboard):
            if "TITLE".lower() in layer.name.lower() and layer.kind == "group":
                outputDictionary['TopTitle']['Title'] = layer[1].text
                outputDictionary['TopTitle']['Sub'] = layer[2].text           
    except:
        pass
#  --- End of block --- #
#  --- End of BABY BLOCKS --- #
def getBabyBlocks():
    try:
        for layer in reversed(desktopArtboard):
            if layer.name.lower() == "TOP BANNER".lower() and layer.kind == "group":
                for copy in layer:
                    try:
                        if copy.name.lower() == "LEFT".lower() and copy.kind == "group":
                            for type_layer in copy:
                                if type_layer.name.lower() == "Copy".lower() and type_layer.kind == "group":
                                    for left_text in type_layer:
                                        if left_text.kind == "type":
                                            outputDictionary['LeftBlock']['Button_Text'] = left_text.text
                    except TypeError:
                        pass
                    try:                            
                        if copy.name.lower() == "RIGHT".lower() and copy.kind == "group":
                                for type_layer in copy:
                                    if type_layer.name.lower() == "Copy".lower() and type_layer.kind == "group":
                                        for right_text in type_layer:
                                            if right_text.kind == "type":
                                                outputDictionary['RightBlock']['Button_Text'] = right_text.text
                    except TypeError:
                        pass
    except AttributeError:
        pass

print('Populating Json...')

#  --- End of block --- #

# Call functions
get_hero_content()
get_newin_block_content(1)
get_newin_block_content(2)
get_newin_block_content(3)
get_newin_block_content(4)
get_left_bottom_content()
get_right_bottom_content()
getBabyTitle()
getBabyBlocks()

with codecs.open(absolute + '/resources/data.json', 'w', encoding="utf-8") as outfile:
    json.dump(outputDictionary, outfile, indent=4, sort_keys=True, ensure_ascii=False)
