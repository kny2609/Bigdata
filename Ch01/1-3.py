"""
날짜 : 2020-07-13
이름 : 김나연
내용 : 파이썬 네이버 헤드라인 뉴스 파싱하기
"""

from bs4 import BeautifulSoup as bs
import urllib.request as req

html = req.urlopen('https://news.naver.com').read().decode('euc-kr')
#print(html)

dom = bs(html, 'html.parser')
news_titles = dom.select('#section_it > .com_list > div > ul > li > a > strong')

for tit in news_titles:
    print(tit.string)
