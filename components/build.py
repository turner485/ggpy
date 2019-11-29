# Import libs
import json
from pathlib import Path
import os
### create vars
_path = 'C://Users//Ben.Turner//Documents//code//python//ggpy//'
os.makedirs(Path(_path).joinpath('production'), exist_ok=True)
html_template = _path + 'templates//template.html'
scss_template = _path + 'templates//template.scss'
html_production = _path + 'production//index.html'
scss_production = _path + 'production//UK.scss'
###
# create function that gets json globally 
def get_json_data():
    try:
        with open('resources/data.json') as json_file:
            data = json.load(json_file)
        return data
    except:
        return None
###
# create function that gets html globally 
def get_html():
    with open(html_template, 'r') as file:
        file_data = file.read()
    return file_data
###
# try get function 2 parameters 
def try_get_data(data, a, b):
    try:
        return data[a][b]
    except KeyError:
        return "An error occured"
###
# try get function 3 parameters 
def try_get_row_data(data, a, b, c):
    try:
        return data[a][b][c]
    except KeyError:
        return "An error occured"
###
# create main function that writes to html
def main(data, html):
    file_data = html_hero_content(data, html)
    file_data = html_browse_gifts_content(data, file_data)
    file_data = html_popular_categories_content(data, file_data)
    file_data = html_gifts_under_content(data, file_data)
    file_data = html_inspiration_content(data, file_data)
    file_data = html_blog_content(data, file_data)
    #build html
    with open(html_production, 'w') as file:
        file.write(file_data)
###
def html_hero_content(data, html):
    file_data = html
    # get data
    HeroHeadline = try_get_data(data, 'Hero', 'Headline')
    heroButtonText = try_get_data(data, 'Hero', 'Button_Text')
    heroLink = try_get_data(data, 'Hero', 'Link')
    # data replace
    file_data = file_data.replace('[Hero_Headline]', HeroHeadline)
    file_data = file_data.replace('[Hero_Button_Text]', heroButtonText)
    file_data = file_data.replace('[Hero_Link]', heroLink)
    return file_data
###
def scss_hero_content(data):
    try:
        with open(scss_template, 'r') as file:
            file_data = file.read()
            # get data
            heroImageOne = try_get_data(data, 'Hero', 'Image_One')
            heroImageTwo = try_get_data(data, 'Hero', 'Image_Two')
            heroImageThree = try_get_data(data, 'Hero', 'Image_Three')
            # data replace
            file_data = file_data.replace('[Hero_Image_One]', heroImageOne)
            file_data = file_data.replace('[Hero_Image_Two]', heroImageTwo)
            file_data = file_data.replace('[Hero_Image_Three]', heroImageThree)
            # build sass
            with open(scss_production, 'w') as file:
                file.write(file_data)

    except TypeError:
        pass
###
def html_browse_gifts_content(data, html):
    #pass html through parameter 
    file_data = html
    # get json data
    Headline = try_get_data(data, 'Browse_Gifts', 'Headline')
    blockOneButtonText = try_get_row_data(data, 'Browse_Gifts', 'block 1', 'Button_Text')
    blockTwoButtonText = try_get_row_data(data, 'Browse_Gifts', 'block 2', 'Button_Text')
    blockThreeButtonText = try_get_row_data(data, 'Browse_Gifts', 'block 3', 'Button_Text')
    blockFourButtonText = try_get_row_data(data, 'Browse_Gifts', 'block 4', 'Button_Text')
    blockOneImgSrc = try_get_row_data(data, 'Browse_Gifts', 'block 1', 'ImageSrc')
    blockTwoImgSrc = try_get_row_data(data, 'Browse_Gifts', 'block 2', 'ImageSrc')
    blockThreeImgSrc = try_get_row_data(data, 'Browse_Gifts', 'block 3', 'ImageSrc')
    blockFourImgSrc = try_get_row_data(data, 'Browse_Gifts', 'block 4', 'ImageSrc')
    BlockOneLink = try_get_row_data(data, 'Browse_Gifts', 'block 1', 'Link')
    BlockTwoLink = try_get_row_data(data, 'Browse_Gifts', 'block 2', 'Link')
    BlockThreeLink = try_get_row_data(data, 'Browse_Gifts', 'block 3', 'Link')
    BlockFourLink = try_get_row_data(data, 'Browse_Gifts', 'block 4', 'Link')
    #replace data
    file_data = file_data.replace('[Browse_Gifts_Headline]', Headline)
    file_data = file_data.replace('[Browse_Gifts_Block_1_Text]', blockOneButtonText)
    file_data = file_data.replace('[Browse_Gifts_Block_2_Text]', blockTwoButtonText)
    file_data = file_data.replace('[Browse_Gifts_Block_3_Text]', blockThreeButtonText)
    file_data = file_data.replace('[Browse_Gifts_Block_4_Text]', blockFourButtonText)
    file_data = file_data.replace('[Browse_Gifts_Block_1_Image_Source]', blockOneImgSrc)
    file_data = file_data.replace('[Browse_Gifts_Block_2_Image_Source]', blockTwoImgSrc)
    file_data = file_data.replace('[Browse_Gifts_Block_3_Image_Source]', blockThreeImgSrc)
    file_data = file_data.replace('[Browse_Gifts_Block_4_Image_Source]', blockFourImgSrc)
    file_data = file_data.replace('[Browse_Gifts_Block_1_Link]', BlockOneLink)
    file_data = file_data.replace('[Browse_Gifts_Block_2_Link]', BlockTwoLink)
    file_data = file_data.replace('[Browse_Gifts_Block_3_Link]', BlockThreeLink)
    file_data = file_data.replace('[Browse_Gifts_Block_4_Link]', BlockFourLink)
    # return data
    return file_data
###
def html_popular_categories_content(data, html):
    #pass html through parameter 
    file_data = html
    #get json data
    PopularCategoriesLeftText = try_get_row_data(data, 'Popular_Categories','Left', 'Button_Text')
    PopularCategoriesLeftImgSrc = try_get_row_data(data, 'Popular_Categories','Left', 'ImgSrc')
    PopularCategoriesLeftLink = try_get_row_data(data, 'Popular_Categories','Left', 'Link')
    PopularCategoriesRightText = try_get_row_data(data, 'Popular_Categories','Right', 'Button_Text')
    PopularCategoriesRightImgSrc = try_get_row_data(data, 'Popular_Categories','Right', 'ImgSrc')
    PopularCategoriesRightLink = try_get_row_data(data, 'Popular_Categories','Right', 'Link')
    #replace data
    file_data = file_data.replace('[Popular_Categories_Left_Text]', PopularCategoriesLeftText)
    file_data = file_data.replace('[Popular_Categories_Left_Image_Source]', PopularCategoriesLeftImgSrc)
    file_data = file_data.replace('[Popular_Categories_Left_Link]', PopularCategoriesLeftLink)
    file_data = file_data.replace('[Popular_Categories_Right_Text]', PopularCategoriesRightText)
    file_data = file_data.replace('[Popular_Categories_Right_Image_Source]', PopularCategoriesRightImgSrc)
    file_data = file_data.replace('[Popular_Categories_Right_Link]', PopularCategoriesRightLink)
    #return data
    return file_data
###
def html_gifts_under_content(data, html):
    #pass html 
    file_data = html
    #get json data
    Headline = try_get_data(data, 'Gifts_Under', 'Headline')
    ButtonText = try_get_data(data, 'Gifts_Under', 'Button_Text')
    ButtonLink = try_get_data(data, 'Gifts_Under', 'Link')
    blockOneButtonText = try_get_row_data(data, 'Gifts_Under', 'block 1', 'Button_Text')
    blockTwoButtonText = try_get_row_data(data, 'Gifts_Under', 'block 2', 'Button_Text')
    blockThreeButtonText = try_get_row_data(data, 'Gifts_Under', 'block 3', 'Button_Text')
    blockFourButtonText = try_get_row_data(data, 'Gifts_Under', 'block 4', 'Button_Text')
    blockOneImgSrc = try_get_row_data(data, 'Gifts_Under', 'block 1', 'ImageSrc')
    blockTwoImgSrc = try_get_row_data(data, 'Gifts_Under', 'block 2', 'ImageSrc')
    blockThreeImgSrc = try_get_row_data(data, 'Gifts_Under', 'block 3', 'ImageSrc')
    blockFourImgSrc = try_get_row_data(data, 'Gifts_Under', 'block 4', 'ImageSrc')
    BlockOneLink = try_get_row_data(data, 'Gifts_Under', 'block 1', 'Link')
    BlockTwoLink = try_get_row_data(data, 'Gifts_Under', 'block 2', 'Link')
    BlockThreeLink = try_get_row_data(data, 'Gifts_Under', 'block 3', 'Link')
    BlockFourLink = try_get_row_data(data, 'Gifts_Under', 'block 4', 'Link')
    #replace data
    file_data = file_data.replace('[Gifts_Under_Headline]', Headline)
    file_data = file_data.replace('[Gifts_Under_Button_Text]', ButtonText)
    file_data = file_data.replace('[Gifts_Under_Button_Link]', ButtonLink)
    file_data = file_data.replace('[Gifts_Under_Block_1_Text]', blockOneButtonText)
    file_data = file_data.replace('[Gifts_Under_Block_2_Text]', blockTwoButtonText)
    file_data = file_data.replace('[Gifts_Under_Block_3_Text]', blockThreeButtonText)
    file_data = file_data.replace('[Gifts_Under_Block_4_Text]', blockFourButtonText)
    file_data = file_data.replace('[Gifts_Under_Block_1_Image_Source]', blockOneImgSrc)
    file_data = file_data.replace('[Gifts_Under_Block_2_Image_Source]', blockTwoImgSrc)
    file_data = file_data.replace('[Gifts_Under_Block_3_Image_Source]', blockThreeImgSrc)
    file_data = file_data.replace('[Gifts_Under_Block_4_Image_Source]', blockFourImgSrc)
    file_data = file_data.replace('[Gifts_Under_Block_1_Link]', BlockOneLink)
    file_data = file_data.replace('[Gifts_Under_Block_2_Link]', BlockTwoLink)
    file_data = file_data.replace('[Gifts_Under_Block_3_Link]', BlockThreeLink)
    file_data = file_data.replace('[Gifts_Under_Block_4_Link]', BlockFourLink)
    # return data
    return file_data
###
def html_inspiration_content(data, html):
        file_data = html
        # get json data
        Headline = try_get_data(data, 'Inspiration', 'Headline')
        blockOneButtonText = try_get_row_data(data, 'Inspiration', 'block 1', 'Button_Text')
        blockTwoButtonText = try_get_row_data(data, 'Inspiration', 'block 2', 'Button_Text')
        blockThreeButtonText = try_get_row_data(data, 'Inspiration', 'block 3', 'Button_Text')
        blockFourButtonText = try_get_row_data(data, 'Inspiration', 'block 4', 'Button_Text')
        blockOneImgSrc = try_get_row_data(data, 'Inspiration', 'block 1', 'ImageSrc')
        blockTwoImgSrc = try_get_row_data(data, 'Inspiration', 'block 2', 'ImageSrc')
        blockThreeImgSrc = try_get_row_data(data, 'Inspiration', 'block 3', 'ImageSrc')
        blockFourImgSrc = try_get_row_data(data, 'Inspiration', 'block 4', 'ImageSrc')
        BlockOneLink = try_get_row_data(data, 'Inspiration', 'block 1', 'Link')
        BlockTwoLink = try_get_row_data(data, 'Inspiration', 'block 2', 'Link')
        BlockThreeLink = try_get_row_data(data, 'Inspiration', 'block 3', 'Link')
        BlockFourLink = try_get_row_data(data, 'Inspiration', 'block 4', 'Link')
        # replace data
        file_data = file_data.replace('[Inspiration_Headline]', Headline)
        file_data = file_data.replace('[Inspiration_Block_1_Text]', blockOneButtonText)
        file_data = file_data.replace('[Inspiration_Block_2_Text]', blockTwoButtonText)
        file_data = file_data.replace('[Inspiration_Block_3_Text]', blockThreeButtonText)
        file_data = file_data.replace('[Inspiration_Block_4_Text]', blockFourButtonText)
        file_data = file_data.replace('[Inspiration_Block_1_Image_Source]', blockOneImgSrc)
        file_data = file_data.replace('[Inspiration_Block_2_Image_Source]', blockTwoImgSrc)
        file_data = file_data.replace('[Inspiration_Block_3_Image_Source]', blockThreeImgSrc)
        file_data = file_data.replace('[Inspiration_Block_4_Image_Source]', blockFourImgSrc)
        file_data = file_data.replace('[Inspiration_Block_1_Link]', BlockOneLink)
        file_data = file_data.replace('[Inspiration_Block_2_Link]', BlockTwoLink)
        file_data = file_data.replace('[Inspiration_Block_3_Link]', BlockThreeLink)
        file_data = file_data.replace('[Inspiration_Block_4_Link]', BlockFourLink)
        # return data
        return file_data
###
def html_blog_content(data, html):
        # pass html
        file_data = html
        # get json data
        Headline = try_get_data(data, 'Blog', 'Headline')
        blockOneButtonText = try_get_row_data(data, 'Blog', 'block 1', 'Text')
        blockTwoButtonText = try_get_row_data(data, 'Blog', 'block 2', 'Text')
        blockThreeButtonText = try_get_row_data(data, 'Blog', 'block 3', 'Text')
        blockOneImgSrc = try_get_row_data(data, 'Blog', 'block 1', 'ImageSrc')
        blockTwoImgSrc = try_get_row_data(data, 'Blog', 'block 2', 'ImageSrc')
        blockThreeImgSrc = try_get_row_data(data, 'Blog', 'block 3', 'ImageSrc')
        BlockOneLink = try_get_row_data(data, 'Blog', 'block 1', 'Link')
        BlockTwoLink = try_get_row_data(data, 'Blog', 'block 2', 'Link')
        BlockThreeLink = try_get_row_data(data, 'Blog', 'block 3', 'Link')
        # replace data
        file_data = file_data.replace('[Blog_Headline]', Headline)
        file_data = file_data.replace('[Blog_Block_1_Text]', blockOneButtonText)
        file_data = file_data.replace('[Blog_Block_2_Text]', blockTwoButtonText)
        file_data = file_data.replace('[Blog_Block_3_Text]', blockThreeButtonText)
        file_data = file_data.replace('[Blog_Block_1_Image_Source]', blockOneImgSrc)
        file_data = file_data.replace('[Blog_Block_2_Image_Source]', blockTwoImgSrc)
        file_data = file_data.replace('[Blog_Block_3_Image_Source]', blockThreeImgSrc)
        file_data = file_data.replace('[Blog_Block_1_Link]', BlockOneLink)
        file_data = file_data.replace('[Blog_Block_2_Link]', BlockTwoLink)
        file_data = file_data.replace('[Blog_Block_3_Link]', BlockThreeLink)
        # return data
        return file_data
### Run functions 
if __name__ == "__main__":
    data = get_json_data()
    html = get_html()
    main(data, html)
    scss_hero_content(data)