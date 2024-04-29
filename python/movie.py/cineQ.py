from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import datetime
import time
import json

# 현재 날짜 가져오기
current_date = datetime.now().strftime("%Y-%m-%d")
filename = f"chart_apple100_{current_date}.json"


# 웹드라이브 설치
options = ChromeOptions()
service = ChromeService(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)
browser.get("https://www.cineq.co.kr/Movie/BoxOffice")

# 페이지가 완전히 로드될 때까지 대기
WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "section group section-movie-list boxoffice"))
)

# 업데이트된 페이지 소스를 변수에 저장
html_source_updated = browser.page_source
soup = BeautifulSoup(html_source_updated, 'html.parser')

# 데이터 추출
songs_list = []
tracks = soup.select(".ul .data-moviecode")

for track in tracks:
    ranking = track.select_one(".movie-desc .label").text.strip()
    title = song.find('div', class_='songs-list-row__song-name').text.strip()
    # artist = song.find('a', {'data-testid': 'click-action'}).text.strip()
    # album = song.find_all('a', {'data-testid': 'click-action'})[1].text.strip()
    # img_tag = song.find('picture').find('source', type="image/webp")  # More specific targeting to webp images
    # if img_tag:
    #     image_sources = img_tag['srcset']
    #     # Extracting the desired 80x80 webp image URL from srcset
    #     image_url = next((src.split(' ')[0] for src in image_sources.split(',') if '80x80bb.webp' in src), "No image available")
    # else:
    #     image_url = "No image available"

    #content > div.section.group.section-movie-list.boxoffice > ul > li:nth-child(1) > img
    #content > div.section.group.section-movie-list.boxoffice > ul > li:nth-child(1) > div

    songs_list.append({
        'ranking': ranking,
        # 'title': title,
        # 'artist': artist,
        # 'album': album,
        # 'image_url': image_url
    })

# 추출된 데이터를 JSON 파일로 저장
# with open(filename, 'w', encoding='utf-8') as f:
#     json.dump(song_data, f, ensure_ascii=False, indent=4)

# # 브라우저 종료
# browser.quit()