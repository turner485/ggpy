# import libaries 
from pathlib import Path
import codecs
import csv
import json
import os
import xlrd

image_url_csv = 'Media_gb_1.csv'
link_xlsx = 'GG_Links.xlsx'
_path = 'C://Users//Ben.Turner//Documents//code//python//ggpy//resources//'

csv_file_path = _path + image_url_csv
xlsx_file_path = _path + link_xlsx

with open('./resources/data.json') as outfile:
    outputDictionary = json.load(outfile)

def get_hero_content():
     for image_url in open(csv_file_path):
        if 'hero-01' in image_url:
            outputDictionary['Hero']['Image_One'] = image_url.strip()
        if 'hero-02' in image_url:
            outputDictionary['Hero']['Image_Two'] = image_url.strip()
        if 'hero-03' in image_url:
            outputDictionary['Hero']['Image_Three'] = image_url.strip()
    
def get_browse_block_content(p):
    block = 'block '.lower() + str(p)
    image_counter = 'browse-gifts-0' + str(p)
    for image_url in open(csv_file_path):
        try:
            if image_counter in image_url:
                outputDictionary['Browse_Gifts'][block]['ImageSrc'] = image_url.strip()
        except AttributeError:
            pass

def get_gifts_under_block_content(p):
    block = 'block '.lower() + str(p)
    image_counter = 'gifts-under-0' + str(p)
    for image_url in open(csv_file_path):
        try:
            if image_counter in image_url:
                outputDictionary['Gifts_Under'][block]['ImageSrc'] = image_url.strip()
        except AttributeError:
            pass

def get_inspiration_block_content(p):
    block = 'block '.lower() + str(p)
    image_counter = 'inspiration-0' + str(p)
    for image_url in open(csv_file_path):
        try:
            if image_counter in image_url:
                outputDictionary['Inspiration'][block]['ImageSrc'] = image_url.strip()
        except AttributeError:
            pass
def get_blog_block_content(p):
    block = 'block '.lower() + str(p)
    image_counter = 'inspiration-0' + str(p)
    for image_url in open(csv_file_path):
        try:
            if image_counter in image_url:
                outputDictionary['Blog'][block]['ImageSrc'] = image_url.strip()
        except AttributeError:
            pass

def popular_categories():
        for image_url in open(csv_file_path):
            if 'popular-categories-left' in image_url:
                outputDictionary['Popular_Categories']['Left']['ImgSrc'] = image_url.strip() 
            if 'popular-categories-right' in image_url:
                outputDictionary['Popular_Categories']['Right']['ImgSrc'] = image_url.strip() 

def import_links():
    x = xlrd.open_workbook(xlsx_file_path)
    xl = x.sheet_by_name('master')
    outputDictionary['Hero']['Link'] = xl.cell_value(0,1).strip()
    outputDictionary['Browse_Gifts']['block 1']['Link'] = xl.cell_value(1,1).strip()
    outputDictionary['Browse_Gifts']['block 2']['Link'] = xl.cell_value(2,1).strip()
    outputDictionary['Browse_Gifts']['block 3']['Link'] = xl.cell_value(3,1).strip()
    outputDictionary['Browse_Gifts']['block 4']['Link'] = xl.cell_value(4,1).strip()
    outputDictionary['Gifts_Under']['Link'] = xl.cell_value(5,1).strip()
    outputDictionary['Gifts_Under']['block 1']['Link'] = xl.cell_value(6,1).strip()
    outputDictionary['Gifts_Under']['block 2']['Link'] = xl.cell_value(7,1).strip()
    outputDictionary['Gifts_Under']['block 3']['Link'] = xl.cell_value(8,1).strip()
    outputDictionary['Gifts_Under']['block 4']['Link'] = xl.cell_value(9,1).strip()
    outputDictionary['Inspiration']['block 1']['Link'] = xl.cell_value(10,1).strip()
    outputDictionary['Inspiration']['block 2']['Link'] = xl.cell_value(11,1).strip()
    outputDictionary['Inspiration']['block 3']['Link'] = xl.cell_value(12,1).strip()
    outputDictionary['Inspiration']['block 4']['Link'] = xl.cell_value(13,1).strip()
    outputDictionary['Blog']['block 1']['Link'] = xl.cell_value(14,1).strip()
    outputDictionary['Blog']['block 2']['Link'] = xl.cell_value(15,1).strip()
    outputDictionary['Blog']['block 3']['Link'] = xl.cell_value(16,1).strip()
    outputDictionary['Popular_Categories']['Left']['Link'] = xl.cell_value(17,1).strip()
    outputDictionary['Popular_Categories']['Right']['Link'] = xl.cell_value(18,1).strip()
    
get_hero_content()
get_browse_block_content(1)
get_browse_block_content(2)
get_browse_block_content(3)
get_browse_block_content(4)
get_gifts_under_block_content(1)
get_gifts_under_block_content(2)
get_gifts_under_block_content(3)
get_gifts_under_block_content(4)
get_inspiration_block_content(1)
get_inspiration_block_content(2)
get_inspiration_block_content(3)
get_inspiration_block_content(4)
get_blog_block_content(1)
get_blog_block_content(2)
get_blog_block_content(3)
popular_categories()

import_links()

with codecs.open(_path +'data.json', 'w', encoding="utf-8") as outfile:
    json.dump(outputDictionary, outfile, indent=4, sort_keys=True, ensure_ascii=False)

