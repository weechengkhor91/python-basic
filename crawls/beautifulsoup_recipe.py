import requests
from bs4 import BeautifulSoup

#requests get
res_foods = requests.get('http://www.xiachufang.com/explore/')

#response
bs_foods = BeautifulSoup(res_foods.text,'html.parser')

#find all
list_foods = bs_foods.find_all('div',class_='info pure-u')
#print(list_foods)
list_all = []
for food in list_foods:
    #print(food)
    #print('---------------------------------------------')
    #extract
    tag_a = food.find('a')
    #print(tag_a)
    name = tag_a.text[17:-13]
    url = 'http://www.xiachufang.com'+tag_a['href']
    
    tag_p =food.find('p', class_='ing ellipsis')
    ingredients = tag_p.text[1:-1]
    #print(ingredients)
    #print(name, '\n', url, '\n', ingredients, '\n')
    list_all.append([name,url,ingredients])
    #print('---------------------------------------------')
print(list_all)