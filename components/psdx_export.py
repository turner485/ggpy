# import libarys 
from psd_tools import PSDImage
import json
import csv
from pathlib import Path
import os
import codecs
###
# create absolute path for linux windows
path = Path.cwd()
# COMMENT BELOW IF YOU ARE NOT INTENDING OF USING BASH SCRIPT
# absolute = (str(path)) + '../..' 
# UNCOMMENT IF NOT USING BASH SCRIPT
### promt file location
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
print('example == 2020_20_01_SS20_C1_GG \n')
image_namespace = input('naming convention:')
###
###
user_directory = absolute 
psd = PSDImage.open(path_of_psd)
os.makedirs(Path(psd_file_path).joinpath('./images/'), exist_ok=True)
outputDictionary = {'Hero': {}, 'Browse_Gifts': {}, 'Popular_Categories': {}, 'Gifts_Under_20': {}, 'Gifts_Under_40': {}, 'Inspiration': {}, 'Blog': {}}
desktopArtboard, tabletArtboard, mobileArtboard = None, None, None
###
for i in psd:
    if 'DESKTOP'.lower() in i.name.lower() and i.kind == "artboard" and i.visible:
        desktopArtboard = i
    if '1200'.lower() in i.name.lower() and i.kind == "artboard" and i.visible: 
        tabletArtboard = i
    if 'MOBILE'.lower() in i.name.lower() and i.kind == "artboard" and i.visible:
        mobileArtboard = i     
###  
### 
def get_hero_images(artboard):
    hero_namespace = "hero"
    counter = []
    for layer in reversed(desktopArtboard):
        if "HERO".lower() in layer.name.lower() and layer.visible:
            outputDictionary['Hero']['Type'] = layer.name.upper()
        if "TITLE".lower() in layer.name.lower() and layer.visible:
            for title in layer:
                if title.kind =='type':
                    outputDictionary['Hero']['Main_Title'] = title.name.lower().strip()
    for layer in reversed(list(artboard.descendants())):
        if "HERO".lower() in layer.name.lower() and layer.visible:
            for images in reversed(list(layer)):
                if images.kind == 'group' and "Image".lower() in images.name.lower():
                    counter.append(images)
                    image = images.compose()
                    image.convert('RGB').save(
                    Path(psd_file_path).joinpath('images', f'{image_namespace}_{hero_namespace}_0{str(len(counter))}_v1.jpg'), quality=85)
                    print(f'exporting hero image {str(len(counter))}...')
                if images.kind == 'group' and "Copy".lower() in images.name.lower():
                    for copy in reversed(list(images)):
                        if copy.kind =='type':
                            outputDictionary['Hero']['Headline'] = images[2].name.lower().strip()
                            outputDictionary['Hero']['Button_Text'] = images[1].name.lower().replace(' >', '').strip()
###
###
def get_tablet_images(artboard):
    tablet_image_namespace = "tablet"
    counter = []
    try:
        for layer in reversed(list(artboard.descendants())):
            if layer.kind == 'group' and "Image".lower() in layer.name.lower():
                try: 
                    counter.append(layer)
                    image = layer.compose()
                    image.convert('RGB').save(
                    Path(psd_file_path).joinpath('images', f'{image_namespace}_{tablet_image_namespace}_0{str(len(counter))}_v1.jpg'), quality=85)
                    print(f'exporting tablet image {str(len(counter))}...')
                except AttributeError:
                    pass
    except:
        pass
###
###
def get_mobile_images(artboard):
    mobile_image_namespace = "mobile"
    counter = []
    try:
        for layer in reversed(list(artboard.descendants())):
            if layer.kind == 'group' and "Image".lower() in layer.name.lower():
                try:
                    counter.append(layer)
                    image = layer.compose()
                    image.convert('RGB').save(
                    Path(psd_file_path).joinpath('images', f'{image_namespace}_{mobile_image_namespace}_0{str(len(counter))}_v1.jpg'), quality=85)
                    print(f'exporting mobile image {str(len(counter))}...')
                except AttributeError:
                    pass
    except:
        pass
###
###
def get_gifts_data(artboard):
    _namespace = "browse-gifts"
    counter = []
    count = 0
    for layer in reversed(desktopArtboard):
        if 'BROWSE GIFTS'.lower() in layer.name.lower():
            for title in reversed(layer):
                if title.kind == "type" and title.visible:
                    outputDictionary['Browse_Gifts']['Headline'] = title.name.lower().strip()
            for copy in reversed(layer):
                if 'block' in copy.name.lower() and copy:
                    for cta in copy:
                        if cta.kind == 'type':
                            count += 1
                            block = 'block '.lower() + str(count)
                            outputDictionary['Browse_Gifts'][block] = {}
                            outputDictionary['Browse_Gifts'][block]['Button_Text'] = cta.text.lower().replace(' >', '').strip()
                    outputDictionary['Browse_Gifts']['count'] = count
            for images in reversed(list(layer.descendants())):
                if images.kind == 'group' and "Image".lower() in images.name.lower():
                    for smart_obj in images:
                        if smart_obj.kind == "smartobject":         
                            try:
                                counter.append(layer)
                                image = smart_obj.compose()
                                image.convert('RGB').save(
                                Path(psd_file_path).joinpath('images', f'{image_namespace}_{_namespace}_0{str(len(counter))}_v1.jpg'), quality=85)
                                print(f'exporting browse gift image {str(len(counter))}...')  
                            except AttributeError:
                                pass
###
###               
def get_popular_cats_images(artboard):
    popular_namespace = "popular-categories"
    outputDictionary['Popular_Categories']['Left'] = {}
    outputDictionary['Popular_Categories']['Right'] = {}
    for layer in reversed(desktopArtboard):
        if 'POPULAR CATEGORIES'.lower() in layer.name.lower():
            for blocks in layer:
                if blocks.kind == 'group' and 'LEFT'.lower() in blocks.name.lower():
                    for left_block in blocks:
                        if left_block.kind =='group' and "Image".lower() in left_block.name.lower():
                            image = left_block.compose()
                            image.convert('RGB').save(
                            Path(psd_file_path).joinpath('images', f'{image_namespace}_{popular_namespace}_left_v1.jpg'), quality=85)
                            print('exporting popular categories left image...')
                        if left_block.kind =='type':
                            outputDictionary['Popular_Categories']['Left']['Button_Text'] = left_block.text.lower().replace(' >', '').strip()
                if blocks.kind == 'group' and 'RIGHT'.lower() in blocks.name.lower():
                    for right_block in blocks:
                        if right_block.kind =='group' and "Image".lower() in right_block.name.lower():
                            image = right_block.compose()
                            image.convert('RGB').save(
                            Path(psd_file_path).joinpath('images', f'{image_namespace}_{popular_namespace}_right_v1.jpg'), quality=85)
                            print('exporting popular categories right image...')  
                        if right_block.kind =='type':
                            outputDictionary['Popular_Categories']['Right']['Button_Text'] = right_block.text.lower().replace(' >', '').strip()
### 
###                       
def get_gifts_under_twenty_data(artboard):
    _namespace = "gifts-under-20"
    counter = []
    count = 0
    for layer in reversed(desktopArtboard):
        if 'GIFTS UNDER 20'.lower() in layer.name.lower():
            for copy in layer:
                if 'COPY'.lower() in copy.name.lower():
                    for title in copy:
                        if title.kind == 'type':
                            outputDictionary['Gifts_Under_20']['Headline'] = title.text.lower().strip().replace('£', '&pound;').strip()
                        if title.kind == 'group' and title.visible:
                            for cta in title:
                                if cta.kind == 'type':
                                    outputDictionary['Gifts_Under_20']['Button_Text'] = cta.text.lower().replace(' >', '').strip()                
            for copy in layer:
                if 'block' in copy.name.lower() and copy.kind == 'group':
                    for cta in copy:
                        if cta.kind == 'type':
                            count += 1
                            block = 'block '.lower() + str(count)
                            outputDictionary['Gifts_Under_20'][block] = {}
                            block_text = outputDictionary['Gifts_Under_20'][block]['Button_Text'] = cta.text.lower().replace('\r', '<br>').strip()
                            block_text =  outputDictionary['Gifts_Under_20'][block]['Button_Text'] = block_text.replace('£', '&pound')
                    outputDictionary['Gifts_Under_20']['count'] = count
            for images in reversed(list(layer.descendants())):
                if images.kind == 'group' and "Image".lower() in images.name.lower():
                    for smart_obj in images:
                        if smart_obj.kind == "smartobject":         
                            try:
                                counter.append(layer)
                                image = smart_obj.compose()
                                image.convert('RGB').save(
                                Path(psd_file_path).joinpath('images', f'{image_namespace}_{_namespace}_0{str(len(counter))}_v1.jpg'), quality=85)
                                print(f'exporting gifts under 20 image {str(len(counter))}...')  
                            except AttributeError:
                                pass
### 
###                                  
def get_gifts_under_forty_data(artboard):
    _namespace = "gifts-under-40"
    counter = []
    count = 0
    for layer in reversed(desktopArtboard):
        if 'GIFTS UNDER 40'.lower() in layer.name.lower():
            for copy in layer:
                if 'COPY'.lower() in copy.name.lower():
                    for title in copy:
                        if title.kind == 'type':
                            outputDictionary['Gifts_Under_40']['Headline'] = title.text.lower().strip().replace('£', '&pound;').strip()
                        if title.kind == 'group' and title.visible:
                            for cta in title:
                                if cta.kind == 'type':
                                    outputDictionary['Gifts_Under_40']['Button_Text'] = cta.text.lower().replace(' >', '').strip()                
            for copy in layer:
                if 'block' in copy.name.lower() and copy.kind == 'group':
                    for cta in copy:
                        if cta.kind == 'type':
                            count += 1
                            block = 'block '.lower() + str(count)
                            outputDictionary['Gifts_Under_40'][block] = {}
                            block_text = outputDictionary['Gifts_Under_40'][block]['Button_Text'] = cta.text.lower().replace('\r', '<br>').strip()
                            block_text =  outputDictionary['Gifts_Under_40'][block]['Button_Text'] = block_text.replace('£', '&pound')
                    outputDictionary['Gifts_Under_40']['count'] = count
            for images in reversed(list(layer.descendants())):
                if images.kind == 'group' and "Image".lower() in images.name.lower():
                    for smart_obj in images:
                        if smart_obj.kind == "smartobject":         
                            try:
                                counter.append(layer)
                                image = smart_obj.compose()
                                image.convert('RGB').save(
                                Path(psd_file_path).joinpath('images', f'{image_namespace}_{_namespace}_0{str(len(counter))}_v1.jpg'), quality=85)
                                print(f'exporting gifts under 40 image {str(len(counter))}...')  
                            except AttributeError:
                                pass
###
###                                   
def get_inspiration_data(artboard):
    _namespace = "inspiration"
    counter = []
    count = 0
    for layer in reversed(desktopArtboard):
        if 'INSPIRATION'.lower() in layer.name.lower():
            for copy in layer:
                if 'COPY'.lower() in copy.name.lower():
                    for title in copy:
                        if title.kind == 'type':
                            outputDictionary['Inspiration']['Headline'] = title.text.lower().strip()
            for copy in reversed(layer):
                if 'block' in copy.name.lower() and copy.visible:
                    for cta in copy:
                        if cta.kind == 'type':
                            count += 1
                            block = 'block '.lower() + str(count)
                            outputDictionary['Inspiration'][block] = {}
                            outputDictionary['Inspiration'][block]['Button_Text'] = cta.text.lower().replace(' >', '').strip()
                    outputDictionary['Inspiration']['count'] = count
            for images in reversed(list(layer.descendants())):
                if images.kind == 'group' and "Image".lower() in images.name.lower():
                    for smart_obj in images:
                        if smart_obj.kind == "smartobject":         
                            try:
                                counter.append(layer)
                                image = smart_obj.compose()
                                image.convert('RGB').save(
                                Path(psd_file_path).joinpath('images', f'{image_namespace}_{_namespace}_0{str(len(counter))}_v1.jpg'), quality=85)
                                print(f'exporting inspo gift image {str(len(counter))}...')  
                            except AttributeError:
                                pass
###  
###                                         
def get_blog_data(artboard):
    _namespace = "blog"
    counter = []
    count = 0
    for layer in reversed(desktopArtboard):
        if 'BLOG'.lower() in layer.name.lower():
            for headline in layer:
                if 'COPY'.lower() in headline.name.lower():
                    for title in headline:
                        if title.kind == 'type':
                            outputDictionary['Blog']['Headline'] = title.text.lower().strip()
            for copy in reversed(layer):
                if 'block' in copy.name.lower() and copy.kind == "group":
                    count +=1
                    for cta in copy:                 
                        if "COPY".lower() in cta.name.lower():
                            for items in cta:
                                if items.kind =='type':
                                    block = 'block '.lower() + str(count)
                                    outputDictionary['Blog'][block] = {}
                                    outputDictionary['Blog'][block]['text'] = cta[0].text.lower().strip()
                                    outputDictionary['Blog'][block]['Button_Text'] = cta[1].text.lower().strip()
            outputDictionary['Blog']['count'] = count
            for images in reversed(list(layer.descendants())):
                if images.kind == 'group' and "Image".lower() in images.name.lower():
                    for smart_obj in images:
                        if smart_obj.kind == "smartobject":         
                            try:
                                counter.append(layer)
                                image = smart_obj.compose()
                                image.convert('RGB').save(
                                Path(psd_file_path).joinpath('images', f'{image_namespace}_{_namespace}_0{str(len(counter))}_v1.jpg'), quality=85)
                                print(f'exporting blog image {str(len(counter))}...')  
                            except AttributeError:
                                pass
###
### Run functions
get_hero_images(desktopArtboard)
get_tablet_images(tabletArtboard)
get_mobile_images(mobileArtboard)
get_gifts_data(desktopArtboard)
get_popular_cats_images(desktopArtboard)
get_gifts_under_twenty_data(desktopArtboard)
get_gifts_under_forty_data(desktopArtboard)
get_inspiration_data(desktopArtboard)
get_blog_data(desktopArtboard)
### export json
with codecs.open('./resources/data.json', 'w', encoding="utf-8") as json_file:
    json.dump(outputDictionary, json_file, indent=4, sort_keys=True, ensure_ascii=False)
print('Populating data.json...')