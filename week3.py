import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

# ranks = list(map(lambda tr: tr.select_one('.number').text[0:2].strip(), musicTrs))
# titles = list(map(lambda tr: tr.select_one('.title ellipsis').text.strip(), musicTrs))
# artists = list(map(lambda tr: tr.select_one('.artist ellipsis').text.strip(), musicTrs))

for tr in trs:
    rank = tr.select_one('.number').text[0:2].strip()
    title = tr.select_one('.title').text.strip()
    artist = tr.select_one('.artist').text.strip()
    print(rank, title, artist)
