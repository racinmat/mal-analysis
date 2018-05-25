﻿﻿﻿﻿# Anime analysis

This is repo for analysing anime from big anime databases.
The main datasource will be MyAnimeList (MAL), and maybe later some others.

Anime sources:
- There is official API for MAL
    - docs: https://myanimelist.net/modules.php?go=api

- and then there is unofficial one which provides more information
    - release post and docs: https://myanimelist.net/forum/?topicid=1616529
    - apiary docs: https://jikan.docs.apiary.io/
    
- Taiga - desktop app which stores anime data offline in xml file
    - main info here: https://myanimelist.net/clubs.php?cid=21400
    - here is thread wilh xml data https://myanimelist.net/forum/?topicid=1358410

- there is one unofficial API https://classes.soe.ucsc.edu/cmps161/Winter12/proposals/bbtran/proposal/malunofficialapi.html#read_anime_list
    - but it is not working
    
- Kuristina - API for animelists and manga lists, provides both json and xml responses: https://github.com/TimboKZ/kuristina

- there is kaggle CSV dataset 
    - https://www.kaggle.com/CooperUnion/anime-recommendations-database
    - scripts for datamining from MAL https://www.kaggle.com/CooperUnion/anime-recommendations-database/discussion/47500
        - the github repo: https://github.com/Dibakarroy1997/myanimelist-data-set-creator

- other kaggle dataset
    - https://www.kaggle.com/canggih/anime-data-score-staff-synopsis-and-genre
        - but probably not much useful, probably as inspiration
        
- mal-scraper
    - https://github.com/QasimK/mal-scraper python project on github
    - wraps the websites loader and scrapper behind nice API. Can not load gender and location

- python-mal
    - https://github.com/shaldengeki/python-mal
    - other wrapper of crawler behind nice API. This one seems pretty advances. Can get username from user ID via comments. Seem to be way for discovering all users who commented more effectively. Because I know user ID of already crawled users, I can search only for missing users this way
    - can load also location and gender, which is nice
    - it seems to work only with python 2, but there is fork https://github.com/pushrbx/python3-mal which just adds python 3 compatibility
    
User sources:
As the first source, I am using the Dibakarroy1997/myanimelist-data-set-creator repo, for that I need user IDs.
So I need user ids (ideally active users) for scrapping ratings per user.
So far I am scraping forum topics to get user ids:
command for scrapping with sample id: `python .\createUserListFromPost.py 1582476 user-lists/UserListPost1582476.txt`
Topics scraped so far - all 8 watching challenge threads

user location and gender must be scraped from official page :(


### Previous analyses - for baseline:

- very basic, but good for very first data scraping validity - https://graph.anime.plus/s/globals
- seems nice, yet simple - https://aquabluesweater.wordpress.com/2010/03/06/compilation-of-top-anime-of-the-decade-lists-around-the-internet-series/
- totally offtopic, yet interesting - http://aja.gr.jp/english/japan-anime-data
- nice temporal analysis, only for moe - https://aquabluesweater.wordpress.com/2010/12/31/genre-over-time-moe/
- nice SAO analysis and score analysis per score - https://www.datasciencecentral.com/profiles/blogs/anime-reviews-and-scores
    - source code: https://github.com/nycdatasci/bootcamp007_project/tree/master/Project3-WebScraping/YisongTao
- recommendation of anime based on kaggle dataset: https://www.slideshare.net/imcinstitute/anime-recommendation-big-data-certification6
- other recommendation based on same dataset: https://medium.com/learning-machine-learning/recommending-animes-using-nearest-neighbors-61320a1a5934
- anime gender preferences: 
    - reddit post: https://www.reddit.com/r/anime/comments/6w60ru/gender_differences_in_anime_preferences/
    - reddit tables: https://www.reddit.com/r/anime/comments/6w60ru/gender_differences_in_anime_preferences/dm5rzdz/
    - tumblr blog: https://bunnyadvocate.tumblr.com/post/164636686962/gender-differences-in-anime-ratings
- anime genres analysis: https://bunnyadvocate.tumblr.com/post/171165531592/mapping-the-anime-fandom?is_related_post=1
- visualization genres article: https://bunnyadvocate.tumblr.com/post/168412595697/visualising-the-vn-market?is_related_post=1
- various analyses from kaggle: https://www.kaggle.com/CooperUnion/anime-recommendations-database/kernels
- anime users compatibility forum thread: https://myanimelist.net/forum/?topicid=5645
- anime recommmendation based on image: http://nicolasbotello.com/recommendMeSenpai/index.html
    - they have their own dataset with over 200 million records on their github https://github.com/bote795/recommendMeSenpai
- another recommendation system based on MAL: https://cs1951arecommender.wordpress.com/
    - maybe contact them and exchange datasets?
- some nice visualization in gephi, but not much verbose about the methodology  https://www.reddit.com/r/dataisbeautiful/comments/37icjf/visualization_of_myanimelist_recommendations_oc/
- described recommendation engine based on the kaggle dataset https://medium.com/learning-machine-learning/recommending-animes-using-nearest-neighbors-61320a1a5934

### DataSet
Some data are already scraped and can be downloaded here https://uloz.to/tam/_uNFuK0YI1Vmk
They are not cleaned and normalized, and far from complete yet.
It contains:
- 204 334 unique usernames
- 19 200 users with downloaded ratings and animelists
- 6 014 042 animelist records
- 3 564 447 ratings in animelists
- 13 983 unique anime ids based on ratings and animelists
- 11 800 anime with downloaded data

The newer version of part of scraped data can be downloaded here: https://uloz.to/tam/_jGFnKV19IIrD
As above, data are not normalized, only in pickle for easier manipulation and compression during scraping.
It contains:
- 204 334 unique usernames
- 46 800 users with downloaded ratings and animelists
- 14 704 980 animelist records
- 8 634 113 ratings in animelists
- 13 983 unique anime ids based on ratings and animelists
- 13 983 anime with downloaded data
The newer version is also available in CSV form, more useful to work with. It can be downloaded here: https://uloz.to/tam/_xZxO5NeiaNqO
It contains same data as binary files above.

3rd version of harvested data can be downloaded here: https://uloz.to/tam/_jU7mHh94xIWB
It contains both pickle and CSV files.
It contains:
- 302 841 unique usernames
- 75 800 users with downloaded ratings and animelists
- 23 753 842 animelist records
- 14 009 170 ratings in animelists
- 14 426 unique anime ids based on ratings and animelists
- 14 269 anime with downloaded data

4th version of harvested data can be downloaded here: https://uloz.to/tam/_c1ESfrgpyqrJ
It contains both pickle and CSV files.
It contains:
- 302 841 unique usernames
- 125 200 users with downloaded ratings and animelists
- 39 184 237 animelist records
- 23 096 715 ratings in animelists
- 14 430 unique anime ids based on ratings and animelists
- 14 269 anime with downloaded data

5th version of harvested data can be downloaded here: https://uloz.to/tam/_1VwDx2NIBaYh
It contains both pickle and CSV files.
It contains:
- 302 841 unique usernames
- 146 700 users with downloaded ratings and animelists
- 45 626 200 animelist records
- 26 832 473 ratings in animelists
- 14 441 unique anime ids based on ratings and animelists
- 14 269 anime with downloaded data
- 68 975 of users also have demographics data

6th version of harvested data can be downloaded here: https://uloz.to/tam/_Rl1XPwuqnsvn
It contains only CSV files.
It contains:
- 302 841 unique usernames
- 235 200 users with downloaded ratings and animelists
- 65 233 633 animelist records
- 37 987 916 ratings in animelists
- 14 466 unique anime ids based on ratings and animelists
- 14 269 anime with downloaded data
- 183 188 of users also have demographics data

The native `.rick` version can be loaded into python as 
```python
import pickle
with open('UserList.rick', 'rb') as f:
    users = pickle.load(f)
    
with open('AnimeList.rick', 'rb') as f:
    animes = pickle.load(f)
```

The CSV can be loaded with pandas as you are used to 
```python
import pandas as pd

animes = pd.read_csv('AnimeList.csv')
users = pd.read_csv('UserList.csv')
animeLists = pd.read_csv('UserAnimeList.csv')
```

or you just can open it in Excel or whatever.    

##### just other stuff and notes

tools and other ideas: 
voyager - web based tool for datasets exploratory analysis:
- github: https://github.com/vega/voyager
- online demo: https://vega.github.io/voyager/
- paper: http://www.cs.tufts.edu/comp/250VIS/papers/2015-Voyager-InfoVis.pdf
- university page: https://idl.cs.washington.edu/papers/voyager/

vega-lite - other tool for visualizations, specifications in json:
- university page: http://idl.cs.washington.edu/papers/vega-lite/

lyra - completely code-less, only web-based GUI:
- university page: https://idl.cs.washington.edu/papers/lyra/

jinak klasika: paraview, tableau, gephi

pro python: networkx pro grafy, plot.ly + dash na interaktivní vizualizace https://dash.plot.ly/getting-started

d3 for nice javascript graphs: https://github.com/d3/d3/wiki/gallery

nápady:
- zjistit velké rozdíly v hodnocení anime, s velkým rozptylem, kde je hodnotí hodně lidí velmi kladně a hodně lidí velmi záprně
- podívat se na rozdíly mezi hodnoceními v čase
- rozdíl mezi lidmi co hodnotili málo a co hodnotili hodně anime, co viděli a co hodnotili za díla
- korlace score, žánrů, sledovanosti, a času, a lidí, co sledují hodně, málo
- rozclusterovat lidi na málohodnotící, a hodně hodnotící, podle střední hodnoty hodnocení apod.
- prozkoumat recency bias u vydání anime, gender split
- prozkoumat plan to watch listy
- prozkoumat sledovatnost žánrů v závislosti na zemi, věku, pohlaví, ale i času, a časový vývoj různých věcí, zkusit změnu trendů v čase, vývoj počtu děl v žánru, průměrné oblíbenosti žánrů v čase apod
- udělat časový vývoj podobně jako https://www.gapminder.org/videos/200-years-that-changed-the-world/?
- vývoj do spiral chartu, například průměrné hodnocení anime podle data vydání: https://stackoverflow.com/questions/46575723/creating-a-temporal-range-time-series-spiral-plot
- časový výoj počtu anime různých žánrů a proměrné hodnocení jako video podobné 200 years? průměr hodnocení na ose a počet kusů jako velikost kolečka? 
popis podobnosti visual novel v grafech: 
For the attraction value specifically, IIRC, it went along these lines (for nodes A and B)

bunnyadvocate
similarityAB = <fans who read both>/<fans who read A>

similarityBA = <fans who read both>/<fans who read B>

attraction = (1-sqrt((1-similarityAB)*(1-similarityBA)))^3
the attraction between two nodes was always the same going each way, A->B and B->A or else you get messy situations where one node is constantly chasing the other as the other is repelled by it more


data notes: days spent watching anime should not be takes seriously because of mismatches. E.g. here: 
https://myanimelist.net/profile/Tationika 1 332.1 days are spent watching anime because there are 9001 rewatches for Akira and Perfect Blue
https://graph.anime.plus/Tationika/profile?referral=search

showing piecharts on world map: http://www.geophysique.be/2010/11/26/matplotlib-basemap-tutorial-06-real-case-pie-charts/

