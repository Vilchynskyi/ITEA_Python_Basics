# The sum of all dividers
if __name__ == '__main__':
    a = int(input('Insert a number '))
    while a <= 0:
        print('Wrong number')
        a = int(input('Insert a number '))
    res = 0
    for i in range(1, a+1):
        if a % i == 0:
            res += i
    print('Sum is', res)
