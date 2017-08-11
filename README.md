# RapidSOS_Assessment

## Introduction

This calculator will allow users to input two numbers and execute the following operations on them: 
* addition
* subtraction
* multiplication
* division
* square root
* mean
* power
* cosine 
* find the range between the two numbers

## Usage
You can run calculator.py in your favorite Python IDE or via command line by directing to the respective 
folder and typing 
```
python calculator.py
```
When you run the program, a welcome prompt will ask you to choose an operation from a list. Select the 
operation by entering the respective number and depending on the operation, the script will ask you one,
two, or multiple numbers to input. For operations that can take in multiple numbers, the script will ask you how
many numbers you would like to input and then repeat the input prompt until the number of inputs has been
met. 

### Things to note
* Entering a non-number will end the script and will ask the user to please try again.
* Square root of a number must be positive. Imaginary numbers are not allow.
* Floating point numbers are allowed

## Running test.py
test.py can be run using an IDE or via command line by directing to the respective folder and typing 
```
python -m unittest test.py 
```
Running test.py will output a test report csv file in the directory called "calc_test.py." The file will
contain the timestamp of when the test was ran, test case ID, Test Case, Actual Output, Expected Ouput, and
whether or not the test passed or failed.

## Author
William Kwan
