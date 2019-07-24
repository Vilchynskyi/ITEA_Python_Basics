"""Без использования методов списков, напишите реализацию таких
методов списков: insert, remove.
"""


def insert(array, index, new_obj):
    if len(array) >= index:
        return array[:index] + [new_obj] + array[index:]
    else:
        return array + [new_obj]


def remove(array, item):
    index = 0
    if item in array:
        for i in array:
            if i == item:
                return array[:index] + array[1 + index:]
            index += 1


if __name__ == '__main__':
    data = ['apple', 'banana', 'cat', 'dictionary']
    print(remove(data, 'cat'))
    print(insert(data, 2, 'car'))
