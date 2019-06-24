# give copy of dictionary or list to function
def copy_func(data):
    return data.copy()


if __name__ == '__main__':
    dictionary = {'Apple', 'Bank', 'Cat'}
    list = ['Apple', 'Bank', 'Cat']
    print('Original ', dictionary)
    print('Copy ', copy_func(dictionary))
    print('Original ', list)
    print('Copy ', copy_func(list))

