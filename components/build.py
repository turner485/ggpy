# Import libs
import json
from pathlib import Path
import os
#
path = Path.cwd()
absolute_path_ = (str(path))
absolute_path_ = absolute_path_
os.makedirs(Path(absolute_path_).joinpath('production'), exist_ok=True)
html_template = absolute_path_ + '//templates//template.html'
scss_template = absolute_path_ + '//templates//template.scss'
html_blocks = absolute_path_ + '//templates//html//blocks//block.html'
html_blog_blocks = absolute_path_ + '//templates//html//blocks//blog_block.html'
html_production = absolute_path_ + '//production//index.html'
scss_production = absolute_path_ + '//production//UK.scss'
###
def get_json_data():
    try:
        with open('resources/data.json') as json_file:
            data = json.load(json_file)
        return data
    except:
        return None
###
def get_html():
    with open(html_template, 'r') as file:
        file_data = file.read()
    return file_data
###
def get_blocks():
    with open(html_blocks, 'r') as file:
        block_data = file.read()
    return block_data
def get_blog_blocks():
    with open(html_blog_blocks, 'r') as file:
        blog_block_data = file.read()
    return blog_block_data
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
    file_data = html_browse_gifts_content(data, file_data, block_data)
    file_data = html_popular_categories_content(data, file_data)
    file_data = html_gifts_under_content(data, file_data, block_data)
    file_data = html_inspiration_content(data, file_data, block_data)
    file_data = html_blog_content(data, file_data, blog_block_data)
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
def html_browse_gifts_content(data, html, block_data):
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
    html = html.replace('[Browse_Gifts_Block]', file_data)
    return html
    
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
def html_gifts_under_content(data, html, block_data):
    count = try_get_data(data, 'Gifts_Under', 'count')
    with open(absolute_path_ + '//templates//html//carousels//gifts_under_carousel.html') as file:
        file_data = file.read()
    carousel_pop_data = ''

    Headline = try_get_data(data, 'Gifts_Under', 'Headline')
    ButtonText = try_get_data(data, 'Gifts_Under', 'Button_Text')
    ButtonLink = try_get_data(data, 'Gifts_Under', 'Link')
    
    #replace data
    file_data = file_data.replace('[Gifts_Under_Headline]', Headline)
    file_data = file_data.replace('[Gifts_Under_Button_Text]', ButtonText)
    file_data = file_data.replace('[Gifts_Under_Button_Link]', ButtonLink)
    
    for i in range(count):
        i+=1
        block_data = block_data.replace(f'[Carousel_Block_{i-1}_Text]', f'[Carousel_Block_{i}_Text]')
        block_data = block_data.replace(f'[Carousel_Block_{i-1}_Link]', f'[Carousel_Block_{i}_Link]')
        block_data = block_data.replace(f'[Carousel_Block_{i-1}_Image_Source]', f'[Carousel_Block_{i}_Image_Source]')

        carousel_empty_data = block_data

        blockButtonText = try_get_row_data(data, 'Gifts_Under', f'block {i}', 'Button_Text')    
        blockButtonLink = try_get_row_data(data, 'Gifts_Under', f'block {i}', 'Link')    
        blockButtonImgSrc = try_get_row_data(data, 'Gifts_Under', f'block {i}', 'ImageSrc')    
        carousel_empty_data = carousel_empty_data.replace(f'[Carousel_Block_{i}_Text]', blockButtonText)
        carousel_empty_data = carousel_empty_data.replace(f'[Carousel_Block_{i}_Link]', blockButtonLink)
        carousel_empty_data = carousel_empty_data.replace(f'[Carousel_Block_{i}_Image_Source]', blockButtonImgSrc)
        carousel_pop_data += carousel_empty_data

    file_data = file_data.replace('[Gifts_Under_Carousel_Row]', carousel_pop_data)
    html = html.replace('[Gifts_Under_Block]', file_data)

    # return data
    return html
###
def html_inspiration_content(data, html, block_data):
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
    html = html.replace('[Inspiration_Block]', file_data)
    return html
###
def html_blog_content(data, html, blog_block_data):
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
    html = html.replace('[Blog_Block]', file_data)
    return html
### Run functions 
if __name__ == "__main__":
    data = get_json_data()
    html = get_html()
    block_data = get_blocks()
    blog_block_data = get_blog_blocks()
    main(data, html)
    scss_hero_content(data)
