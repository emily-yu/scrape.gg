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

# block [1] get last updated time for checking updated click for button
a = driver.find_elements_by_class_name("LastUpdate")
print(a[0].text)

updatebutton = driver.find_elements_by_id("SummonerRefreshButton")[0]
ActionChains(driver).click(updatebutton).perform()
# WebDriverWait(driver, 15).until(a != driver.find_elements_by_class_name("LastUpdate")[0].text)
WebDriverWait(driver, 10).until(
    lambda wd: a == driver.find_elements_by_class_name("LastUpdate")[0].text
)

# verify that [1] has changed
b = driver.find_elements_by_class_name("LastUpdate")
print(b[0].text)
print('driver update successful: ', a == b)