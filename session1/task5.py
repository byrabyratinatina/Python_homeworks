import os

os.system('cls')

quarter = int(input('Введите номер четверти: '))

if quarter == 1:
    print('x > 0, y > 0')
elif quarter == 2:
    print('x < 0, y > 0')
elif quarter == 3:
    print('x < 0, y < 0')
elif quarter == 4:
    print('x > 0, y < 0')
else:
    print('На координатной плоскости только 4 четверти')
    