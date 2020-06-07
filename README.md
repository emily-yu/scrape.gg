## scrapeGG

A python library to pull information on Profile and MatchHistory from op.gg (last verified 06/05/2020). 

Note: scrapes using English, only tested on NA server at the moment.

### Requirements

- from selenium import webdriver
- from selenium.webdriver.common.by import By
- from selenium.webdriver.support import expected_conditions as EC
- from selenium.webdriver.support.wait import WebDriverWait
- import re
- import os
- from bs4 import BeautifulSoup

### Installation

	pip install scrapeGG==0.0.5

or

    https://github.com/emily-yu/scrape.gg.git
    cd scrape.gg
    python setup.py

### Usage
set up chromedriver, if not already exists
check if already exists using `chromedriver --version`

install chromedriver `brew cask install chromedriver`

find path `which chromedriver`

import and create an instance, such that 'API' is the summonerName you want to search for.

`scrapeGG(string summonerName)`

	from scrapeGG import scrapeGG
	init = scrapeGG('API')
	
### Functions
(see scrape_test.py for usage examples)
(see snapshots/06-06-2020.json for example output)

### scrapeGG.profile

- .getProfile() - [CONSTRUCTOR] - returns profile()
- .recently\_played\_with()
- .top\_played\_champions() - todo
- .rank(string game_type= ["Ranked Solo", "Total", "Ranked Flex 5v5") - todo

### scrapeGG.match

- .getMatch(int count) - returns match()
- .getMatchSequence(int count) - returns arr[scrapeGG.match]
- .game\_player\_names(is_win)
- .self_stats()
- .recent.player_stats(string summonerName) - summonerName can be any of the players in the game
- .overview() - unstable*
- .build() - unstable*

*selenium has issues with click events, which occasionally raises`selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted`

### example usage

```
from scrapeGG import scrapeGG

init = scrapeGG('API')

# test match api class
recent = init.getMatch(1)
player_names = recent.game_player_names(True)

profile = init.getProfile()
ranksolo_rank = profile.rank('Ranked Solo')

```

### changelog
0.0.4 - first release on PyPI
0.0.5 - correction to installation instructions
