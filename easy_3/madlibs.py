adjective_1 = input('Enter an adjective: ')
adjective_2 = input('Enter another adjective: ')
adjective_3 = input('Enter another adjective: ')
name = input('Enter a last name: ')
adjective_4 = input('Enter another adjective: ')
noun = input('Enter a plural noun: ')

sentence = (f'The {adjective_1} man entered the {adjective_2} building to'
            f' visit a {adjective_3} man. "Sit down Mr. {name},'
            f' can I interest you in any {adjective_4} {noun}?"')

print(sentence)