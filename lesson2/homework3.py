# Возвести число в степень с помощью цикла
if __name__ == '__main__':
    num = int(input('Insert a number '))
    power = int(input('Insert a power '))
    while num < 0 or power < 0:
        print('Numbers can not be negative')
        num = int(input('Insert a number '))
        power = int(input('Insert a power '))
    res = 1
    for i in range(power):
        res *= num
    print('Result is ', res)