# wrapper
def match(match):
    return {
        'tier_avg': 'g5',
    }

    # stats before clicking downarrow
    def player_stats(match, username):
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
                'kda': 3.0,
                'kda_detail': {
                    'kill': 2,
                    'death': 0, 
                    'assist': 1
                },
                'damage': 29393,
                'wards': {
                    'control': 0,
                    'total': 0,
                    'destroyed': 3
                }
            }        
        }

    def overview(match):
        blue_team = {}
        red_team = {
            'players': [],
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
        }

    # player stats
    def build(match):
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