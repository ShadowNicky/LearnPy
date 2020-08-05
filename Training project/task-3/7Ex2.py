try:
    n = int( input('Введите число (от 1 до 10): '))
    mult = 0
    i = 0
    if 0<n<=10:
        while i < n:
            i += 1
            mult = i * n
            print(i,' * ', n, ' = ', mult)
    else: input('Введённое число не находиться в заданном диапазоне')
except:
    print('То что вы ввели крашит программу. Так не надо!')
    input()
