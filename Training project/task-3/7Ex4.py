import time
try:
    time_count = int(input('Введите колличество секунд: '))
    for i in range(time_count, 0, -1):
        print('Осталось %a секунд' % i)
        time.sleep(1)
    print('\n Время закончилось!')
    input()
except:
    print('То что вы ввели крашит программу. Так не надо!')
    input()

