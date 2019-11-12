import json
from pathlib import Path
import os

path = Path.cwd()
absolute = (str(path))

os.makedirs(Path(absolute).joinpath('./production'), exist_ok=True)

user_input = input('desired output file EG womens: ')

html_prod_path = absolute + "/production/" + user_input + ".html"
scss_prod_path = absolute + "/production/" + user_input + ".scss"

html_template_path = absolute + "/templates/template.html"
sass_template_path = absolute + "/templates/template.scss"


def try_get_data(data, a, b):
    try:
        return data[a][b]
    except KeyError:
        return "An error occured"

def try_get_newin_data(data, a, b, c):
    try:
        return data[a][b][c]
    except KeyError:
        return "An error occured"

def html_hero_content(p):
    try:
        with open(p, 'r') as file:
            file_data = file.read()
            
            heroTextOne = try_get_data(data, 'Hero', 'Text_One')
            heroTextTwo = try_get_data(data, 'Hero', 'Text_Two')
            heroButtonText = try_get_data(data, 'Hero', 'Button_Text')
            heroImageMobile = try_get_data(data, 'Hero', 'Mobile')
            heroLink = try_get_data(data, 'Hero', 'Link')
            heroTracking = try_get_data(data, 'Hero', 'Tracking')

            file_data = file_data.replace('[Hero_Text_One]', heroTextOne)
            file_data = file_data.replace('[Hero_Text_Two]', heroTextTwo)
            file_data = file_data.replace('[Hero_Button_Text]', heroButtonText)
            file_data = file_data.replace('[Hero_Image_Mobile]', heroImageMobile)
            file_data = file_data.replace('[Hero_Link]', heroLink)
            file_data = file_data.replace('[Hero_Tracking]', heroTracking)

            print('populating hero content...')

        return file_data
    except TypeError:
        pass


def html_newin_content():
    with open(absolute + '/templates/html_modules/newin.html', 'r') as file:
        file_data = file.read()

        Title = try_get_data(data, 'NewInBlock', 'Title')

        blockOneButtonText = try_get_newin_data(data, 'NewInBlock', 'block 1', 'Button_Text')
        blockTwoButtonText = try_get_newin_data(data, 'NewInBlock', 'block 2', 'Button_Text')
        blockThreeButtonText = try_get_newin_data(data, 'NewInBlock', 'block 3', 'Button_Text')
        blockFourButtonText = try_get_newin_data(data, 'NewInBlock', 'block 4', 'Button_Text')

        blockOneImgSrc = try_get_newin_data(data, 'NewInBlock', 'block 1', 'ImageSrc')
        blockTwoImgSrc = try_get_newin_data(data, 'NewInBlock', 'block 2', 'ImageSrc')
        blockThreeImgSrc = try_get_newin_data(data, 'NewInBlock', 'block 3', 'ImageSrc')
        blockFourImgSrc = try_get_newin_data(data, 'NewInBlock', 'block 4', 'ImageSrc')

        BlockOneLink = try_get_newin_data(data, 'NewInBlock', 'block 1', 'Link')
        BlockTwoLink = try_get_newin_data(data, 'NewInBlock', 'block 2', 'Link')
        BlockThreeLink = try_get_newin_data(data, 'NewInBlock', 'block 3', 'Link')
        BlockFourLink = try_get_newin_data(data, 'NewInBlock', 'block 4', 'Link')

        BlockOneTracking = try_get_newin_data(data, 'NewInBlock', 'block 1', 'Tracking')
        BlockTwoTracking = try_get_newin_data(data, 'NewInBlock', 'block 2', 'Tracking')
        BlockThreeTracking = try_get_newin_data(data, 'NewInBlock', 'block 3', 'Tracking')
        BlockFourTracking = try_get_newin_data(data, 'NewInBlock', 'block 4', 'Tracking')

        file_data = file_data.replace('[Title]', Title)

        file_data = file_data.replace('[Button_Text_1]', blockOneButtonText)
        file_data = file_data.replace('[Button_Text_2]', blockTwoButtonText)
        file_data = file_data.replace('[Button_Text_3]', blockThreeButtonText)
        file_data = file_data.replace('[Button_Text_4]', blockFourButtonText)

        file_data = file_data.replace('[Block_1_ImageSrc]', blockOneImgSrc)
        file_data = file_data.replace('[Block_2_ImageSrc]', blockTwoImgSrc)
        file_data = file_data.replace('[Block_3_ImageSrc]', blockThreeImgSrc)
        file_data = file_data.replace('[Block_4_ImageSrc]', blockFourImgSrc)

        file_data = file_data.replace('[Block_1_Link]', BlockOneLink)
        file_data = file_data.replace('[Block_2_Link]', BlockTwoLink)
        file_data = file_data.replace('[Block_3_Link]', BlockThreeLink)
        file_data = file_data.replace('[Block_4_Link]', BlockFourLink)

        file_data = file_data.replace('[Block_1_Tracking]', BlockOneTracking)
        file_data = file_data.replace('[Block_2_Tracking]', BlockTwoTracking)
        file_data = file_data.replace('[Block_3_Tracking]', BlockThreeTracking)
        file_data = file_data.replace('[Block_4_Tracking]', BlockFourTracking)

        print('populating newin content...')

    return file_data

def html_bottom_blocks_content():
    with open(absolute + '/templates/html_modules/bottom_blocks.html', 'r') as file:
        file_data = file.read()
        leftBlockTextOne = try_get_data(data, 'LeftBlock', 'Text_One')
        leftBlockTextTwo = try_get_data(data, 'LeftBlock', 'Text_Two')
        leftBlockImgSrc = try_get_data(data, 'LeftBlock', 'ImageSrc')
        leftBlockLink = try_get_data(data, 'LeftBlock', 'Link')
        leftBlockTracking = try_get_data(data, 'LeftBlock', 'Tracking')

        rightBlockTextOne = try_get_data(data, 'RightBlock', 'Text_One')
        rightBlockTextTwo = try_get_data(data, 'RightBlock', 'Text_Two')
        rightBlockImgSrc = try_get_data(data, 'RightBlock', 'ImageSrc')
        rightBlockLink = try_get_data(data, 'RightBlock', 'Link')
        rightBlockTracking = try_get_data(data, 'RightBlock', 'Tracking')
        
        file_data = file_data.replace('[Block_Left_Text_One]', leftBlockTextOne)
        file_data = file_data.replace('[Block_Left_Text_Two]', leftBlockTextTwo)
        file_data = file_data.replace('[Block_Left_ImageSrc]', leftBlockImgSrc)
        file_data = file_data.replace('[Block_Left_Link]', leftBlockLink)
        file_data = file_data.replace('[Block_Left_Tracking]', leftBlockTracking)

        file_data = file_data.replace('[Block_Right_Text_One]', rightBlockTextOne)
        file_data = file_data.replace('[Block_Right_Text_Two]', rightBlockTextTwo)
        file_data = file_data.replace('[Block_Right_ImageSrc]', rightBlockImgSrc)
        file_data = file_data.replace('[Block_Right_Link]', rightBlockLink)
        file_data = file_data.replace('[Block_Right_Tracking]', rightBlockTracking)

        print('populating bottom block content...')

    return file_data

def html_baby_blocks_content():
    with open(absolute + '/templates/html_modules/baby_top_blocks.html', 'r') as file:
        file_data = file.read()

        BabyTopTitle = try_get_data(data, 'TopTitle', 'Title')
        BabyTopSub = try_get_data(data, 'TopTitle', 'Sub')
        
        leftBlockTextOne = try_get_data(data, 'LeftBlock', 'Text_One')
        leftBlockTextTwo = try_get_data(data, 'LeftBlock', 'Text_Two')
        leftBlockButtonText = try_get_data(data, 'LeftBlock', 'Button_Text')
        leftBlockImgSrc = try_get_data(data, 'LeftBlock', 'ImageSrc')
        leftBlockLink = try_get_data(data, 'LeftBlock', 'Link')
        leftBlockTracking = try_get_data(data, 'LeftBlock', 'Tracking')

        rightBlockTextOne = try_get_data(data, 'RightBlock', 'Text_One')
        rightBlockTextTwo = try_get_data(data, 'RightBlock', 'Text_Two')
        rightBlockButtonText = try_get_data(data, 'LeftBlock', 'Button_Text')
        rightBlockImgSrc = try_get_data(data, 'RightBlock', 'ImageSrc')
        rightBlockLink = try_get_data(data, 'RightBlock', 'Link')
        rightBlockTracking = try_get_data(data, 'RightBlock', 'Tracking')
        
        file_data = file_data.replace('[Baby_Top_Title]', BabyTopTitle)
        file_data = file_data.replace('[Baby_Top_Sub]', BabyTopSub)

        file_data = file_data.replace('[Block_Left_Text_One]', leftBlockTextOne)
        file_data = file_data.replace('[Block_Left_Text_Two]', leftBlockTextTwo)
        file_data = file_data.replace('[Block_Left_Button_Text]', leftBlockButtonText)
        file_data = file_data.replace('[Block_Left_ImageSrc]', leftBlockImgSrc)
        file_data = file_data.replace('[Block_Left_Link]', leftBlockLink)
        file_data = file_data.replace('[Block_Left_Tracking]', leftBlockTracking)

        file_data = file_data.replace('[Block_Right_Text_One]', rightBlockTextOne)
        file_data = file_data.replace('[Block_Right_Text_Two]', rightBlockTextTwo)
        file_data = file_data.replace('[Block_Right_Button_Text]', rightBlockButtonText)
        file_data = file_data.replace('[Block_Right_ImageSrc]', rightBlockImgSrc)
        file_data = file_data.replace('[Block_Right_Link]', rightBlockLink)
        file_data = file_data.replace('[Block_Right_Tracking]', rightBlockTracking)
       
        print('populating baby block content...')
    return file_data

def get_html_hero():
    with open(absolute + '/resources/data.json') as json_file:
        data = json.load(json_file)
        try:
            hero_type = data['Hero']['Type']
            if "HERO" in hero_type:
                if "HERO - FULL BLEED" in hero_type:
                    html_full_bleed = absolute + "/templates/html_modules/hero_full_bleed.html"
                    html_content = html_hero_content(html_full_bleed)
                    return html_content
                if "HERO - 2 SPLIT LEFT" in hero_type:
                    html_2_split_left = absolute + "/templates/html_modules/hero_2_split_left.html"
                    html_content = html_hero_content(html_2_split_left)
                    return html_content
                if "HERO - 2 SPLIT RIGHT" in hero_type:
                    html_2_split_right = absolute + "/templates/html_modules/hero_2_split_right.html"
                    html_content = html_hero_content(html_2_split_right)
                    return html_content
                if "HERO - 3 SPLIT" in hero_type:
                    html_3_col = absolute + "/templates/html_modules/hero_3_col.html"
                    html_content = html_hero_content(html_3_col)
                    return html_content
                else:
                    return ''
        except KeyError:
            pass
            
 # Read Json file
with open(absolute + '/resources/data.json') as json_file:
    data = json.load(json_file)
    
def sass_full_bleed():
    sass_full_bleed = absolute + "/templates/sass_modules/hero_full_bleed.scss" 
    with open(sass_full_bleed, 'r') as file:
        file_data = file.read()
        heroImageOne = try_get_data(data, 'Hero', 'Image_One')
        file_data = file_data.replace('[Hero_Image_One]', heroImageOne)
    return file_data

def sass_two_col_left():
    sass_2_split_left = absolute + "/templates/sass_modules/hero_2_split_left.scss"
    with open(sass_2_split_left, 'r') as file:
        file_data = file.read()

        heroImageOne = try_get_data(data, 'Hero', 'Image_One')
        heroImageTwo = try_get_data(data, 'Hero', 'Image_Two')
        heroImageTablet = try_get_data(data, 'Hero', 'Tablet')
        
        file_data = file_data.replace('[Hero_Image_One]', heroImageOne)
        file_data = file_data.replace('[Hero_Image_Two]', heroImageTwo)
        file_data = file_data.replace('[Hero_Image_Tablet]', heroImageTablet)
    return file_data

def sass_two_col_right():
    sass_2_split_right = absolute + "/templates/sass_modules/hero_2_split_right.scss"
    with open(sass_2_split_right, 'r') as file:
        file_data = file.read()

        heroImageOne = try_get_data(data, 'Hero', 'Image_One')
        heroImageTwo = try_get_data(data, 'Hero', 'Image_Two')
        heroImageTablet = try_get_data(data, 'Hero', 'Tablet')

        file_data = file_data.replace('[Hero_Image_One]', heroImageOne)
        file_data = file_data.replace('[Hero_Image_Two]', heroImageTwo)
        file_data = file_data.replace('[Hero_Image_Tablet]', heroImageTablet)
    return file_data      

def sass_three_split():
    sass_3_col = absolute + "/templates/sass_modules/hero_3_col.scss"
    with open(sass_3_col, 'r') as file:
        file_data = file.read()

        heroImageOne = try_get_data(data, 'Hero', 'Image_One')
        heroImageTwo = try_get_data(data, 'Hero', 'Image_Two')
        heroImageThree = try_get_data(data, 'Hero', 'Image_Three')
        heroImageTablet = try_get_data(data, 'Hero', 'Tablet')

        file_data = file_data.replace('[Hero_Image_One]', heroImageOne)
        file_data = file_data.replace('[Hero_Image_Two]', heroImageTwo)
        file_data = file_data.replace('[Hero_Image_Three]', heroImageThree)
        file_data = file_data.replace('[Hero_Image_Tablet]', heroImageTablet)
    return file_data      

def insert_hero():
    html_list = []

    with open(html_template_path, 'r') as file:
        html_master_template = file.read()
        a = None
        try:
            a = data['Hero']
        except KeyError:
            pass
        if not a:
            html_list.append(html_baby_blocks_content())
            html_list.append(html_newin_content())
        else:
            try:
                html_list.append(get_html_hero())
            except:
                pass
            html_list.append(html_newin_content())
            html_list.append(html_bottom_blocks_content())
      
        join_list = ''.join(html_list) 
        # print(html_list)
        html_master_template = html_master_template.replace('[content]', join_list) 
         
    with open(html_prod_path, 'w') as file:
        file.write(html_master_template)

with open(sass_template_path, 'r') as file:
    scss_master_template = file.read()

    with open(absolute + '/resources/data.json') as json_file:
        data = json.load(json_file)
        try:
            hero_type = data['Hero']['Type']      
            if "HERO" in hero_type:
                if "HERO - FULL BLEED" in hero_type:
                    scss_master_template = scss_master_template.replace('[hero]', sass_full_bleed())
                    with open(scss_prod_path, 'w') as file:
                        file.write(scss_master_template)
                        file.close()
                if "HERO - 2 SPLIT LEFT" in hero_type:
                    scss_master_template = scss_master_template.replace('[hero]', sass_two_col_left())   
                    with open(scss_prod_path, 'w') as file:
                        file.write(scss_master_template)
                        file.close()
                if "HERO - 2 SPLIT RIGHT" in hero_type:
                    scss_master_template = scss_master_template.replace('[hero]', sass_two_col_right()) 
                    with open(scss_prod_path, 'w') as file:
                        file.write(scss_master_template)
                        file.close()
                if "HERO - 3 SPLIT" in hero_type:
                    scss_master_template = scss_master_template.replace('[hero]', sass_three_split()) 
                    with open(scss_prod_path, 'w') as file:
                        file.write(scss_master_template)
                        file.close()
                print('populating sass...')
        except KeyError:
            pass

# Call functions
insert_hero()