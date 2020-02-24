# wrapper
class match:
    def __init__(self, match):
        self.match = match
        self.gamestats = match.find_elements_by_class_name("GameStats")[0]
    
    # stats before clicking downarrow
    def self_stats(self):
        queue_type = class_content(self.gamestats, "GameType")
        is_win = class_content(self.gamestats, "GameResult") == 'Victory'

        return {
            'win': is_win,
            'queue_type': queue_type,
            'time': '4 days ago',
            'player': {
                'champion_played': 'ekko',
            },
            'gameplay': {
                'level': 14,
                'cs' : 120,
                'cs_per_min': 3.2,
                'pkill' : 0.59,
                'build': [],
                'kda': {
                    'overall': 3.88,
                    'kill': 6.8,
                    'death': 3.8,
                    'assist': 7.8
                },
                'damage': 29393,
                'tieravg': 'g4'
            }        
        }

    def player_stats(self, username):
        return {
            'username': 'bakanano',
            'win': True,
            'time': '4 days ago',
            'player': {
                'elo': 'g3',
                'champion_played': 'ekko',
                'rank': 4, # mvp, 2nd, 3rd (...)
                'opscore': 3.2,
            },
            'gameplay': {
                'level': 14,
                'cs' : 120,
                'cs_per_min': 3.2,
                'pkill' : 0.59,
                'build': [],
                'kda': {
                    'overall': 3.88,
                    'kill': 6.8,
                    'death': 3.8,
                    'assist': 7.8
                },
                'damage': 29393,
                'wards': {
                    'control': 0,
                    'total': 0,
                    'destroyed': 3
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