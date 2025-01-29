# Build a program that asks the user to enter the length and width of a room,
# in meters, then prints the room's area in both square meters and square feet.

# PSEUDOCODE:
# - Welcome user, explain what the program does (finds area of room in metres
# and feet)
# - Ask user to enter length of room
# - Check for valid input
# - Ask user to enter width of room
# - Check for valid input
# - calculate area of room and return value in metres and feet
# - display result in metres and feet
# - Ask if user wishes to start again

def display(message):
    print(f'# {message}')

def prompt():
    return input('--> ')

def invalid_input(user_input):
    try:
        float(user_input)
    except ValueError:
        display('Invalid input, please enter a number.')
        return True
    if float(user_input) == 0.0:
        display("A measurement can't be 0! Try again.")
        return True
    return False

def check_metric(user_input):
    while True:
        if user_input.lower() in ['m', 'metres', 'meters', 'metre', 'meter']:
            return 'metres'
        if user_input.lower() in ['f', 'feet']:
            return 'feet'
        display("Invalid metric entered, try again."
                "'m' for metres, 'f' for feet.")
        user_input = prompt()

def calculate_area(length, width, metric):
    area = length * width
    if metric == 'metres':
        area_metres = area
        area_feet = area * 10.7639
        return (area_metres, area_feet)
    area_metres = area / 10.7639
    area_feet = area
    return (area_feet, area_metres)

def try_again(answer):
    while True:
        answer = answer.lower()
        if answer in ['n', 'no']:
            return False
        if answer in ['y', 'yes']:
            return True
        print('Invalid input, enter "y" or "n":')
        answer = prompt()

# Program Start #

display('Welcome to the Room Area Calculator!')
display('This program will calculate the area of a room in metres or feet.')

while True:
    display('Please specify if the measurement is in metres or feet: m/f')
    user_metric = prompt()
    user_metric = check_metric(user_metric)

    if user_metric == 'metres':
        other_metric = 'feet'
    else:
        other_metric = 'metres'

    display(f'Please enter the length of the room in '
            f'{user_metric}')
    room_length = prompt()

    while invalid_input(room_length):
        room_length = prompt()

    room_length = float(room_length)

    display('Please enter the width of the room in '
            f'{user_metric}')
    room_width = prompt()

    while invalid_input(room_width):
        room_width = prompt()

    room_width = float(room_width)

    area_metres_feet = calculate_area(room_length, room_width, user_metric)

    display(f'The area of the room in {user_metric} is: '
            f'{area_metres_feet[0]:.2f}')
    display(f'(or {area_metres_feet[1]:.2f} in {other_metric})')

    display('Do you wish to try again? y/n')
    user_answer = prompt()
    if try_again(user_answer):
        continue
    display('Program Terminated')
    break