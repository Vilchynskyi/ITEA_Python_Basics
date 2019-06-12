# Выводить буквы строки до первой заглавной
if __name__ == '__main__':
    a = 'this is sTroka'
    for i in a:
        if i.islower() or i.isspace():
            print(i, end='')
        else:
            break
