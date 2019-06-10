# Extract the square of the number as long as the value is bigger than 10
import math
if __name__ == '__main__':
    i = int(input('Insert the number '))
    while i > 10:
        print(i)
        i = math.sqrt(i)
