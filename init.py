import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains


# get initial html
summonerName = 'API'
driverpath = os.path.realpath(r'drivers/chromedriver')
chrome_options = Options()  
chrome_options.add_argument("--headless")  

driver = webdriver.Chrome(driverpath, options=chrome_options)
driver.get('https://na.op.gg/summoner/userName=' + summonerName)

print(driver.page_source)