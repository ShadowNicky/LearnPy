try:
    p = n = int(input('Введите число: '))
    sum = 0
    if n > 0:
        for i in range(1, n + 1):
            sum += i
        print('Сумма всех чисел:', p, ' =', sum)
        input()

    elif n == 0: input('Зачем вы ввели ноль?')
    else: input('Вы что ввели отрицательное число? Зачем?')
except:
    print('То что вы ввели крашит программу. Так не надо!')
    input()
