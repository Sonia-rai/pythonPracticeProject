import argparse
import sys

def faulty_calculator(num):
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
        Dev = num.num2 / num.num1
        return Dev
    elif num.num3 == '-':
        Dev = num.num2 - num.num1
        return Dev
    elif num.num3 == '%':
        percent = num.num2 % num.num1
        return percent
    else:
       return("Error! Please check your input")


if __name__=="__main__":
    calc=argparse.ArgumentParser()
    calc.add_argument('--num1', type=float, default=0.0,
                      help="Enter the first number .This is utility for calculation.PLease contact Sonia rai")

    calc.add_argument('--num2', type=float, default=0.0,
                      help="Enter Second number.This is a utility fpr calculation.please contact Sonia rai")

    calc.add_argument('--num3', type=str, default="+",
                      help="This is a utility for calculation.Please contact Sonia rai for more info")

    num=calc.parse_args()
    sys.stdout.write(str(faulty_calculator(num)))
