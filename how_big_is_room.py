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

def sq_metres_to_feet(sq_metres):
    return sq_metres * 10.7639

def invalid_input(user_input):
    try:
        float(user_input)
    except ValueError:
        print('Invalid input, please enter a number.')
        return True
    return False

def calculate_area(length, width):
    return length * width

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
display('This program will calculate the area of a room in metres and feet.')

while True:
    display('Please enter the length of the room in metres:')
    room_length = prompt()

    while invalid_input(room_length):
        room_length = prompt()

    room_length = float(room_length)

    display('Please enter the width of the room in metres:')
    room_width = prompt()

    while invalid_input(room_width):
        room_width = prompt()

    room_width = float(room_width)

    area_metres = calculate_area(room_length, room_width)
    area_feet = sq_metres_to_feet(area_metres)

    display(f'The area of the room in square metres is: {area_metres}')
    display(f'The area in square feet is: {area_feet}')

    display('Do you wish to try again? y/n')
    user_answer = prompt()
    if try_again(user_answer):
        continue
    display('Program Terminated')
    break

#TODO: Check is either value is zero and ask for input again for the
# corresponding required input.