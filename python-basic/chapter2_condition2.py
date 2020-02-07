
salary = 500

if salary <= 500:
    print('欢迎进入史塔克穷人帮前三名')
    if salary <= 100:
        print('恭喜您荣获“美元队长”称号！')
    else:
        print('请找弗瑞队长加薪')

elif 500 < salary <= 1000:
    print('祝贺您至少可以温饱了')

elif salary > 1000:
    print('经济危机都难不倒您')
    if 1000 < salary <= 20000:
        print('您快比钢铁侠有钱了！')
    else:
        print('您是不是来自于瓦坎达国？')
print('程序结束')
