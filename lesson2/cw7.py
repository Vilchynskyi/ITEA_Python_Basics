# Play the guess until user insert 0
if __name__ == '__main__':
    num = int(input('Quess the number '))
    sum = 0
    amount = 0
    while num != 0:
        num = int(input('Nope, try again '))
        sum += num
        amount += 1
    print('Bingo. Average {0}. Amount of numbers {1}'.format(sum, amount))
