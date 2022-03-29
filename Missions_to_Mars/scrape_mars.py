#Import splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
#import pandas as pd
import time
import datetime as dt

#scrape all function
def scrape_all():

    #Set up splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #get the information from the news page
    news_title, news_paragraph= scrape_news(browser)

    #build a dictionary using the information from the scrapes
    marsData= {
        "newsTitle":news_title,
        "newsParagraph":news_paragraph,
        "featuredImage": scrape_feature_img(browser),
        "facts": scrape_facts_page(browser),
        "hemispheres": scrape_hemispheres(browser),
        "lastUpdated": dt.datetime.now()
    }
    #stop the webdriver
    browser.quit()

    #display output
    return marsData

#scrape the NASA Mars News website
def scrape_news(browser):
    url = "https://redplanetscience.com/"
    browser.visit(url)
    
    #delay for loading page
    time.sleep(1)

    #Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    #collect the latest news title
    slide_elem=soup.select_one('div.list_text')
    news_t=slide_elem.find('div', class_='content_title').get_text()

    #collect paragraph text of latest news title
    news_p=slide_elem.find('div', class_='article_teaser_body').get_text()

    #return the title and paragraph
    return news_t, news_p

#scrape through the featured image page
def scrape_feature_img(browser):
    url = "https://spaceimages-mars.com"
    browser.visit(url)  

    #find and click the full image button
    full_image_link= browser.find_by_tag('button')[1]
    full_image_link.click()

    #Scrape image html page into Soup
    html=browser.html
    img_soup=bs(html,'html.parser')
  
    #delay for loading page
    time.sleep(1)

    #use base url to create the absolute url
    img_url_rel= img_soup.find('img', class_='fancybox-image').get('src')

    #use base url to create the absolute url
    featured_image_url= f'https://spaceimages-mars.com/{img_url_rel}'

    #return featured image url
    return featured_image_url

#scrape through the Mars Facts webpage
def scrape_facts_page(browser):
    #Visit the Mars Facts webpage
    url= 'https://galaxyfacts-mars.com/'
    browser.visit(url)

    #Scrape html page into Soup
    html=browser.html
    fact_soup=bs(html,'html.parser')

    #find the facts location
    factsLocation= fact_soup.find('div', class_="diagram mt-4")
    factTable=factsLocation.find('table')

    #create and empty string
    facts=" "

    #add text to the empty string then return
    facts += str(factTable)
    
    return facts

#scrape through the hemispheres pages
def scrape_hemispheres(browser):
    #Visit the astrogeology site for high resoltuion images
    url= 'https://marshemispheres.com/'
    browser.visit(url)

    #create a list to hold image urls and titles
    hemisphere_image_urls=[]

    #loop through links, click link, find sample anchor, return the href
    for i in range(4):
        hemisphereInfo={}
        browser.find_by_css('a.product-item img')[i].click()
        sample=browser.links.find_by_text('Sample').first
        hemisphereInfo['title']=browser.find_by_css('h2.title').text
        hemisphereInfo['img_url']=sample['href']
        
        #append hemisphere object to list
        hemisphere_image_urls.append(hemisphereInfo)
        
        browser.back()

    #retrun hemisphere urls with the titles
    return hemisphere_image_urls

if __name__ == "__main__":
    print(scrape_all())
