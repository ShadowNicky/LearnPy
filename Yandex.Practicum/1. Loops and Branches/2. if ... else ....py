import random  # импорт модуля random

 # фукнция randint() генерирует случайное целое число в заданном диапазоне
current_hour = random.randint(0, 23)

if current_hour < 12:
    print('Доброе утро!')
else:
    print('Добрый день!')
