import requests, random, bs4

# 为躲避反爬机制，伪装成浏览器的请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url, headers=headers)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        num = titles.find('em',class_="").text
        #查找序号
        title = titles.find('span', class_="title").text
        #查找电影名
        tes = titles.find('span',class_="inq").text
        #查找推荐语
        comment = titles.find('span',class_="rating_num").text
        #查找评分
        url_movie = titles.find('a')['href']

        print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url_movie)
----------------------------------------------------------------------------------------------
          9         num = titles.find('em',class_="").text
     10         title = titles.find('span', class_="title").text
---> 11         tes = titles.find('span',class_="inq").text
     12         comment = titles.find('span',class_="rating_num").text
     13         url_movie = titles.find('a')['href']

AttributeError: 'NoneType' object has no attribute 'text'
看下报错信息“AttributeError: 'NoneType' object has no attribute 'text' ” ，定位到了tes这一行，这是推荐语呀，为什么会错呢？ 我们回归网页，发现第223个电影是《三块广告牌》，诶，它竟然没有推荐语，而空值是没办法做text文本转换的，因此报错了呢。
那怎么解决呢，聪明的你一定想到啦～ Bingo，加一个判断就可以啦～
修改过代码，我们再试一下哦～