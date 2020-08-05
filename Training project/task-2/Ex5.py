try:
    a = float(input('Введите ширину в мм: '))
    b = float(input('Введите длину в мм: '))
    print('Площадь пола = ', round((a*b/1000000),10), '(м^2)')
    input()
except:
    print('Вы ввели неверные значения!')
    input()
