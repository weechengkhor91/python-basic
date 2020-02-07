import requests

res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')

#print(res.status_code)
#print(type(res))


#print(res.content)

pic = res.content

#photo = open('./crawls/get.jpg', 'wb')

#photo = writer(pic)

#photo.close()

with open('./crawls/picGet.jpg','wb') as file:
    writer = file.write(pic)