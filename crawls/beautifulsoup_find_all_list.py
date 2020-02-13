import requests
from bs4 import BeautifulSoup

#request get
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')

#response 
print(res.status_code)

html = res.text

content = BeautifulSoup(html, 'html.parser')

items = content.find_all(class_='books')

#print(items)

for item in items:
    print('想找的数据都包含在这里了：\n', item)


