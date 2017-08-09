num = []


def add(num):
    try:
        return sum(num)
    except TypeError:
        pass


# def subtract():
#
#
# def multiply():
#
#
# def divide():
#
#
# def square_root():
#
#
# def mean():
#
#
# def power():
#
#
# def cosine():
#
#
# def range():

def get_num():
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
    try:
        if operation in (1, 2, 3, 4, 6, 7, 9):
            num.append(int(input('Please enter your first number: ')))
            num.append(int(input('Please enter your second number: ')))
            return num
        elif operation in (5, 8):
            num.append(int(input('Please enter your first number: ')))
            return num
        else:
            print('Number is not an operation')
    except ValueError:
        print('Please enter a valid number')


if __name__ == '__main__':
    print(add(get_num()))
