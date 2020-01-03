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

    browse_count = outputDictionary['Browse_Gifts']['count']
    gifts_under_twenty_count = outputDictionary['Gifts_Under_20']['count']
    gifts_under_forty_count = outputDictionary['Gifts_Under_40']['count']
    inspiration_count = outputDictionary['Inspiration']['count']
    blog_count = outputDictionary['Blog']['count']
   

def get_hero_content():
     for image_url in open(csv_file_path):
        if 'hero-01' in image_url:
            outputDictionary['Hero']['Image_One'] = image_url.strip()
        if 'hero-02' in image_url:
            outputDictionary['Hero']['Image_Two'] = image_url.strip()
        if 'hero-03' in image_url:
            outputDictionary['Hero']['Image_Three'] = image_url.strip()
    
def get_browse_block_content():
   
    for image_url in open(csv_file_path):
        for i in range(browse_count + 1):
            block = 'block '.lower() + str(i)
            image_counter = 'browse-gifts-0' + str(i)
            try:
                if image_counter in image_url:
                    outputDictionary['Browse_Gifts'][block]['ImageSrc'] = image_url.strip()
            except AttributeError:
                pass

def get_gifts_under_20_block_content():
    
    for image_url in open(csv_file_path):
        for i in range(gifts_under_twenty_count + 1):
            block = 'block '.lower() + str(i)
            image_counter = 'gifts-under-20-0' + str(i)
            try:
                if image_counter in image_url:
                    outputDictionary['Gifts_Under_20'][block]['ImageSrc'] = image_url.strip()
            except AttributeError:
                pass

def get_gifts_under_40_block_content():
    
    for image_url in open(csv_file_path):
        for i in range(gifts_under_forty_count + 1):
            block = 'block '.lower() + str(i)
            image_counter = 'gifts-under-40-0' + str(i)
            try:
                if image_counter in image_url:
                    outputDictionary['Gifts_Under_40'][block]['ImageSrc'] = image_url.strip()
            except AttributeError:
                pass

def get_inspiration_block_content():
    
    for image_url in open(csv_file_path):
        for i in range(inspiration_count + 1):
            block = 'block '.lower() + str(i)
            image_counter = 'inspiration-0' + str(i)
            try:
                if image_counter in image_url:
                    outputDictionary['Inspiration'][block]['ImageSrc'] = image_url.strip()
            except AttributeError:
                pass
def get_blog_block_content():
    
    for image_url in open(csv_file_path):
        for i in range(blog_count + 1):
            block = 'block '.lower() + str(i)
            image_counter = 'blog-0' + str(i)
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
    # read xl sheet master
    x = xlrd.open_workbook(xlsx_file_path)
    xl = x.sheet_by_name('master')
    # Write to json
    outputDictionary['Hero']['Link'] = xl.cell_value(0,1).strip()
    outputDictionary['Gifts_Under_20']['Link'] = xl.cell_value(1,1).strip()
    outputDictionary['Gifts_Under_40']['Link'] = xl.cell_value(2,1).strip()
    outputDictionary['Popular_Categories']['Left']['Link'] = xl.cell_value(3,1).strip()
    outputDictionary['Popular_Categories']['Right']['Link'] = xl.cell_value(4,1).strip()
    # Swap xl sheet to carousels
    x = xlrd.open_workbook(xlsx_file_path)
    xl = x.sheet_by_name('carousels')
    for i in range(browse_count):
        outputDictionary['Browse_Gifts'][f'block {i + 1}']['Link'] = xl.cell_value(i,1).strip()
    a = i
    for j in range(gifts_under_twenty_count):
        a += 1
        outputDictionary['Gifts_Under_20'][f'block {j + 1}']['Link'] = xl.cell_value(a,1).strip()
    b = a
    for k in range(gifts_under_forty_count):
        b += 1
        outputDictionary['Gifts_Under_40'][f'block {k + 1}']['Link'] = xl.cell_value(b,1).strip()
    c = b
    for z in range(inspiration_count):
        c += 1
        outputDictionary['Inspiration'][f'block {z + 1}']['Link'] = xl.cell_value(c,1).strip()
    d = c
    for w in range(blog_count):
        d += 1
        outputDictionary['Blog'][f'block {w + 1}']['Link'] = xl.cell_value(d,1).strip()
   
    
get_hero_content()
get_browse_block_content()
get_gifts_under_20_block_content()
get_gifts_under_40_block_content()
get_inspiration_block_content()
get_blog_block_content()
popular_categories()
import_links()

print('Populating image sources and links to data.json...')

with codecs.open(_path +'data.json', 'w', encoding="utf-8") as outfile:
    json.dump(outputDictionary, outfile, indent=4, sort_keys=True, ensure_ascii=False)

