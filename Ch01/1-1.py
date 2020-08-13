"""
날짜 : 2020-07-13
이름 : 김나연
내용 : 파이썬 HTML 요청하기
"""

import urllib.request as req

# 네이버 HTML 문서 요청
resp = req.urlopen('http://naver.com').read()
html = resp.decode('UTF-8')
print(html)

