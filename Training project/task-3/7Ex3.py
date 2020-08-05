a = []
try:
    n = int(input('Введите n: '))
    for i in range (n+1): a.append(0);
    for i in range (2, n+1):
        if a[i]==0:
            print (i, end='; ')
            j = 2*i
            while j<=n:
                a[j] = 1
                j+=i
except:
    print('То что вы ввели крашит программу. Так не надо!')
    input()
