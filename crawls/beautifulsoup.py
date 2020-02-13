#调用requests模块
import requests

from bs4 import BeautifulSoup

#获取代码 get
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')

# check response
print(res.status_code)

soup = BeautifulSoup(res.text, 'html.parser')

print(type(soup))
print(soup)
#with open('crawls/book.html','w', encoding='utf-8') as file:
#content = file.write(res.text)
