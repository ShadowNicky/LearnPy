a = input('Введите первое число: ')
b = input('Введите второе число: ')
try:
    a = int(a)
    b = int(b)
    if a<b: print(a,'<',b)
    elif a>b: print(a,'>',b)
    else:print (a,'=',b)
    input()
except:
    print('Вы ввели неверные значения!')
    input()
