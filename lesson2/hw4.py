# Check simple number
if __name__ == '__main__':
    a = int(input('Insert a number '))
    while a < 0:
        print('Number can not be negative')
        a = int(input('Insert a number '))
    if a/a == 1 and a/1 == a:
        print('Number is prime')
    else:
        print('Number is not prime')