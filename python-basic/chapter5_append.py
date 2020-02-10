students = ['lee keng', 'wee cheng', 'lee peng']

for i in range(3):
    student1 = students[0]
    students = students[1:]
    students.append(student1)
    print(students)