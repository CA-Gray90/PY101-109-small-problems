# Print all odd numbers from 1 - 99 inclusive with each number on a seperate
# line. Solve the problem by just iterating over the odd numbers.

# Pseudocode:
# - loop through a range of numbers from 1 - 99, going up by 2
# (for the odd numbers).
# - print out each number as we go up the range of numbers till we get to 99

# for i in range(1, 100, 2):
#     print(i)

# Further exploration: Consider adding a way for the user to specify the start
# and end numbers:

# Pseudocode:
# - Welcome the user, explain what the program will do
# - get a starting number from the user (`start`)
# - get a finishing number from the user (`finish`)
# - loop through a range of numbers from `start` - `finish`, going up by 2
# (for the odd numbers).
# - print out each number as we go up the range of numbers till we get to
# the finishing number
# - prompt the user asking whether they would like to do it again.

def display(text):
    print(f'# {text}')

def prompt():
    user_input = input('--> ')
    return user_input

def print_odd(start, end):
    for i in range(start, end + 1):
        if i % 2 != 0:
            print(i)

def check_number(num):
    try:
        num = int(num)
    except ValueError:
        return False
    return True

def try_again():
    while True:
        display('Do another range of numbers? y/n')
        answer = prompt()

        if answer in ['y', 'Y']:
            return True
        if answer in ['n', 'N']:
            return False
        display('Incorrect input')

# Program start
display('Welcome to the odd number printer.')
display('It will print all the odd numbers between two user chosen numbers')

while True:
    while True:
        display('Enter the starting number:')
        start_num = prompt()
        if not check_number(start_num):
            display('Please enter a whole number.')
            continue
        start_num = int(start_num)
        break

    while True:
        display('Enter the ending number:')
        end_num = prompt()
        if not check_number(end_num):
            display('Please enter a whole number.')
            continue
        end_num = int(end_num)
        break

    if start_num >= end_num:
        display('The numbers entered are not consecutive. Try again.')
        continue

    display(f'The odd numbers between {start_num} and {end_num} are:')
    print_odd(start_num, end_num)

    if try_again():
        continue
    display('Program end')
    break