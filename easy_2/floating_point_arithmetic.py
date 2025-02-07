# Write a program that prompts the user for two positive numbers
# (floating-point), then prints the results of the following operations on
# those two numbers: addition, subtraction, product, quotient, floor quotient,
# remainder, and power. 

OPERATION_DICT = {
    '+' : (lambda x, y: x + y),
    '-' : (lambda x, y: x - y),
    '*' : (lambda x, y: x * y),
    '/' : (lambda x, y: x / y),
    '//': (lambda x, y: x // y),
    '%' : (lambda x, y: x % y),
    '**': (lambda x, y: x**y)
}

def prompt(text):
    print(f'==> {text}')

def print_operation_results(num_1, num_2):
    for operator, operation in OPERATION_DICT.items():
        prompt(f'{num_1} {operator} {num_2} = {operation(num_1, num_2)}')

def main():
    prompt('Enter the first number:')
    user_num_1 = float(input())

    prompt('Enter the second number:')
    user_num_2 = float(input())

    print_operation_results(user_num_1, user_num_2)

main()

# LS Solution:

# def calculate(first, second, operator):
#     match operator:
#         case '+':  return first + second
#         case '-':  return first - second
#         case '*':  return first * second
#         case '/':  return first / second
#         case '//': return first // second
#         case '%':  return first % second
#         case '**': return first ** second

# first_float = float(input("==> Enter the first number:\n"))
# second_float = float(input("==> Enter the second number:\n"))
# for operator in ['+', '-', '*', '/', '//', '%', '**']:
#     operation = f"{first_float} {operator} {second_float}"
#     result = calculate(first_float, second_float, operator)
#     print(f"==> {operation} = {result}")

# Thier solution uses a match/case statement inside a function. 