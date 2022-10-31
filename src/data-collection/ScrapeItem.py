from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re

def scrape_item(url):

    chrome_options = Options()
    chrome_options.headless = True
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)

    try:
        name_el = driver.find_element(By.CSS_SELECTOR, "#itemTitle")
        name = name_el.get_attribute("innerText")[16:]
    except:
        name = ""

    try:
        condition_el = driver.find_element(By.CSS_SELECTOR, ".condText")
        condition = condition_el.get_attribute("innerText")
    except:
        condition = ""


    try:
        end_date_el = driver.find_element(By.CSS_SELECTOR, "#bb_tlft")
        end_date = re.sub("/[\n\t\r]/g","",end_date_el.get_attribute("innerText"))
    except: 
        end_date = -1


    try:
        postage_el = driver.find_element(By.CSS_SELECTOR, "#fshippingCost")
        postage = postage_el.get_attribute("innerText")
    except:
        postage = -1



    try:
        price_el = driver.find_element(By.CSS_SELECTOR, ".vi-VR-cvipPrice")
        price = price_el.get_attribute("innerText")
    except:
        price = -1


    try:
        bids_el = driver.find_element(By.CSS_SELECTOR, "#vi-VR-bid-lnk- > span:first-child")
        bids = bids_el.get_attribute("innerText")
    except:
        bids = -1
        

    driver.quit()

    item = {
        'name': name,
        'condition': condition,
        'end_date': end_date,
        'postage': postage,
        'price': price,
        'bids': bids
    }

    return item


    