try:
    q = int(input('Колличество чисел: '))
    r = input('Диапазон чисел: ').split('-')
    f = int(r[0])
    s = int(r[1])

    from random import sample
    list = sample(range(f, s), q)
    a=sum(list)
    print('Числа: ',list)
    print('Сумма чисел: ',a)
except:
    print('То что вы ввели крашит программу. Так не надо!')
    input()

