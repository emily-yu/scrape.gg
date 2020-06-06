import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

from profile_detail import profile
from match_detail import match

class scrape:
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

init = scrape('API') # driver

# test match api class
recent = init.getMatch(1)
# second = init.getMatch(2)
# top10 = init.getMatchSequence(10)

# match class tests
print(recent.game_player_names(True)) # stable
print(recent.self_stats()) # stable
print(recent.player_stats('API')) # stable
print(recent.overview())
print(recent.build())

# profile details class
profile = init.getProfile() # stable
print(profile.recently_played_with()) # stable
print(profile.queue_stats('Total')) # stable
# print(profile.top_played_champions())
# print(profile.rank())

# {'winner': {'API': 'Vladimir', 'Champagnè': 'Volibear', 'RANGED TOP LANER': 'Tristana', 'jspostbox': 'Vayne', 'Azailas': 'LeBlanc'}, 'loser': {'bladdee': 'Kindred', 'Nëver One': 'Elise', 'Derpcon4': 'Nocturne', 'AstVoid': "Kai'Sa", 'Electric Zoom': 'Senna'}}
# {'win': False, 'queue_type': 'Normal', 'time': '4 days ago', 'length': '31m 12s', 'players': {'champion_played': 'Vladimir', 'winner': {'bladdee': 'Kindred', 'Nëver One': 'Elise', 'Derpcon4': 'Nocturne', 'AstVoid': "Kai'Sa", 'Electric Zoom': 'Senna'}, 'loser': {'API': 'Vladimir', 'Champagnè': 'Volibear', 'RANGED TOP LANER': 'Tristana', 'jspostbox': 'Vayne', 'Azailas': 'LeBlanc'}}, 'gameplay': {'level': 'Level15', 'cs': '193', 'cs_per_min': '6.2', 'pkill': 'P/Kill 50%', 'build': [], 'kda': {'overall': '1.44:1', 'kill': '8', 'death': '9', 'assist': '5'}, 'tieravg': 'N/A'}}
# {'username': 'API', 'win': '\n\t\t\t\t\t\t\t\t\tDefeat\t\t\t\t\t\t\t\t', 'player': {'elo': 'Platinum2', 'champion_played': 'Vladimir', 'rank': 'ACE', 'opscore': '6.3'}, 'gameplay': {'level': '15', 'cs': '193', 'cs_per_min': '6.2', 'pkill': '(50%)', 'build': [], 'kda': {'overall': '1.44:1', 'kill': '8', 'death': '5', 'assist': '9'}, 'damage': '23,520', 'wards': {'control': '0', 'total': '8', 'destroyed': '1'}}}
# {'players': {'winner': {'bladdee': 'Kindred', 'Nëver One': 'Elise', 'Derpcon4': 'Nocturne', 'AstVoid': "Kai'Sa", 'Electric Zoom': 'Senna'}, 'loser': {'API': 'Vladimir', 'Champagnè': 'Volibear', 'RANGED TOP LANER': 'Tristana', 'jspostbox': 'Vayne', 'Azailas': 'LeBlanc'}}, 'player_stats': {'team': 'Blue Team', 'result': 'Defeat'}, 'blue': {'kill': '39', 'gold': '62209', 'objectives': {'baron': '0', 'dragon': '1', 'tower': '2'}}, 'red': {'kill': '26', 'gold': '52037', 'objectives': {'baron': '1', 'dragon': '4', 'tower': '8'}}}
# {'item': {'0 min': ['033_Buckler', '2003_Health_Potion', '3350_GreaterYellowTrinket'], '3 min': ['1052_Amplifying_Scepter', '2031_Refillable_Potion'], '8 min': ['3145_Hextech_Revolver', '3067_Kindlegem'], '10 min': ['3152_Hextech_Rocket_Belt', '3020_Flamewalkers'], '14 min': ['1058_Needlessly_Large_Wand'], '15 min': ['3113_Aether_Wisp'], '17 min': ['3907'], '20 min': ['2031_Refillable_Potion', '113_Tome_of_Minor_Necro_Compulsion'], '24 min': ['1058_Needlessly_Large_Wand', '033_Buckler', '2420'], '26 min': ['3363_OracleRedTrinket'], '27 min': ['3157_Zhonyas_Hourglass']}, 'skill': {'Q': ['1', '4', '5', '7', '9'], 'W': ['3', '14', '15'], 'E': ['2', '8', '10', '12', '13'], 'R': ['6', '11']}, 'runes': ['Phase Rush', 'Nimbus Cloak', 'Transcendence', 'Gathering Storm', 'Magical Footwear', 'Cosmic Insight']}
# {'1': {'username': 'ithrowshoesatyou', 'played': '5', 'win': '3', 'lose': '2', 'ratio': '60%'}}
# {'type': 'Total', 'win': '7', 'loss': '3', 'kda': {'overall': '2.75:1', 'kill': '6.8', 'assist': '8.6', 'death': '5.6'}, 'pkill': '(<span>52%</span>)', 'top3champions': {'Rumble': {'winratio': '67%', 'kda': {'overall': '3.58', 'win': '2', 'lose': '1'}}, 'Syndra': {'winratio': '50%', 'kda': {'overall': '2.45', 'win': '1', 'lose': '1'}}, 'Ezreal': {'winratio': '100%', 'kda': {'overall': '5.25', 'win': '1', 'lose': '0'}}}, 'preferred': [{'role': 'Middle', 'rolerate': '43', 'winrate': '67'}, {'role': 'Top', 'rolerate': '29', 'winrate': '50'}]}