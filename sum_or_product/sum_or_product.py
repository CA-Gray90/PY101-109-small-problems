def welcome():
    print('Welcome to the'
          ' "Sum or Product of Consecutive Integers" Calculator!')
    print()
    
def explanation():
    print('When prompted, please enter an integer greater than 0.\n'
          'You will then be asked whether you would like the result of the sum'
          ' of all the integers between 1 and your number, or the product.\n'
          "Let's begin!")
    print()

def get_number():
    print('Please now enter a number greater than 0:')
    user_number = input()
    while True:
        try:
            user_number = int(user_number)
            if user_number <= 0:
                raise ValueError
            break
        except ValueError:
            print('Please enter a whole number greater than 0:')
            user_number = input()
    return user_number

def get_operation():
    print("Enter 's' to get the sum, or 'p' to get the product:")
    operation = input().casefold()
    while True:
        if operation == 's':
            return 'sum'
        elif operation == 'p':
            return 'product'
        print("Please enter either 's' or 'p':")
        operation = input().casefold()

def sum_of_integers(number):
    return sum(range(1, number + 1))

def product_of_integers(number):
    x = 1
    for i in range(2, number + 1):
        x *= i
    return x

def show_result(result, operation, user_number):
    print(f'The {operation} of all integers between 1 and {user_number}'
          f' is {result}.')

def main():
    welcome()
    explanation()
    user_integer = get_number()
    user_operation = get_operation()

    if user_operation == 'sum':
        result = sum_of_integers(user_integer)
    else:
        result = product_of_integers(user_integer)

    show_result(result, user_operation, user_integer)

main()