import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

from profile_detail import profile
from match_detail import match

import json # for testing

driver = 0
summonerName = 'API'
queryMode = 'Total' # 'Ranked Solo', 'Ranked Flex'/'Ranked Flex 5v5'
summonerData = {}

def initDriver():
    # get initial html
    driverpath = os.path.realpath(r'drivers/chromedriver')
    chrome_options = Options()  
    # chrome_options.add_argument("--headless")  

    driver = webdriver.Chrome(driverpath, options=chrome_options)
    driver.get('https://na.op.gg/summoner/userName=' + summonerName)

    return driver

# click 'Update Profile'
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

# click 'Show More Matches'
def showMoreMatches():
    # block [2] find number initial elements
    a = driver.find_elements_by_class_name("GameItemWrap")
    print(len(a))
    print(a)

    link = driver.find_element_by_link_text('Show More')
    link.click()

    # WebDriverWait(driver, 15).until(a != driver.find_elements_by_class_name("LastUpdate")[0].text)
    WebDriverWait(driver, 10).until(
        lambda wd: len(a) < len(driver.find_elements_by_class_name("GameItemWrap"))
    )

    # verify that [2] has changed
    print('driver update successful: ', len(a) < len(driver.find_elements_by_class_name("GameItemWrap")))

def getMatchDetail():
    curr = driver.find_elements_by_class_name("GameItemWrap")[0]
    return match(curr, summonerName)
    
driver = initDriver()
# print(driver.page_source)
# refreshFullProfile()
# showMoreMatches()

# test = getMatchDetail()
# print(json.dumps(test.self_stats(), indent=2))
# print(json.dumps(test.player_stats('Sevald'), indent=2))
# print(json.dumps(test.overview(), indent=2))
# print(json.dumps(test.build(), indent=2))

test = profile(driver)
print(json.dumps(test.queue_stats('Total'), indent=2))

driver.quit()