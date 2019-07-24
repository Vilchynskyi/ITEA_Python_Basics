"""Без использования методов строк, напишите реализацию таких методов строк:
replace, split, find. Напишите функцию remove по индексу и по подстроке.
"""


def remove_by_index(string, index):
    return string[:index] + string[1 + index:]


def remove_by_substring(string, substring):
    index = 0
    for i in string:
        if i == substring[0]:
            if string[index:index + len(substring)] == substring:
                return string[:index] + string[len(substring) + index:]
        index += 1


def replace(string, old_item, new_item):
    index = 0
    global new_string
    for i in string:
        if i == old_item[0]:
            if string[index:index + len(old_item)] == old_item:
                new_string = new_item + string[len(old_item):]
                return new_string
    return string


def split_func(string, separator):
    new_data = []
    temp = ''
    for i in string:
        if i != separator:
            temp += i
        else:
            new_data.append(temp)
            temp = ''
    if temp:
        new_data.append(temp)
    return new_data


def find(string, search):
    count = 0
    for i in string:
        if i == search[0]:
            if string[count:count+len(search)] == search:
                return count
        count += 1
    return -1


if __name__ == '__main__':
    data = 'apple, banana, cat, dictionary'
    print('Original --', data)
    print('Replace function -', replace(data, 'apple', 'auto'))
    print('Split function -', split_func(data, ','))
    print('Find function -', find(data, 'le'))
    print('Remove by index -', remove_by_index(data, 3))
    print('Remove by substring -', remove_by_substring(data, 'dict'))
