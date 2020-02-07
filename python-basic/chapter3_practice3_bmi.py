weight = float(input('Insert your weight: '))
height = float(input('Insert your height: '))

bmi = weight / (height * height)
print(bmi)
if bmi < 18.5:
    print('underweight')
elif 18.5 <= bmi < 24.0:
    print('normal')
elif 24.0 <= bmi < 28.0:
    print('overweight')
else:
    print('obese') 