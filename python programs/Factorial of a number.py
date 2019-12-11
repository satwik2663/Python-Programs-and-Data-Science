#Author: Satwik Kashyap
#This program finds the factorial of the specified numbers

def factorial(number):
    if number < 0:
        print('Invalid entry! Cannot find factorial of a negative number')
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

if __name__ == '__main__':
    userInput_number = int(input('Enter the Number to find the factorial of: '))
    print(factorial(userInput_number))
