from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
starturl = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('./chromedriver.exe')
browser.get(starturl)
time.sleep(10)
def scrape():
    headers =['V_Mag',"Proper _name","Bayer_designation",'Distance','Spectral class','Mass','Radius','Luminosity']
    planet_data = []
    for i in range(0,439):
        soup = BeautifulSoup(browser.page_source,'html.parser')
        for ultag in soup.find_all('ul',attrs = {'class','exoplanet'}):
            litags = ultag.find_all('li')
            templist = []
            for index,litag in enumerate(litags):
                if index == 0:
                    templist.append(litag.find_all('a')[0].contents[0])
                else:
                    try:
                        templist.append(litag.contents[0])
                    except:
                        templist.append('')
            planet_data.append(templist)
        browser.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table/thead/tr/th[2]').click()
    with open('scrapper3.csv','w')as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()        



