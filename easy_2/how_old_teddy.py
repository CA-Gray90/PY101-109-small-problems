# Build a program that randomly generates and prints teddies age. 

import random

age = random.randrange(20, 101)
# print(f'Teddy is {age} years old!')
# print('Teddy is {} years old!'.format(age))

# Further exploration:

print('What is your name?')
name = input('==> ')

if not name or name.isspace():
    name = 'Teddy'
print(f'{name} is {age} years old!')

# def random_age(name='Teddy'):
#     age = random.randrange(20, 101)
#     print(f'{name} is {age} years old!')

# print('What is your name?')
# user_name = input('==> ')

# random_age()