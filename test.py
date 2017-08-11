import csv
import datetime
import logging
import unittest
import calculator

with open('calc_test.csv', 'w') as csvfile:
    header = csv.writer(csvfile)
    header.writerow(['Time', 'Test Case-ID', 'Test Case', 'Actual Output', 'Expected Output', 'Pass/Fail'])


class TestClass(unittest.TestCase):
    def setUp(self):
        #change filename to change the log filename and directory
        logging.basicConfig(filename='C:/Users/clkwa/PycharmProjects/RapidSOS_Assessment/calc_test.csv',
                            filemode='a',
                            level=logging.DEBUG,
                            datefmt='%m-%d %H:%M',
                            format='%(asctime)s, %(message)s')

    def test_add(self):
        logger = logging.getLogger()
        test_case = [[1, 2], [0, 0], [-15, 10], [3.14, .001], ['a', 'b']]
        expected_result = [3, 0, -5, 3.141, None]

        for i in range(len(expected_result)):
            if expected_result[i] == calculator.add(test_case[i]):
                print('{} Add-{}\nTest Case: {}\nExpected: {}\nOutput: {}'.format(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                    i,
                    ' '.join((str(x) for x in test_case[i])),
                    calculator.add(test_case[i]),
                    expected_result[i]))
                print('Pass\n')
                logger.info('Add-{}, {}, {}, {}, Pass, '.format(
                    i,
                    ' '.join((str(x) for x in test_case[i])),
                    calculator.add(test_case[i]),
                    expected_result[i]))

            else:
                print('{} Add-{}\nTest Case: {}\nExpected: {}\nOutput: {}'.format(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                    i,
                    ' '.join((str(x) for x in test_case[i])),
                    calculator.add(test_case[i]),
                    expected_result[i]))
                logger.info('Add-{}, {}, {}, {}, Fail, '.format(
                    i,
                    ' '.join((str(x) for x in test_case[i])),
                    calculator.add(test_case[i]),
                    expected_result[i]))
                print('Fail\n')
        print('------------------------------------------')

    def test_subtract(self):
        logger = logging.getLogger()
        test_case = [[3, 2], [0, 1], [-15, 10], [321, .1], ['a', 'b']]
        expected_result = [1, -1, -25, 320.9, None]

        for i in range(len(expected_result)):
            if expected_result[i] == calculator.subtract(test_case[i]):
                print('{} Subtract-{}\nTest Case: {}\nExpected: {}\nOutput: {}'.format(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                    i,
                    test_case[i],
                    expected_result[i],
                    calculator.subtract(test_case[i])))
                print('Pass\n')
                logger.info('Subtract-{}, {}, {}, {}, Pass, '.format(
                    i,
                    ' '.join((str(x) for x in test_case[i])),
                    calculator.subtract(test_case[i]),
                    expected_result[i]))

            else:
                print('{} Subtract-{}\nTest Case: {}\nExpected: {}\nOutput: {}'.format(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                    i,
                    test_case[i],
                    expected_result[i],
                    calculator.subtract(test_case[i])))
                logger.info('Subtract-{}, {}, {}, {}, Fail, '.format(
                    i,
                    ' '.join((str(x) for x in test_case[i])),
                    calculator.subtract(test_case[i]),
                    expected_result[i]))
                print('Fail\n')
        print('------------------------------------------')

    def test_multiply(self):
        logger = logging.getLogger()
        test_case = [[3, 2], [0, 1], [-15, 10], [321, .1], ['a', 'b']]
        expected_result = [6, 0, -150, 32.1, None]

        for i in range(len(expected_result)):
            if expected_result[i] == calculator.multiply(test_case[i]):
                print('{} Multiply-{}\nTest Case: {}\nExpected: {}\nOutput: {}'.format(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                    i,
                    test_case[i],
                    expected_result[i],
                    calculator.multiply(test_case[i])))
                print('Pass\n')
                logger.info('Multiply-{}, {}, {}, {}, Pass, '.format(
                    i,
                    ' '.join((str(x) for x in test_case[i])),
                    calculator.multiply(test_case[i]),
                    expected_result[i]))

            else:
                print('{} Multiply-{}\nTest Case: {}\nExpected: {}\nOutput: {}'.format(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                    i,
                    test_case[i],
                    expected_result[i],
                    calculator.multiply(test_case[i])))
                logger.info('Multiply-{}, {}, {}, {}, Fail, '.format(
                    i,
                    ' '.join((str(x) for x in test_case[i])),
                    calculator.multiply(test_case[i]),
                    expected_result[i]))
                print('Fail\n')
        print('------------------------------------------')

    def test_divide(self):
        logger = logging.getLogger()
        test_case = [[3, 2], [1, 0], [-15, 10], [321, .1], ['a', 'b']]
        expected_result = [1.5, None, -1.5, 3210, None]

        for i in range(len(expected_result)):
            if expected_result[i] == calculator.divide(test_case[i]):
                print('{} Divide-{}\nTest Case: {}\nExpected: {}\nOutput: {}'.format(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                    i,
                    test_case[i],
                    expected_result[i],
                    calculator.divide(test_case[i])))
                print('Pass\n')
                logger.info('Divide-{}, {}, {}, {}, Pass, '.format(
                    i,
                    ' '.join((str(x) for x in test_case[i])),
                    calculator.divide(test_case[i]),
                    expected_result[i]))

            else:
                print('{} Divide-{}\nTest Case: {}\nExpected: {}\nOutput: {}'.format(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                    i,
                    test_case[i],
                    expected_result[i],
                    calculator.divide(test_case[i])))
                logger.info('Divide-{}, {}, {}, {}, Fail, '.format(
                    i,
                    ' '.join((str(x) for x in test_case[i])),
                    calculator.divide(test_case[i]),
                    expected_result[i]))
                print('Fail\n')
        print('------------------------------------------')

    def test_square_root(self):
        logger = logging.getLogger()
        test_case = [[4], [25], [2], [-1], ['a']]
        expected_result = [2, 5, 1.4142135623730951, None, None]

        for i in range(len(expected_result)):
            if expected_result[i] == calculator.square_root(test_case[i]):
                print('{} Square Root-{}\nTest Case: {}\nExpected: {}\nOutput: {}'.format(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                    i,
                    test_case[i],
                    expected_result[i],
                    calculator.square_root(test_case[i])))
                print('Pass\n')
                logger.info('Square Root-{}, {}, {}, {}, Pass, '.format(
                    i,
                    ' '.join((str(x) for x in test_case[i])),
                    calculator.square_root(test_case[i]),
                    expected_result[i]))

            else:
                print('{} Square Root-{}\nTest Case: {}\nExpected: {}\nOutput: {}'.format(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                    i,
                    test_case[i],
                    expected_result[i],
                    calculator.square_root(test_case[i])))
                logger.info('Square Root-{}, {}, {}, {}, Fail, '.format(
                    i,
                    ' '.join((str(x) for x in test_case[i])),
                    calculator.square_root(test_case[i]),
                    expected_result[i]))
                print('Fail\n')
        print('------------------------------------------')

    def test_mean(self):
        logger = logging.getLogger()
        test_case = [[1, 2, 3], [-1, 0.5, 6, 8], [0, 0, 0], [89, 23, 353, -275, 2278, 10], ['a', 'b']]
        expected_result = [2, 3.375, 0, 413, None]

        for i in range(len(expected_result)):
            if expected_result[i] == calculator.mean(test_case[i]):
                print('{} Mean-{}\nTest Case: {}\nExpected: {}\nOutput: {}'.format(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                    i,
                    test_case[i],
                    expected_result[i],
                    calculator.mean(test_case[i])))
                print('Pass\n')
                logger.info('Mean-{}, {}, {}, {}, Pass, '.format(
                    i,
                    ' '.join((str(x) for x in test_case[i])),
                    calculator.mean(test_case[i]),
                    expected_result[i]))

            else:
                print('{} Mean-{}\nTest Case: {}\nExpected: {}\nOutput: {}'.format(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                    i,
                    test_case[i],
                    expected_result[i],
                    calculator.mean(test_case[i])))
                logger.info('Mean-{}, {}, {}, {}, Fail, '.format(
                    i,
                    ' '.join((str(x) for x in test_case[i])),
                    calculator.mean(test_case[i]),
                    expected_result[i]))
                print('Fail\n')
        print('------------------------------------------')

    def test_power(self):
        logger = logging.getLogger()
        test_case = [[3, 2], [8, 0], [-15, 9], [4, -1], ['a', 'b']]
        expected_result = [9, 1, -38443359375, 0.25, None]

        for i in range(len(expected_result)):
            if expected_result[i] == calculator.power(test_case[i]):
                print('{} Power-{}\nTest Case: {}\nExpected: {}\nOutput: {}'.format(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                    i,
                    test_case[i],
                    expected_result[i],
                    calculator.power(test_case[i])))
                print('Pass\n')
                logger.info('Power-{}, {}, {}, {}, Pass, '.format(
                    i,
                    ' '.join((str(x) for x in test_case[i])),
                    calculator.power(test_case[i]),
                    expected_result[i]))

            else:
                print('{} Power-{}\nTest Case: {}\nExpected: {}\nOutput: {}'.format(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                    i,
                    test_case[i],
                    expected_result[i],
                    calculator.power(test_case[i])))
                logger.info('Power-{}, {}, {}, {}, Fail, '.format(
                    i,
                    ' '.join((str(x) for x in test_case[i])),
                    calculator.power(test_case[i]),
                    expected_result[i]))
                print('Fail\n')
        print('------------------------------------------')


if __name__ == '__main__':
    unittest.main()
