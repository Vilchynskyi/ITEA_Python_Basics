# quess the number
import random
if __name__ == '__main__':
    r = random.randint(1, 20)
    h = int(input('Quess a number between 1 and 20 '))
    while True:
        if h == r:
            break
        elif h < r:
            print('More')
            h = int(input('Try again '))
        else:
            print('Less')
            h = int(input('Try again '))
    print('You win!')