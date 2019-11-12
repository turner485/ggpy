import json
import csv
import codecs
import xlrd
from pathlib import Path

# create absolute path for linux windows
path = Path.cwd()
absolute = (str(path))

region = '_' + input('please input region IE DE: ').upper() + '.xlsx'

link_csv = absolute + '/resources/links' + region

with codecs.open(absolute + '/resources/data.json', 'r', encoding="utf-8-sig") as file:
    data = json.load(file)

    x = xlrd.open_workbook(link_csv)
    homepage = x.sheet_by_name(str(input('*CASE SENSITIVE* \nEnter name of sheet IE Womens: ')))


    if homepage.cell_value(0,1) == '':
        print('empty cell...')
    else:
         data['Hero']['Link'] = homepage.cell_value(0,1)

    data['NewInBlock']['block 1']['Link'] = homepage.cell_value(1,1)
    data['NewInBlock']['block 2']['Link'] = homepage.cell_value(2,1)
    data['NewInBlock']['block 3']['Link'] = homepage.cell_value(3,1)
    data['NewInBlock']['block 4']['Link'] = homepage.cell_value(4,1)
    data['LeftBlock']['Link'] = homepage.cell_value(5,1)
    data['RightBlock']['Link'] = homepage.cell_value(6,1)

    if homepage.cell_value(0,2) == '':
        print('empty cell...')
    else:
        data['Hero']['Tracking'] = homepage.cell_value(0,2)    

    data['NewInBlock']['block 1']['Tracking'] = homepage.cell_value(1,2)
    data['NewInBlock']['block 2']['Tracking'] = homepage.cell_value(2,2)
    data['NewInBlock']['block 3']['Tracking'] = homepage.cell_value(3,2)
    data['NewInBlock']['block 4']['Tracking'] = homepage.cell_value(4,2)
    data['LeftBlock']['Tracking'] = homepage.cell_value(5,2)
    data['RightBlock']['Tracking'] = homepage.cell_value(6,2)
   

    print('exporting links to json...')
    
    with codecs.open(absolute + '/resources/data.json', 'w', encoding="utf-8") as outfile:
        json.dump(data, outfile, indent=4, sort_keys=True, ensure_ascii=False)  