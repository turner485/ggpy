# import libarys 
from psd_tools import PSDImage
import json
import csv
from pathlib import Path
import os
import codecs


outputDictionary = {'Title': {}, 'Hero': {}, 'Browse_Gifts': {}}

path = Path.cwd()

psd_path = 'C://Users//Ben.Turner//Documents//code//python//ggpy//resources//'
psd_file = 'test.psd'
psd_file_path = psd_path + psd_file
psd = PSDImage.open(psd_file_path)
os.makedirs(Path(psd_path).joinpath('./images/'), exist_ok=True)
desktopArtboard = None

for i in psd:
    if 'DESKTOP'.lower() in i.name.lower() and i.kind == "artboard" and i.visible:
        desktopArtboard = i

        for layer in reversed(desktopArtboard):
            if "TITLE".lower() in layer.name.lower() and layer.visible:
                for title in layer:
                    if title.kind =='type':
                        outputDictionary['Title']['Heading'] = title.name

def hero_images(p):
    hero_namespace = "hero"
    counter = []
    
    for layer in reversed(list(p.descendants())):   
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
                            outputDictionary['Hero']['Headline'] = images[2].name
                            outputDictionary['Hero']['cta'] = images[1].name
                
def get_browse_title():
    try:
        for layer in reversed(list(desktopArtboard)):
            if "BROWSE GIFTS".lower() in layer.name.lower():
                for title in layer:
                    if title.kind == "type" and title.visible:
                        outputDictionary['Browse_Gifts']['Title'] = title.name
    except:
        pass
        
hero_images(desktopArtboard)
get_browse_title()

with codecs.open('./resources/data.json', 'w', encoding="utf-8") as json_file:
    json.dump(outputDictionary, json_file, indent=4, sort_keys=True, ensure_ascii=False)
