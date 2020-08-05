try:
    a=[]
    a.append(input('Введите число:'))
    while a[-1]!='стоп':
        a.append(input('Введите число или "stop" чтобы посчитть среднеарефмитическое значение: '))
    a.pop(-1)

    for i in range(len(a)):
        a[i] = int(a[i])
    s=sum(a)/len(a)
    print(s)

except:
    print('То что вы ввели крашит программу. Так не надо!')
    input()
