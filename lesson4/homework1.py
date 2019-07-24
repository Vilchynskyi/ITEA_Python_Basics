"""Пользователь задает случайное число n. Сгенерировать список этой длины
и заполнить его 0 и 1 случайным образом. Найти самую длинную цепочку
из подряд идущих 0 или 1. Вывести эту длину.
Для какого максимального значения n, ваш алгоритм будет работать меньше
чем 1 секунда?
"""


import random
import time

if __name__ == '__main__':
    user_input = int(input('len '))
    list_of_num = []
    for i in range(user_input):
        list_of_num.append(random.randint(0, 1))
    print(list_of_num)
    max_count = 1
    list_of_counter = []
    for i in range(len(list_of_num)-1):
        if list_of_num[i] == list_of_num[i + 1]:
            max_count += 1
        else:
            list_of_counter.append(max_count)
            max_count = 1
    print(time.process_time(), 'seconds. Max length of list when program '
                               'is working less than 1 second, '
                               'is near 99500 numbers.')
    print('Max same numbers in a row -', max(list_of_counter))
