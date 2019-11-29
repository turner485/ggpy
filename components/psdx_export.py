# import libarys 
from psd_tools import PSDImage
import json
import csv
from pathlib import Path
import os
import codecs
# end of import
outputDictionary = {'Headline': {}, 'Hero': {}, 'Browse_Gifts': {}, 'Popular_Categories': {}, 'Gifts_Under': {}, 'Inspiration': {}, 'Blog': {}}
path = Path.cwd()
psd_path = 'C://Users//Ben.Turner//Documents//code//python//ggpy//resources//'
psd_file = 'test.psd'
psd_file_path = psd_path + psd_file
psd = PSDImage.open(psd_file_path)
os.makedirs(Path(psd_path).joinpath('./images/'), exist_ok=True)
desktopArtboard = None
###
for i in psd:
    if 'DESKTOP'.lower() in i.name.lower() and i.kind == "artboard" and i.visible:
        desktopArtboard = i
###
def get_title():
        for layer in reversed(desktopArtboard):
            if "TITLE".lower() in layer.name.lower() and layer.visible:
                for title in layer:
                    if title.kind =='type':
                        outputDictionary['Headline']['Heading'] = title.name.lower().strip()
### 
def get_hero_images(artboard):
    hero_namespace = "hero"
    counter = []
    for layer in reversed(list(artboard.descendants())):   
        if "TOP BANNER".lower() in layer.name.lower() and layer.visible:
            for images in reversed(list(layer)):
                if images.kind == 'group' and "Image".lower() in images.name.lower():
                    counter.append(images)
                    image = images.compose()
                    image.convert('RGB').save(
                    Path(psd_path).joinpath('images', f'_{hero_namespace}_0{str(len(counter))}_v1.jpg'), quality=85)
                    print(f'exporting hero image {str(len(counter))}...')
                if images.kind == 'group' and "Copy".lower() in images.name.lower():
                    for copy in reversed(list(images)):
                        if copy.kind =='type':
                            outputDictionary['Hero']['Headline'] = images[2].name.lower().strip()
                            outputDictionary['Hero']['Button_Text'] = images[1].name.lower().replace(' >', '').strip()
###
def get_browse_gifts_data(artboard):
    browse_namespace = "browse-gifts"
    counter = []
    count = 0
    for layer in reversed(desktopArtboard):
        if 'BROWSE GIFTS'.lower() in layer.name.lower():
            for title in reversed(layer):
                if title.kind == "type" and title.visible:
                    outputDictionary['Browse_Gifts']['Headline'] = title.name.lower().strip()
            for images in reversed(list(layer.descendants())):
                if images.kind == 'group' and "Image".lower() in images.name.lower():
                    try:
                        counter.append(layer)
                        image = images.compose()
                        image.convert('RGB').save(
                        Path(psd_path).joinpath('images', f'{browse_namespace}_0{str(len(counter))}_v1.jpg'), quality=85)
                        print(f'exporting browse gift image {str(len(counter))}...')  
                    except AttributeError:
                        pass
            for copy in reversed(layer):
                if 'block' in copy.name.lower() and copy.visible:
                    for cta in copy:
                        if cta.kind == 'type':
                            count += 1
                            block = 'block '.lower() + str(count)
                            outputDictionary['Browse_Gifts'][block] = {}
                            outputDictionary['Browse_Gifts'][block]['Button_Text'] = cta.text.lower().replace(' >', '').strip()
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
                            Path(psd_path).joinpath('images', f'{popular_namespace}_left_v1.jpg'), quality=85)
                            print('exporting popular categories left image...')
                        if left_block.kind =='type':
                            outputDictionary['Popular_Categories']['Left']['Button_Text'] = left_block.text.lower().replace(' >', '').strip()
                if blocks.kind == 'group' and 'RIGHT'.lower() in blocks.name.lower():
                    for right_block in blocks:
                        if right_block.kind =='group' and "Image".lower() in right_block.name.lower():
                            image = right_block.compose()
                            image.convert('RGB').save(
                            Path(psd_path).joinpath('images', f'{popular_namespace}_right_v1.jpg'), quality=85)
                            print('exporting popular categories right image...')  
                        if right_block.kind =='type':
                            outputDictionary['Popular_Categories']['Right']['Button_Text'] = right_block.text.lower().replace(' >', '').strip()
###                        
def get_gifts_under_data(artboard):
    browse_namespace = "gifts-under"
    counter = []
    count = 0
    for layer in reversed(desktopArtboard):
        if 'GIFTS FOR UNDER'.lower() in layer.name.lower():
            for copy in layer:
                if 'COPY'.lower() in copy.name.lower():
                    for title in copy:
                        if title.kind == 'type':
                            outputDictionary['Gifts_Under']['Headline'] = title.text.lower().strip().replace('£', '&pound;').strip()
                        if title.kind == 'group' and title.visible:
                            for cta in title:
                                if cta.kind == 'type':
                                    outputDictionary['Gifts_Under']['Button_Text'] = cta.text.lower().replace(' >', '').strip()
            for copy in layer:
                if 'block' in copy.name.lower() and copy.visible:
                    for cta in copy:
                        if cta.kind == 'type':
                            count += 1
                            block = 'block '.lower() + str(count)
                            outputDictionary['Gifts_Under'][block] = {}
                            outputDictionary['Gifts_Under'][block]['Button_Text'] = cta.text.lower().replace('\r', '<br>').strip()
            for images in reversed(list(layer.descendants())):
                if images.kind == 'group' and "Image".lower() in images.name.lower():
                    counter.append(layer)
                    image = images.compose()
                    image.convert('RGB').save(
                    Path(psd_path).joinpath('images', f'{browse_namespace}_0{str(len(counter))}_v1.jpg'), quality=85)
                    print(f'exporting gift for under £40 image {str(len(counter))}...')  
###                                   
def get_inspiration_data(artboard):
    browse_namespace = "inspiration"
    counter = []
    count = 0
    for layer in reversed(desktopArtboard):
        if 'INSPIRED'.lower() in layer.name.lower():
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
            for images in reversed(list(layer.descendants())):
                if images.kind == 'group' and "Image".lower() in images.name.lower():
                    counter.append(layer)
                    image = images.compose()
                    image.convert('RGB').save(
                    Path(psd_path).joinpath('images', f'{browse_namespace}_0{str(len(counter))}_v1.jpg'), quality=85)
                    print(f'exporting inspired image {str(len(counter))}...')  
###                                           
def get_blog_data(artboard):
    browse_namespace = "blog"
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
                if 'block' in copy.name.lower() and copy.visible:
                    for cta in copy:
                        if "COPY".lower() in cta.name.lower():
                            for items in cta:
                                if items.kind =='type':
                                    count +=1
                                    block = 'block '.lower() + str(count)
                                    outputDictionary['Blog'][block] = {}
                                    outputDictionary['Blog'][block]['text'] = cta[0].text.lower().strip()
                                    outputDictionary['Blog'][block]['Button_Text'] = cta[1].text.lower().strip()
                       
# ###                        
# ### Run functions                            
# get_title()
# get_hero_images(desktopArtboard)
# get_browse_gifts_data(desktopArtboard)
# # get_popular_cats_images(desktopArtboard)
# get_gifts_under_data(desktopArtboard)
# get_inspiration_data(desktopArtboard)
get_blog_data(desktopArtboard)

### export json
with codecs.open('./resources/data.json', 'w', encoding="utf-8") as json_file:
    json.dump(outputDictionary, json_file, indent=4, sort_keys=True, ensure_ascii=False)
