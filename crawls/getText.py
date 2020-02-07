import requests

#request
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')

# return value 
novel = res.text

print(novel[:800])



