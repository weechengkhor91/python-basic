file1 = open('gongxi.txt','r',encoding='utf-8')
content = file1.read()

file1.close()


for i in content:
    print(i)