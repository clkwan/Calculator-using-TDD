
def add(num):
    for i in num:
        if i == str:
            print('Please enter a valid number')
        else:
            return sum(num)

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

if __name__ == '__main__':
    print('Welcome to William\'s Calculator!')
    operation = input('Please choose from the following operations:\n'
                      '1. addition\n'
                      '2. subtraction\n'
                      '3. multiplication\n'
                      '4. division\n'
                      '5. square root\n'
                      '6. mean\n'
                      '7. power\n'
                      '8. cosine\n'
                      '9. range\n')
    if operation == 1:
        num = []
        try:
            num = input('Please input the numbers you would like to sum up. Inputs should be separated by a space')
            num = num.split(' ')
        except ValueError:
            print('That was not a valid number please try again.')
        add(num)
