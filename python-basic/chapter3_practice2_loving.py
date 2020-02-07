

while True:
    status = int(input('两人的关系是不是达到了【朋友之上，恋人未满】？ 请输入1-是， 2-不是 '))
    if status == 1:
        print('1')
        answer = int(input('你是不是想和对方有进一步的发展？1-是， 2-不是 '))
        if answer == 1:
            extend = int(input('对方是不是想有进一步的发展？1-是， 2-不是 '))
            if extend == 1:
                print('恭喜你们，有情人终成眷属')    
            elif extend == 2:
                print('恭喜获得“好人卡”')
        elif answer == 2:
            print('还是做朋友吧。程序终结')
        break
    elif status == 2:
        print('2')
        break
    else:
        print('请输入说1 或 2。 1-是， 2-不是 ')