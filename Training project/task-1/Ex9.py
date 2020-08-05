a = str(input('Введите строку: '))
b = a.split(' ')
print('Количество букв \"е\": ' + str(a.count('е')))
print('Измененная строка: ' + b[0].replace('е', 'и') + a[len(b[0]):len(a)])
input ()

