import requests as req 
from bs4 import BeautifulSoup as bs
import pandas as pd

res = req.get("https://music.bugs.co.kr/chart")


# print(res.text)
# print(res.status_code) #200 

soup = bs(res.text, "lxml")
# print(soup)

# 데이터 선택
rangking = soup.select(".ranking > strong")
title = soup.select(".title > a")
artist = soup.select(".artist > a:nth-child(1)")

# print(len(rangking))
# print(len(title))
# print(len(artist))

# #데이터 저장
# rangkingList = []
# titleList = []
# artistList = []

# for i in range(len(rangking)) :
#     rangkingList.append(rangking[i].text)
#     titleList.append(title[i].text)
#     artistList.append(artist[i].text)

# # print(artistList)    

# data = {"rank" : rangkingList, "title" : titleList, "artist" : artistList }
# print(pd.DataFrame(data))

#데어터 자장 
rangkingList = [r.text.strip() for r in rangking]
titleList = [t.text.strip() for t in title]
artistList = [a.text.strip() for a in artist]

#데이터 프레임 생성
chart_df = pd.DataFrame ({
    'Ranking':rangkingList,
    'Title':titleList,
    'Artist':artistList
})

# JSON 파일로 저장
chart_df.to_json("bugsChart100.json", force_ascii=False, orient="records")