import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

from profile_detail import profile
import match_detail

class scrape:
    def __init__(self, summonerName):
        self.driver = self.initDriver(summonerName) # source if want to write custom functions

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
        # return initDriver()
    
    '''
    todo: implement in matches
    if match count > 10, click expansion for (count - 10) % 10 + 1 (if not equal 10, for remainder)
    '''
    # get data for user-defined amount of matches (count)
    def getMatchSequence(self, count):
        return [0 * count]
    
    # get individual match, x most recent
    def getMatch(self, count):
        return 0

init = scrape('API') # driver

# test match api class
recent = init.getMatch(1)
second = init.getMatch(2)
top10 = init.getMatchSequence(10)

# match class tests
# print(recent.game_player_names(True))
# print(recent.self_stats())
# print(recent.player_stats('API'))
# print(recent.overview())
# print(recent.build())

# profile details class
profile = init.getProfile()
print(profile.recently_played_with())
print(profile.queue_stats('Total'))
# print(profile.top_played_champions())
# print(profile.rank())