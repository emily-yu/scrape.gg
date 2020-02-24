class profile:
    def __init__(self, source):
        self.source = source

    def top_played_champions(self):
        return {
            '1': {
                'champion': 'Shyvana',
                'games_played': 44,
                'winrate': 0.66,
                'kda': {
                    'overall': 3.88,
                    'kill': 6.8,
                    'death': 3.8,
                    'assist': 7.8
                },
                'cs': 333,
                'cs_per_minute': 30
            }
        }

    def rank(self, type): # type: 'Ranked Solo, Flex 5:5 Rank
        return {
            'type': 'Ranked Solo',
            'lp': 61,
            'wlratio': 0.58,
            'win_count': 92,
            'loss_count': 68,
        }

    def queue_stats(self, type): # type: 'Ranked Solo, Ranked Flex
        return {
            'type': 'Ranked Solo', 
            'game_count': 10, 
            'win': 6,
            'loss': 4,
            'kda': 3.37,
            'pkill': 0.56,
            'top3champions': [], # see top played champions for structure
            'preferred': {
                '1': {
                    'role': 'Jungle',
                    'percent': 0.60,
                    'winratio': 0.5
                },
                '2': {
                    'role': 'Middle',
                    'percent': 0.40,
                    'winratio': 0.2
                }
            }
        }

    def recently_played_with(self):
        return {
            '1': {
                'username': 'ithrowname',
                'played': 8,
                'wins': 4,
                'loss': 4,
                'winratio': 0.5
            },
            '2': None,
            '3': None
        }
    # -------dont bother until finish everything else-----
    def all_champions(self):
        # https://na.op.gg/summoner/champions/userName=API
        return 'asdf'
    # ----------------------------------------------------