# Import libs
import json
from pathlib import Path
import os
###
path = Path.cwd()
absolute_path_ = (str(path))
absolute_path_ = absolute_path_
os.makedirs(Path(absolute_path_).joinpath('production'), exist_ok=True)
scss_template = absolute_path_ + '//templates//template.scss'
html_blocks = absolute_path_ + '//templates//html//blocks//block.html'
html_blog_blocks = absolute_path_ + '//templates//html//blocks//blog_block.html'
html_production = absolute_path_ + '//production//index.html'
scss_production = absolute_path_ + '//production//UK.scss'
def get_json_data():
    try:
        with open('resources/data.json') as json_file:
            data = json.load(json_file)
        return data
    except:
        return None
###
def get_blocks():
    with open(html_blocks, 'r') as file:
        block_data = file.read()
    return block_data
###
def get_blog_blocks():
    with open(html_blog_blocks, 'r') as file:
        blog_block_data = file.read()
    return blog_block_data
###
def try_get_data(data, a, b):
    try:
        return data[a][b]
    except KeyError:
        return "An error occured"
###
def try_get_row_data(data, a, b, c):
    try:
        return data[a][b][c]
    except KeyError:
        return "An error occured"
### END ###
### HERO SASS ###
def scss_hero_full_bleed(data):
    scss_full_bleed = absolute_path_ + "/templates/scss/hero_full_bleed.scss"
    try:
        with open(scss_full_bleed, 'r') as file:
            file_data = file.read()
            # get data
            heroImageOne = try_get_data(data, 'Hero', 'Image_One')
            # data replace
            file_data = file_data.replace('[Hero_Image_One]', heroImageOne)
            # build sass
        return file_data
    except TypeError:
        pass
###
def scss_hero_2_col(data):
    scss_2_col = absolute_path_ + "/templates/scss/hero_2_col.scss"
    try:
        with open(scss_2_col, 'r') as file:
            file_data = file.read()
            # get data
            heroImageOne = try_get_data(data, 'Hero', 'Image_One')
            heroImageTwo = try_get_data(data, 'Hero', 'Image_Two')
            # data replace
            file_data = file_data.replace('[Hero_Image_One]', heroImageOne)
            file_data = file_data.replace('[Hero_Image_Two]', heroImageTwo)
            # build sass
        return file_data
    except TypeError:
        pass
###
def scss_hero_2_split_right(data):
    scss_2_col = absolute_path_ + "/templates/scss/hero_2_split_right.scss"
    try:
        with open(scss_2_col, 'r') as file:
            file_data = file.read()
            # get data
            heroImageOne = try_get_data(data, 'Hero', 'Image_One')
            heroImageTwo = try_get_data(data, 'Hero', 'Image_Two')
            # data replace
            file_data = file_data.replace('[Hero_Image_One]', heroImageOne)
            file_data = file_data.replace('[Hero_Image_Two]', heroImageTwo)
            # build sass
        return file_data
    except TypeError:
        pass
###
def scss_hero_3_col(data):
    scss_3_col = absolute_path_ + "/templates/scss/hero_3_col.scss"
    try:
        with open(scss_3_col, 'r') as file:
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
        return file_data
    except TypeError:
        pass
### END ###
def select_scss_hero(data):
    hero_type = data['Hero']['Type']
    if "HERO" in hero_type:
        if "HERO - FULL BLEED".upper() in hero_type:
            scss_content = scss_hero_full_bleed(data)
            return scss_content
        if "HERO - 2 COL".upper() in hero_type:
            scss_content = scss_hero_2_col(data)
            return scss_content
        if "HERO - 2 SPLIT RIGHT".upper() in hero_type:
            scss_content = scss_hero_2_split_right(data)
            return scss_content
        if "HERO - 3 COL".upper() in hero_type:
            scss_content = scss_hero_3_col(data)
            return scss_content
### HTML STUFFS ###
def html_hero_content(data, content):
    with open(content, 'r') as file:
        file_data = file.read()
        # get data
        MainTitle = try_get_data(data, 'Hero', 'Main_Title')
        HeroHeadline = try_get_data(data, 'Hero', 'Headline')
        heroButtonText = try_get_data(data, 'Hero', 'Button_Text')
        heroLink = try_get_data(data, 'Hero', 'Link')
        # data replace
        file_data = file_data.replace('[Main_Title]', MainTitle)
        file_data = file_data.replace('[Hero_Headline]', HeroHeadline)
        file_data = file_data.replace('[Hero_Button_Text]', heroButtonText)
        file_data = file_data.replace('[Hero_Link]', heroLink)
    return file_data
###
def select_html_hero(data):
    hero_type = data['Hero']['Type']
    if "HERO" in hero_type:
        if "HERO - FULL BLEED".upper() in hero_type:
            html_full_bleed = absolute_path_ + "/templates/html/hero/hero_full_bleed.html"
            html_content = html_hero_content(data, html_full_bleed)
            return html_content
        if "HERO - 2 COL".upper() in hero_type:
            html_2_col = absolute_path_ + "/templates/html/hero/hero_2_col.html"
            html_content = html_hero_content(data, html_2_col)
            return html_content
        if "HERO - 2 SPLIT RIGHT".upper() in hero_type:
            html_2_col = absolute_path_ + "/templates/html/hero/hero_2_split_right.html"
            html_content = html_hero_content(data, html_2_col)
            return html_content
        if "HERO - 3 COL".upper() in hero_type:
            html_3_col = absolute_path_ + "/templates/html/hero/hero_3_col.html"
            html_content = html_hero_content(data, html_3_col)
            return html_content
###
def html_browse_gifts_content(data, block_data):
    #pass html through parameter 
    count = try_get_data(data, 'Browse_Gifts', 'count')
    with open(absolute_path_ + '//templates//html//carousels//browse_carousel.html') as file:
        file_data = file.read()
    carousel_pop_data = ''
    Headline = try_get_data(data, 'Browse_Gifts', 'Headline')
    file_data = file_data.replace('[Browse_Gifts_Headline]', Headline)
    for i in range(count):
        i+=1
        block_data = block_data.replace(f'[Carousel_Block_{i-1}_Text]', f'[Carousel_Block_{i}_Text]')
        block_data = block_data.replace(f'[Carousel_Block_{i-1}_Link]', f'[Carousel_Block_{i}_Link]')
        block_data = block_data.replace(f'[Carousel_Block_{i-1}_Image_Source]', f'[Carousel_Block_{i}_Image_Source]')
        carousel_empty_data = block_data
        blockButtonText = try_get_row_data(data, 'Browse_Gifts', f'block {i}', 'Button_Text')    
        blockButtonLink = try_get_row_data(data, 'Browse_Gifts', f'block {i}', 'Link')    
        blockButtonImgSrc = try_get_row_data(data, 'Browse_Gifts', f'block {i}', 'ImageSrc')    
        carousel_empty_data = carousel_empty_data.replace(f'[Carousel_Block_{i}_Text]', blockButtonText)
        carousel_empty_data = carousel_empty_data.replace(f'[Carousel_Block_{i}_Link]', blockButtonLink)
        carousel_empty_data = carousel_empty_data.replace(f'[Carousel_Block_{i}_Image_Source]', blockButtonImgSrc)
        carousel_pop_data += carousel_empty_data
    file_data = file_data.replace('[Browse_Gifts_Carousel_Row]', carousel_pop_data)
    return file_data
###
def html_popular_categories_content(data):
    #pass html through parameter 
    with open(absolute_path_ + '//templates//html//misc//Popular_Categories.html') as file:
        file_data = file.read()
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
def html_gifts_under_twenty_content(data, block_data):
    count = try_get_data(data, 'Gifts_Under_20', 'count')
    with open(absolute_path_ + '//templates//html//carousels//gifts_under_20_carousel.html') as file:
        file_data = file.read()
    carousel_pop_data = ''
    Headline = try_get_data(data, 'Gifts_Under_20', 'Headline')
    ButtonText = try_get_data(data, 'Gifts_Under_20', 'Button_Text')
    ButtonLink = try_get_data(data, 'Gifts_Under_20', 'Link')
    #replace data
    file_data = file_data.replace('[Gifts_Under_20_Headline]', Headline)
    file_data = file_data.replace('[Gifts_Under_20_Button_Text]', ButtonText)
    file_data = file_data.replace('[Gifts_Under_20_Button_Link]', ButtonLink)
    for i in range(count):
        i+=1
        block_data = block_data.replace(f'[Carousel_Block_{i-1}_Text]', f'[Carousel_Block_{i}_Text]')
        block_data = block_data.replace(f'[Carousel_Block_{i-1}_Link]', f'[Carousel_Block_{i}_Link]')
        block_data = block_data.replace(f'[Carousel_Block_{i-1}_Image_Source]', f'[Carousel_Block_{i}_Image_Source]')
        carousel_empty_data = block_data
        blockButtonText = try_get_row_data(data, 'Gifts_Under_20', f'block {i}', 'Button_Text')    
        blockButtonLink = try_get_row_data(data, 'Gifts_Under_20', f'block {i}', 'Link')    
        blockButtonImgSrc = try_get_row_data(data, 'Gifts_Under_20', f'block {i}', 'ImageSrc')    
        carousel_empty_data = carousel_empty_data.replace(f'[Carousel_Block_{i}_Text]', blockButtonText)
        carousel_empty_data = carousel_empty_data.replace(f'[Carousel_Block_{i}_Link]', blockButtonLink)
        carousel_empty_data = carousel_empty_data.replace(f'[Carousel_Block_{i}_Image_Source]', blockButtonImgSrc)
        carousel_pop_data += carousel_empty_data
    file_data = file_data.replace('[Gifts_Under_20_Carousel_Row]', carousel_pop_data)
    # return data
    return file_data
###
def html_gifts_under_forty_content(data, block_data):
    count = try_get_data(data, 'Gifts_Under_40', 'count')
    with open(absolute_path_ + '//templates//html//carousels//gifts_under_40_carousel.html') as file:
        file_data = file.read()
    carousel_pop_data = ''
    Headline = try_get_data(data, 'Gifts_Under_40', 'Headline')
    ButtonText = try_get_data(data, 'Gifts_Under_40', 'Button_Text')
    ButtonLink = try_get_data(data, 'Gifts_Under_40', 'Link')
    #replace data
    file_data = file_data.replace('[Gifts_Under_40_Headline]', Headline)
    file_data = file_data.replace('[Gifts_Under_40_Button_Text]', ButtonText)
    file_data = file_data.replace('[Gifts_Under_40_Button_Link]', ButtonLink)
    for i in range(count):
        i+=1
        block_data = block_data.replace(f'[Carousel_Block_{i-1}_Text]', f'[Carousel_Block_{i}_Text]')
        block_data = block_data.replace(f'[Carousel_Block_{i-1}_Link]', f'[Carousel_Block_{i}_Link]')
        block_data = block_data.replace(f'[Carousel_Block_{i-1}_Image_Source]', f'[Carousel_Block_{i}_Image_Source]')
        carousel_empty_data = block_data
        blockButtonText = try_get_row_data(data, 'Gifts_Under_40', f'block {i}', 'Button_Text')    
        blockButtonLink = try_get_row_data(data, 'Gifts_Under_40', f'block {i}', 'Link')    
        blockButtonImgSrc = try_get_row_data(data, 'Gifts_Under_40', f'block {i}', 'ImageSrc')    
        carousel_empty_data = carousel_empty_data.replace(f'[Carousel_Block_{i}_Text]', blockButtonText)
        carousel_empty_data = carousel_empty_data.replace(f'[Carousel_Block_{i}_Link]', blockButtonLink)
        carousel_empty_data = carousel_empty_data.replace(f'[Carousel_Block_{i}_Image_Source]', blockButtonImgSrc)
        carousel_pop_data += carousel_empty_data
    file_data = file_data.replace('[Gifts_Under_40_Carousel_Row]', carousel_pop_data)
    # return data
    return file_data
###
def html_inspiration_content(data, block_data):
    #pass html through parameter 
    count = try_get_data(data, 'Inspiration', 'count')
    with open(absolute_path_ + '//templates//html//carousels//inspiration_carousel.html') as file:
        file_data = file.read()
    carousel_pop_data = ''
    Headline = try_get_data(data, 'Inspiration', 'Headline')
    file_data = file_data.replace('[Inspiration_Headline]', Headline)
    for i in range(count):
        i+=1
        block_data = block_data.replace(f'[Carousel_Block_{i-1}_Text]', f'[Carousel_Block_{i}_Text]')
        block_data = block_data.replace(f'[Carousel_Block_{i-1}_Link]', f'[Carousel_Block_{i}_Link]')
        block_data = block_data.replace(f'[Carousel_Block_{i-1}_Image_Source]', f'[Carousel_Block_{i}_Image_Source]')
        carousel_empty_data = block_data
        blockButtonText = try_get_row_data(data, 'Inspiration', f'block {i}', 'Button_Text')    
        blockButtonLink = try_get_row_data(data, 'Inspiration', f'block {i}', 'Link')    
        blockButtonImgSrc = try_get_row_data(data, 'Inspiration', f'block {i}', 'ImageSrc')    
        carousel_empty_data = carousel_empty_data.replace(f'[Carousel_Block_{i}_Text]', blockButtonText)
        carousel_empty_data = carousel_empty_data.replace(f'[Carousel_Block_{i}_Link]', blockButtonLink)
        carousel_empty_data = carousel_empty_data.replace(f'[Carousel_Block_{i}_Image_Source]', blockButtonImgSrc)
        carousel_pop_data += carousel_empty_data
    file_data = file_data.replace('[Inspiration_Carousel_Row]', carousel_pop_data)
    return file_data
###
def html_blog_content(data, blog_block_data):
    #pass html through parameter 
    count = try_get_data(data, 'Blog', 'count')
    with open(absolute_path_ + '//templates//html//carousels//blog_row.html') as file:
        file_data = file.read()
    carousel_pop_data = ''
    Headline = try_get_data(data, 'Blog', 'Headline')
    file_data = file_data.replace('[Blog_Headline]', Headline)
    for i in range(count):
        i+=1
        blog_block_data = blog_block_data.replace(f'[Carousel_Block_{i-1}_Text]', f'[Carousel_Block_{i}_Text]')
        blog_block_data = blog_block_data.replace(f'[Carousel_Block_{i-1}_Link]', f'[Carousel_Block_{i}_Link]')
        blog_block_data = blog_block_data.replace(f'[Carousel_Block_{i-1}_Image_Source]', f'[Carousel_Block_{i}_Image_Source]')
        carousel_empty_data = blog_block_data
        blockButtonText = try_get_row_data(data, 'Blog', f'block {i}', 'text')    
        blockButtonLink = try_get_row_data(data, 'Blog', f'block {i}', 'Link')    
        blockButtonImgSrc = try_get_row_data(data, 'Blog', f'block {i}', 'ImageSrc')    
        carousel_empty_data = carousel_empty_data.replace(f'[Carousel_Block_{i}_Text]', blockButtonText)
        carousel_empty_data = carousel_empty_data.replace(f'[Carousel_Block_{i}_Link]', blockButtonLink)
        carousel_empty_data = carousel_empty_data.replace(f'[Carousel_Block_{i}_Image_Source]', blockButtonImgSrc)
        carousel_pop_data += carousel_empty_data
    file_data = file_data.replace('[Blog_Carousel_Row]', carousel_pop_data)
    return file_data
### Run functions 
def main():
    with open(scss_template) as file:
        sass_file = file.read()
        sass_file = sass_file.replace('[Hero]', output_sass)
        with open(scss_production, 'w') as scss_file_prod:
            scss_file_prod.write(sass_file)    
    asd = select_html_hero(data) + html_browse_gifts_content(data, block_data) + html_popular_categories_content(data) + html_gifts_under_twenty_content(data, block_data) + html_gifts_under_forty_content(data, block_data) + html_inspiration_content(data, block_data) + html_blog_content(data, blog_block_data)
    with open(html_production, 'w') as html_file:
        html_file.write(asd)
### function vars ###
data = get_json_data()
block_data = get_blocks()
blog_block_data = get_blog_blocks()
output_sass = select_scss_hero(data)
###
print('building page...')
if __name__ == "__main__":
    main()