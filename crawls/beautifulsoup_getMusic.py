import requests
from bs4 import  BeautifulSoup

# 请求html，得到response
res_music = requests.get('https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E5%91%A8%E6%9D%B0%E4%BC%A6')

print(res_music.text)
# 解析html
bs_music = BeautifulSoup(res_music.text,'html.parser')
# 查找class属性值为“js_song”的a标签，得到一个由标签组成的列表
list_music = bs_music.find_all('a',class_='js_song')
#print(type(list_music))
# 对查找的结果执行循环
for music in list_music:
    # 打印出我们想要的音乐名
    print(music['title'])