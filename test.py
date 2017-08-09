import calculator
import unittest
import logging
import pandas
import csv
import datetime
import sys




def test_add():

    test_case = [[1, 2], [0, 0], [-15, 10], [3.14, .001], ['a', 'b']]
    expected_result = [3, 0, -5, 3.141, 'Please enter a valid number']

    for i in range(len(expected_result)):
        if expected_result[i] == calculator.add(test_case[i]):
            logger.info('Add\nExpected: {}\nOutput: {}'.format(calculator.add(test_case[i]), expected_result[i]))
            print('Add\nExpected: {}\nOutput: {}'.format(calculator.add(test_case[i]), expected_result[i]))
            print('Pass\n')
        else:
            logger.info('Add\nExpected: {}\nOutput: {}'.format(calculator.add(test_case[i]), expected_result[i]))
            print('Add\nExpected: {}\nOutput: {}'.format(calculator.add(test_case[i]), expected_result[i]))
            print('Fail\n')



logging.basicConfig(filename='C:/Users/clkwa/PycharmProjects/RapidSOS_Assessment/calc_test.txt', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')
test_add()
logger = logging.getLogger()
