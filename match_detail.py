# wrapper
import re
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class match:
    def __init__(self, match):
        self.match = match
        self.gamestats = match.find_elements_by_class_name("GameStats")[0]
        self.gamesetting = match.find_elements_by_class_name("GameSettingInfo")[0]
        self.playerstats = match.find_elements_by_class_name("Stats")[0]
        self.kda = match.find_elements_by_class_name('KDA')[0]

        # expanded menu
        # self.gamedetail = match.find_elements_by_class_name('GameDetailTableWrap')[0]
    
    # stats before clicking downarrow
    def self_stats(self):
        # game stats information block
        queue_type = class_content(self.gamestats, "GameType")
        is_win = class_content(self.gamestats, "GameResult") == 'Victory'
        game_length = class_content(self.gamestats, "GameLength")
        game_time = class_content_search(self.gamestats, ["TimeStamp", "_timeago"])

        # game setting information block
        champion_played_wrapper = self.gamesetting.find_elements_by_class_name("ChampionName")[0]
        champion_played = a_textcontent(champion_played_wrapper)
        # +runes

        # game stats information block
        level = class_content(self.playerstats, "Level")
        cs_wrapper = class_content_search(self.playerstats, ["CS", "tip"])
        cs_per_min = cs_wrapper[cs_wrapper.find("(")+1:cs_wrapper.find(")")]
        cs_raw = cs_wrapper.replace('(' + cs_per_min + ')', '')

        pkill = class_content(self.playerstats, "CKRate")

        mmr_wrapper = self.playerstats.find_elements_by_class_name("MMR")[0]
        mmr = mmr_wrapper.find_elements_by_tag_name('b')[0].get_attribute('innerHTML')

        # kda stats information block
        kill_count = class_content_search(self.kda, ["KDA", "Kill"])
        assist_count = class_content_search(self.kda, ["KDA", "Assist"])
        death_count = class_content_search(self.kda, ["KDA", "Death"])
        kda_ratio = class_content_search(self.kda, ["KDARatio", "KDARatio"])

        # +items
        # +player names

        return {
            'win': is_win,
            'queue_type': queue_type.strip(),
            'time': game_time,
            'length': game_length,
            'player': {
                'champion_played': champion_played,
            },
            'gameplay': {
                'level': level.strip(),
                'cs' : cs_raw.strip(),
                'cs_per_min': cs_per_min,
                'pkill' : pkill.strip(),
                'build': [],
                'kda': {
                    'overall': kda_ratio,
                    'kill': kill_count,
                    'death': death_count,
                    'assist': assist_count
                },
                'tieravg': mmr
            }        
        }

    def player_stats(self, username):
        # click expand button
        link = self.match.find_element_by_id('right_match')
        link.click()

        # wait until detaillayout is expanded
        WebDriverWait(self.match, 10).until(
            EC.presence_of_element_located((
            By.CLASS_NAME, "MatchDetailLayout")))

        # extraction logic
        matchdetail = self.match.find_elements_by_class_name("MatchDetailLayout")[0]

        # find username row
        head = matchdetail.find_element(By.PARTIAL_LINK_TEXT, username)

        # find row container from username row
        parent = head.find_element_by_xpath('../..')

        # data from row container
        champion_played = class_content_search(parent, ["ChampionImage", "Image"])
        level = class_content_search(parent, ["ChampionImage", "Level"])
        elo = class_content(parent, "Tier")

        opscore = class_content_search(parent, ["OPScore", "Text"])
        opscore_rank = class_content_search(parent, ["OPScore", "Badge"])

        kda_ratio = class_content_search(parent, ["KDA", "KDARatio"])
        kill = class_content_search(parent, ["KDA", "Kill"])
        assist = class_content_search(parent, ["KDA", "Death"])
        death = class_content_search(parent, ["KDA", "Assist"])
        
        pkill = class_content_search(parent, ["KDA", "CKRate"])

        damage = class_content_search(parent, ["Damage", "ChampionDamage"])

        ward = parent.find_elements_by_class_name("Ward")[0]
        ward_title = ward.get_attribute('title').split('<br>')
        control = remove_nonnumerical(ward_title[0])
        placed = remove_nonnumerical(ward_title[1])
        destroyed = remove_nonnumerical(ward_title[2])

        cs = class_content_search(parent, ["CS", "CS"])
        cs_per_min = class_content_search(parent, ["CS", "CSPerMinute"]).replace('/m', '')

        # look in header for game status
        header_wrapper = parent.find_element_by_xpath('../..').find_elements_by_class_name("Header")[0]
        is_victory = class_content_search(header_wrapper, ["Row","HeaderCell", "GameResult"])

        return {
            'username': username,
            'win': is_victory,
            'player': {
                'elo': remove_spaces(elo),
                'champion_played': champion_played,
                'rank': opscore_rank, # mvp, 2nd, 3rd (...)
                'opscore': opscore,
            },
            'gameplay': {
                'level': level,
                'cs' : cs,
                'cs_per_min': cs_per_min,
                'pkill' : pkill,
                'build': [],
                'kda': {
                    'overall': kda_ratio,
                    'kill': kill,
                    'death': death,
                    'assist': assist
                },
                'damage': damage,
                'wards': {
                    'control': control,
                    'total': placed,
                    'destroyed': destroyed
                }
            }        
        }

    def overview(self):
        blue_team = {}
        red_team = {
            'players': [],
            'queue_type': 'rankedsolo',
            'objective_count': {
                'baron': 0,
                'dragon': 1,
                'tower': 5
            },
            'totalkill': 20,
            'totalgold': 20000
        }

        # run player_stats() for each player
        return {
            'blue': blue_team,
            'red' : red_team,
            'tier_avg': 'g5',
        }

    # player stats
    def build(self):
        item = [
            ('0 min', ['potion', 'dorans', 'ward']),
            ('5 min', ['potion', 'dorans', 'ward']),
            # extract all -min items
        ]
        skill = [
            ('1', 'Q')
            ('2', 'W')
            # extract all (order, ability)
            ('16', 'R')
        ]
        runes = {
            'sorcery': [],
            'domination': [],
            'runestats': []
        }

        return {
            'item': item,
            'skill': skill,
            'runes': runes
        }

# helper functions

# extract first element content (by class)
def class_content(parent, className):
    first_element = parent.find_elements_by_class_name(className)[0]
    return first_element.get_attribute('innerHTML')
def a_textcontent(parent):
    first_element = parent.find_elements_by_tag_name('a')[0]
    return first_element.get_attribute('innerHTML')

# classList is [firstClassToFind, secondClassToFind, etc.]
def class_content_search(parent, classList):
    head = parent
    while classList:
        head = head.find_elements_by_class_name(classList[0])[0]
        classList.pop(0)
    return head.get_attribute('innerHTML')

def remove_spaces(inp):
    return "".join(inp.split())

def remove_nonnumerical(inp):
    return re.sub("[^0-9]", "", inp)
    