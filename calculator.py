import math


def add(num):
    try:
        return sum(num)
    except TypeError:
        pass


def subtract(num):
    try:
        return num[0]-num[1]
    except TypeError:
        pass


def multiply(num):
    try:
        return num[0]*num[1]
    except TypeError:
        pass


def divide(num):
    try:
        return num[0]/num[1]
    except TypeError:
        pass
    except ZeroDivisionError:
        pass


def square_root(num):
    try:
        return math.sqrt(num[0])
    except TypeError:
        pass
    except ValueError:
        pass


def mean(num):
    try:
        return float(sum(num)) / max(len(num), 1)
    except TypeError:
        pass


def power(num):
    try:
        return num[0]**num[1]
    except TypeError:
        pass


def cosine(num):
    try:
        return math.cos(num[0])
    except TypeError:
        pass


def get_operation():
    print('Welcome to William\'s Calculator!')
    operation = int(input('Please choose from the following operations:\n'
                          '1. addition\n'
                          '2. subtraction\n'
                          '3. multiplication\n'
                          '4. division\n'
                          '5. square root\n'
                          '6. mean\n'
                          '7. power\n'
                          '8. cosine\n'
                          '9. range\n'))
    return operation


def get_num(operation):
    try:
        if operation in (2, 3, 4, 7, 9):
            num.append(int(input('Please enter your first number: ')))
            num.append(int(input('Please enter your second number: ')))
            return num
        elif operation in (1, 6):
            count = int(input('Please enter the amount of numbers you would like to enter: '))
            for i in range(count):
                num.append(int(input('Please enter your number: ')))
            return num
        elif operation in (5, 8):
            if operation == 5:
                num.append(int(input('Please enter your first number: ')))
                if num[0] < 0:
                    print('The square root of a number must be positive!')
                else:
                    num.append(int(input('Please enter your first number: ')))
                    return num
        else:
            print('Number is not an operation')
    except ValueError:
        print('That was not a valid number. Please try again.')


if __name__ == '__main__':
        num = []
        operation = get_operation()
        if operation == 1:
            answer = add(get_num(operation))
            if answer is None:
                pass
            else:
                print('Your answer is {}'.format(answer))
        elif operation == 2:
            answer = subtract(get_num(operation))
            if answer is None:
                pass
            else:
                print('Your answer is {}'.format(answer))
        elif operation == 3:
            answer = multiply(get_num(operation))
            if answer is None:
                pass
            else:
                print('Your answer is {}'.format(answer))
        elif operation == 4:
            answer = divide(get_num(operation))
            if answer is None:
                pass
            else:
                print('Your answer is {}'.format(answer))
        elif operation == 5:
            answer = square_root(get_num(operation))
            if answer is None:
                pass
            else:
                print('Your answer is {}'.format(answer))
        elif operation == 6:
            answer = mean(get_num(operation))
            if answer is None:
                pass
            else:
                print('Your answer is {}'.format(answer))
        elif operation is 7:
            answer = power(get_num(operation))
            if answer is None:
                pass
            else:
                print('Your answer is {}'.format(answer))
        elif operation == 8:
            answer = cosine(get_num(operation))
            if answer is None:
                pass
            else:
                print('Your answer is {}'.format(answer))
        elif operation == 9:
            answer = get_num(operation)
            if answer is None:
                pass
            else:
                print('Your answer is', end=' ')
                if answer[0] > answer[1]:
                    answer.sort()
                    for x in list(reversed(range(answer[0], answer[1] + 1))):
                        print(x, end=' ')
                else:
                    for x in range(answer[0], answer[1]+1):
                        print(x, end=' ')
