a = input('Введите строку: ')
if len(a) == 0:
    print ('Вы ничего не ввели')
elif len(a) < 12:
    if len(a) == 1:
        print('В строке', len(a), 'символ')
    elif len(a) < 5:
        print('В строке', len(a), 'символа')
    else:
        print('В строке', len(a), 'символов')
else:
    print('Слишком много символов')
