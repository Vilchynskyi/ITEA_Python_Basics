# Find a factorial of number
import math
if __name__ == '__main__':
    f = int(input('Insert number '))
    while f < 0:
        print('Number can not be negative')
        f = int(input('Insert a number '))
    print('Factorial equal ', math.factorial(f))
