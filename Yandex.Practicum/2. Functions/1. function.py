# объявите функцию здесь
def print_friends_count(friends_count):

    if friends_count == 1:
        print('У тебя 1 друг')
    elif 2 <= friends_count <= 4:
        print('У тебя ' + str(friends_count) + ' друга')
    elif friends_count >= 5:
        print('У тебя ' + str(friends_count) + ' друзей')

for i in range(1, 11):
    print_friends_count(i)