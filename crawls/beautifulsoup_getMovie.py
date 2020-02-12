import requests
from bs4 import BeautifulSoup

# 为躲避反爬机制，伪装成浏览器的请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

for x in range(10):

    #requests
    url = 'https://movie.douban.com/top250?start=' + str(x*25) +'&filter='
    res = requests.get(url,headers = headers)

    #response status code
    html = res.text
    print(res.status_code)
    #BeautifulSoup(param1, 'html.parser')
    content = BeautifulSoup(html, 'html.parser')

    #find all
    items = content.find_all('ol',class_='grid_view')
    items = content.find_all('li')
    all_titles = content.find_all('span',class_='title')
    print(all_titles )
    print(len(items))

    for item in items:
        #print(type(item))
 #or (item.find('em',class_='') != None) or (item.find('span',class_='rating_num') != None) or (item.find('a') != None)
        if item.find('span', class_='title') != None or item.find('em',class_='') != None:
            title = item.find('span', class_='title').text
            num = item.find('em',class_='').text
            #comments = item.find('span',class_='rating_num').text
            #url_movie = item.find('a')['href']
            print(num + '. ' +title )
            print('-----------------------------------------------------------------')


