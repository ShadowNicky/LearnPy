try:
    a = float(input('Введите число: '))
    print(round(a % 1,10))
    input()
except:
    print('Вы ввели неверные значения!')
    input()