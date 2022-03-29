
# web-scraping-challenge
HW # 12 Web Scraping- Mission to Mars

Summary
This assignment demonstrates the use of Splinter and BeautifulSoup to build a web application that scrapes 4 websites collecting data related to the Mission to Mars. The data is then displayed on an HTML for easier viewiing.

Data
NASA Mars News: https://redplanetscience.com/
JPL Mars Space Images: https://spaceimages-mars.com)
Mars Facts: https://galaxyfacts-mars.com
Mars Hemispheres: https://marshemispheres.com/

Part 1:
Completed initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter for the 4 websites. Collected the latest news title and paragraph text, a featured space image, a table containing facts about the planet, and images for each of Mar's hemispheres.

File: mission_to_mars.ipynb

Part 2:
Used MondgoDB with Flask to create a new HTML page that displays all of the data scraped. This was done by converting the Jupyter notebook into a python script called "scrape_mars.py". Then created an "app.py" python script with "/scrape" route that calls a "scrape" function. The root route queries the Mongo database and passes the data into an HTML template,"index.html", to display the data as the final web page product shown below. 


![Screen Shot_FinalAppWebBrowser](https://user-images.githubusercontent.com/94502554/160531255-bd058f71-9491-4e30-9704-231edd25ffe8.png),
