year = input('Введите год: ')
try:
    a = int(year)
    if a % 4 != 0 or (a % 100 == 0 and a % 400 != 0):
        print('Это обычный год!')
    else: print('Это високосный год!')
    input()
except:
    print('Вы ввели неверные значения!')
    input()
