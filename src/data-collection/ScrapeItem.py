from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def ScrapeItem(url):

    chrome_options = Options()
    chrome_options.headless = True
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)


    try:
        price_el = driver.find_element(By.CSS_SELECTOR, ".vi-VR-cvipPrice")
        price = price_el.get_attribute("innerText")
    except:
        price = -2


    try:
        bids_el = driver.find_element(By.CSS_SELECTOR, "#vi-VR-bid-lnk- > span:first-child")
        bids = bids_el.get_attribute("innerText")
    except:
        bids = -2
        

    driver.quit()

    return (price, bids)

ScrapeItem('https://www.ebay.com/itm/374328760872')