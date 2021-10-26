
import argparse
import sys

def calculator(args):
    if num.num1 == 45 and num.num2 == 3 and num.num3 == '*':
        return "555"
    elif num.num1 == 56 and num.num2 == 9 and num.num3 == '+':
        return "77"
    elif num.num1 == 56 and num.num2 == 6 and num.num3 == '/':
        return "4"
    elif num.num3 == '*':
        num4 = num.num1 * num.num2
        return num4
    elif num.num3 == '+':
        plus = num.num2 + num.num1
        return plus
    elif num.num3 == '/':
        Dev =num.num2 / num.num1
        return Dev
    elif num.num3 == '-':
        Dev = num.num2 - num.num1
        return Dev
    elif num.num3 == '%':
        percent = num.num2 % num.num1
        return percent
    else:
       return("Error! Please check your input")

if __name__ == '__main__':
    calc= argparse.ArgumentParser()
    calc.add_argument('--num1', type=float, default=45.0,
                      help="Enter first number. This is a utility for calculation."
                           " Please contact harry bhai")

    calc.add_argument('--num2', type=float, default=3.0,
                      help="Enter second number. This is a utility for calculation. "
                           "Please contact harry bhai")

    calc.add_argument('--num3', type=str, default="*",
                      help="This is a utility for calculation."
                           " Please contact harry bhai for more")

    num = calc.parse_args()
    sys.stdout.write(str(calculator(num)))

