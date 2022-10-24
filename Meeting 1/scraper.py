from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.headless = True
driver = webdriver.Chrome(options=chrome_options)

start_url = "https://www.wikipedia.org"
driver.get(start_url)

search_el = driver.find_element("name", "search")
search_el.send_keys("War")

driver.find_element_by_css_selector('button[type=submit]').click()

driver.save_screenshot("image.png")

driver.quit()