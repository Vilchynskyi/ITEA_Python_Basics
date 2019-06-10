# Print 3 random numbers in a user-defined range
import random
if __name__ == '__main__':
    q = int(input('Введите число '))
    w = int(input('Введите второе число '))
    if q > w:
        c = q
        q = w
        w = c
    for i in range(3):
        print(random.randint(q, w))
