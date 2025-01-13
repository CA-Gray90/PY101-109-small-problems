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
    step = -1 if start > end else 1

    for i in range(start, end + step, step):
        if i % 2 != 0:
            print(i)

def invalid_number(num):
    try:
        num = int(num)
    except ValueError:
        display('Invalid number, please enter a whole number.')
        return True
    return False

def try_again(response):
    while True:
        if response in ['y', 'Y']:
            display('Starting over...')
            return True
        if response in ['n', 'N']:
            return False
        display('Incorrect input, try again. y/n?')
        response = prompt()

# Program start
display('Welcome to the odd number printer.')
display('It will print all the odd numbers between two user chosen numbers')

while True:
    for element in ['starting', 'ending']:
        display(f'Enter the {element} number:')
        user_num = prompt()
        
        while invalid_number(user_num):
            user_num = prompt()
        
        if element == 'starting':
            start_num = int(user_num)
        else:
            end_num = int(user_num)

    if start_num == end_num:
        display('The numbers entered are the same. Try again.')
        continue

    display(f'The odd numbers between {start_num} and {end_num} are:')
    print_odd(start_num, end_num)

    display('Do another range of numbers? y/n')
    answer = prompt()
    if try_again(answer):
        continue
    display('Program end')
    break