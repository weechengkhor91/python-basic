import requests
from bs4 import BeautifulSoup

#requests get
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spder-men0.0.html')

#response 200
#print(res.status_code)

#response content
#print(res.text)

#check directory
#print(dir(res))

content = BeautifulSoup(res.text, 'html.parser')


item = content.find('div')

#<class 'bs4.element.Tag'>
print(type(item))

print(item)