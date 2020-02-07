start_floor = '3'
end_floor = '4'
floor_last_number = ['01','02','03']

#init start floor rooms template
start_floor_rooms = {301:[1,80], 302:[1,80], 303: [2,90]}

#create object , save all data
unit_rooms = {}
unit_rooms[int(start_floor)] = start_floor_rooms
#unit_rooms[3] = {301:[1,80], 302: [1,80], 303: [2,90]}


floor_rooms = {}
#给4楼创建一个字典
for i in range(len(start_floor_rooms)):
    #print(i)
    number = '4' + floor_last_number[i]
    # number = [401,402,403]
    info = start_floor_rooms[int(start_floor + floor_last_number[i])]
    # int(start_floor+floor_last_number[i]) = 301
    #info = [1,80]
    floor_rooms[int(number)] = info
    #print(floor_rooms[int(number)])
    #print(floor_rooms)
unit_rooms[4] = floor_rooms
print(unit_rooms)