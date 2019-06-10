# triangle. the height insert user
if __name__ == '__main__':
    h = int(input('Insert a height '))
    while h <= 0:
        print('Height can not be less than 1')
        h = int(input('Insert a height '))
    for i in range(h):
        print(' ' * (h - i - 1) + '|' * (i * 2 + 1))
