# Write a program that asks for user's name, then greets the user. If the user
# appends a ! to their name, the computer will yell the greeting (print it
# using all uppercase).

# get user input (name)
# Check if user has appended `!` to thier name.
# if yes:
# print greeting 'HELLO `NAME`! WHY ARE WE YELLING?'
# if no:
# print 'Hello `name`.'

user_name = input('What is your name? ')

# if user_name[-1] == '!':
#     print(f'HELLO {user_name.upper()} WHY ARE WE YELLING?')
# else:
#     print(f'Hello {user_name.capitalize()}.')

# # Refactor

if user_name.endswith('!'):
    print(f'HELLO {user_name.upper()} WHY ARE WE YELLING?')
else:
    print(f'Hello {user_name.capitalize()}.')