import requests
import html2text

#print(dir(html2text))


for i in range(32,43):
    #print(i)
    #requests get
    url = 'https://www.ddshu.net/12506_5902'+ str(i) +'.html'
    #print(url)
    res = requests.get(url)
    res.encoding='gbk'
    #return value to variable
    novel = res.text
    convert = html2text.HTML2Text()
    convert.ignore_links = True
    convert.unicode_snob = True
    content = convert.handle(novel)
    #print(content)
    with open('./crawls/novel1.txt', 'a+', encoding='utf-8') as file:
        writer = file.write(content)
