# give copy of dictionary or list to function
def copy_func(x):
    return x


if __name__ == '__main__':
    dictionary = {'Apple', 'Bank', 'Cat'}
    list = ['Apple', 'Bank', 'Cat']
    print('Original ', dictionary)
    print('Copy ', copy_func(dictionary.copy()))
    print('Original ', list)
    print('Copy ', copy_func(list.copy()))
