# Print squares of numbers until they are less than 1000
if __name__ == '__main__':
    i = 1
    while i * i < 1000:
        print(i ** 2)
        i += i
