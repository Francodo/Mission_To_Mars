import splinter, BeautifulSoup
 

from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt


def scrape_all():
    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)

    img_url1 = mars_cerberus_image(browser)
    img_url2 = mars_Schiaparelli_image(browser)
    img_url3 = mars_syrtis_major(browser)
    img_url4 =  mars_valles_marineris(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "img_url1": Cerberus_image,
        "img_url2": Schiaparelli_image,
        "img_url3": Syrtis_major,
        "img_url4": Valles_marineris,
        "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data


def mars_cerberus_image(browser):

    # Scrape Mars Hemisphere images
    # Visit the mars Nasa Hemisphere images site
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Convert the browser html to a image object and then quit the browser
    html = browser.html
    image_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = image_soup.select_one("ul.item_list li.slide")
        # Use the parent element to find the first 'a' tag and save it as 'image_title'
        image_title = slide_elem.find("div", class_="title").get_text()
        # Use the parent element to find the title in paragraph text
        cerberus_image = slide_elem.find("div", class_="wrapper").get_full_url()

    except AttributeError:
        return None, None

    return image_title, cerberus_image


def mars_Schiaparelli_image(browser):
    # Visit URL
    url ='https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Convert the browser html to a image object and then quit the browser
    html = browser.html
    image_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = image_soup.select_one("ul.item_list li.slide")
        # Use the parent element to find the first 'a' tag and save it as 'image_title'
        image_title = slide_elem.find("div", class_="title").get_text()
        # Use the parent element to find the title in paragraph text
        schiaparelli_image = slide_elem.find("div", class_="wrapper").get_full_url()

    except AttributeError:
        return None, None

    return image_title, schiaparelli_image



def mars_syrtis_major(browser):
    
    # Scrape Mars Hemisphere images
    # Visit the mars Nasa Hemisphere images site
    url ='https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced/'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Convert the browser html to a image object and then quit the browser
    html = browser.html
    image_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = image_soup.select_one("ul.item_list li.slide")
        # Use the parent element to find the first 'a' tag and save it as 'image_title'
        image_title = slide_elem.find("div", class_="title").get_text()
        # Use the parent element to find the title in paragraph text
        syrtis_major_image = slide_elem.find("div", class_="wide-image-wrapper").get_full_url()

    except AttributeError:
        return None, None

    return image_title, syrtis_major


def mars_valles_marineris(browser):
    
    # Scrape Mars Hemisphere images
    # Visit the mars Nasa Hemisphere images site
    url='https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced/'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Convert the browser html to a image object and then quit the browser
    html = browser.html
    image_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = image_soup.select_one("ul.item_list li.slide")
        # Use the parent element to find the first 'a' tag and save it as 'image_title'
        image_title = slide_elem.find("div", class_="title").get_text()
        # Use the parent element to find the title in paragraph text
        valles_marineris_image = slide_elem.find("div", class_="wide-image-wrapper").get_full_url()

    except AttributeError:
        return None, None

    return image_title, valles_marineris


def mars_pdread():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the image into a dataframe
        df = pd.read_html('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['image_url', 'title']
    df.set_index('image_url', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")

if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())