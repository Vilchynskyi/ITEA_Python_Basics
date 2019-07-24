"""Без использования методов словарей(кроме items),
напишите  функцию remove по ключу и remove по значению.
"""


def remove_by_key(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    return dictionary


def remove_by_value(dictionary, item):
    new_dict = {}
    for key, value in dictionary.items():
        if value != item:
            new_dict[key] = value
    return new_dict


if __name__ == '__main__':
    data = {'Ford': 'Mustang', 'Dodge': 'Charger 1970', 'BMW': 'M5'}
    print(remove_by_key(data, 'Ford'))
    print(remove_by_value(data, 'M5'))
