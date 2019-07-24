# give copy of dictionary or list to function
def copy_func(data):
    return data.copy()


if __name__ == '__main__':
    dictionary = {'Apple', 'Bank', 'Cat'}
    original_list = ['Apple', 'Bank', 'Cat']
    print('Original ', dictionary)
    print('Copy ', copy_func(dictionary))
    print('Original ', original_list)
    print('Copy ', copy_func(original_list))

