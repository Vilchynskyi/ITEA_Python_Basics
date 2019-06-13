# Check prime number
import math

def check_prime(x):
    for i in range(x - 1, int(math.sqrt(x)), -1):
        if not x % i:
            return False
    return True

if __name__ == '__main__':
    num = int(input('Insert a number '))
    while num < 2:
        print('Number have to be 2 and more')
        num = int(input('Insert a number '))
    if num == 2:
        print('Number is prime')
    elif check_prime(num):
        print('Number is prime')
    else:
        print('Number is not prime')
