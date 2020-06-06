import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

from profile_detail import profile
from match_detail import match

class scrapegg:
    def __init__(self, summonerName):
        self.driver = self.initDriver(summonerName) # source if want to write custom functions
        self.summonerName = summonerName

    # import from init file
    def initDriver(self, summonerName):
        # get initial html
        driverpath = os.path.realpath(r'../drivers/chromedriver')
        chrome_options = Options()  
        # chrome_options.add_argument("--headless")  

        driver = webdriver.Chrome(driverpath, options=chrome_options)
        driver.get('https://na.op.gg/summoner/userName=' + summonerName)

        return driver

    def getProfile(self):
        return profile(self.driver)
    
    # get data for user-defined amount of matches (count)
    def getMatchSequence(self, count):
        expansions = 0
        while (count > 10):
            self.showMoreMatches()
            print('click expansion', count)
            count -= 10
            expansions += 1
        res = []
        for match_play in self.driver.find_elements_by_class_name("GameItemWrap"):
            res.append(match(match_play, self.summonerName))
            if len(res) == count + (10 * expansions):
                return res
    # expand match list (use in getMatchSequence, getMatch)
    def showMoreMatches(self):
        # find number initial elements
        a = self.driver.find_elements_by_class_name("GameItemWrap")

        link = self.driver.find_element_by_link_text('Show More')
        link.click()

        WebDriverWait(self.driver, 10).until(
            lambda wd: len(a) < len(self.driver.find_elements_by_class_name("GameItemWrap"))
        )

    # get individual match, x most recent
    def getMatch(self, count):
        expansions = 0
        while (count > 10):
            self.showMoreMatches()
            print('click expansion', count)
            count -= 10
            expansions += 1
        return match(self.driver.find_elements_by_class_name("GameItemWrap")[count], self.summonerName)
    
    # close driver
    def quit(self):
        self.driver.quit()
        return True