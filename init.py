import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

driver = 0
summonerName = 'API'

def initDriver():
    # get initial html
    driverpath = os.path.realpath(r'drivers/chromedriver')
    chrome_options = Options()  
    chrome_options.add_argument("--headless")  

    driver = webdriver.Chrome(driverpath, options=chrome_options)
    driver.get('https://na.op.gg/summoner/userName=' + summonerName)

    return driver

def refreshFullProfile():
    # block [1] get last updated time for checking updated click for button
    a = driver.find_elements_by_class_name("LastUpdate")
    print(a[0].text)

    updatebutton = driver.find_elements_by_id("SummonerRefreshButton")[0]
    ActionChains(driver).click(updatebutton).perform()
    # WebDriverWait(driver, 15).until(a != driver.find_elements_by_class_name("LastUpdate")[0].text)
    WebDriverWait(driver, 10).until(
        lambda wd: a != driver.find_elements_by_class_name("LastUpdate")[0].text
    )

    # verify that [1] has changed
    print('driver update successful: ', a == 'Last updated: a minute ago')

driver = initDriver()
print(driver.page_source)
refreshFullProfile()