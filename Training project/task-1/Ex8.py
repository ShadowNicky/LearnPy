a = str(input('Введите слово из трех букв: '))
b = ord(a[0])
c = ord(a[1])
d = ord(a[2])
if len(a) < 3:
    print('Слово слишком короткое')
elif len(a) > 3:
    print('Слово слишком длинное')
else:
    print ("Первый символ " + a[0] + ' имеет код ' + str(b))
    print ("Второй символ " + a[1] + ' имеет код ' + str(c))
    print ("Третий символ " + a[2] + ' имеет код ' + str(d))
    print ('Сумма: ' + str(int(b) + int(c) + int(d)))
input()
