import csv

with open('assets.csv', 'a', newline='', encoding='utf-8') as file:

    writer = csv.writer(file, dialect='excel')

    header = ['小区名称','地址', '建筑时间','楼栋', '单元',  '门牌', '朝向', '面积']

    writer.writerow(header)
    content = []

    name = input('小区名称: ')
    content.append(name)

    address = input('地址: ')
    content.append(address)

    built_year = input('建筑时间: ')
    content.append(built_year)

    block = input('楼栋: ')
    content.append(block)

    unit = input('单元: ')
    content.append(unit)

    postal = input('门牌: ')
    content.append(postal)

    direction = input('朝向: ')
    content.append(direction)

    square_feet = input('面积: ')
    content.append(direction)

    writer.writerow(content)