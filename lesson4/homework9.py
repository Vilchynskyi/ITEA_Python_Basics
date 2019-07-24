# Напишите функцию, которая сортирует массив рекурсивно.


def sort(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            temporary = array[i]
            array[i] = array[i + 1]
            array[i + 1] = temporary
            sort(array)


if __name__ == '__main__':
    numbers = [1, 45, 76, 34, 977, 4, 78, 23]
    sort(numbers)
    print(numbers)
