import requests as req 
from bs4 import BeautifulSoup as bs
import pandas as pd

head = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Whale/3.25.232.19 Safari/537.36'}
res = req.get("https://www.melon.com/chart/index.htm", headers=head)


# print(res.text)
# print(res.status_code) #406

soup = bs(res.text, "lxml")

# 데이터 선택

ranking = soup.select("tbody .wrap.t_center > .rank")
title = soup.select("tbody .wrap_song_info .ellipsis.rank01 span > a")
artist = soup.select("tbody .wrap_song_info .ellipsis.rank02 span > a:nth-child(1)")

print(len(ranking))
print(len(title))
print(len(artist))

#데이터 자장 
ranking = [r.text.strip() for r in ranking]
title = [t.text.strip() for t in title]
artist = [a.text.strip() for a in artist]

#데이터 프레임 생성
chart_df = pd.DataFrame ({
    'Ranking':ranking,
    'Title':title,
    'Artist':artist
})

# JSON 파일로 저장
chart_df.to_json("MelonChart100.json", force_ascii=False, orient="records")