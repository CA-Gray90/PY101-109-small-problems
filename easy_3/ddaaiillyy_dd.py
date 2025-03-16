# Write a function that takes a string argument and returns a new string that
# contains the value of the original string with all consecutive duplicate
# characters collapsed into a single character.

# PSEUDOCODE:
# Take a string as input
# Initialize an empty string variable: new_string
# Take the first character of the input, check if the next character is the same
# IF the next character is the same as the previous, move to check the next char
# IF the next character is NOT the same as the previous, add that to new_string
# Once we have iterated through the input string, return the new string

# FORMAL PSEUDOCODE:
# GET string input as argument
# SET variable result to empty string ''
# FOR LOOP through each character of input string:
# First iteration;
# IF character == input string[0]:
#    SET a variable, previous_char to first char of input string
# On following iterations:
# IF current character != previous character:
#   new_string += current character
# ELSE:
#   continue
# once loop is finished, return new_string

# def crunch(string):
#     result = ''
#     index = 0

#     for char in string:
#         if index == 0:
#             previous_char = char
#             result += char
#             index += 1
#         else:
#             if previous_char != char:
#                 result += char
#                 previous_char = char
#     return result

def crunch(string):
    result = ''
    index = 0

    while index < len(string):
        if index == 0 or string[index] != string[index - 1]:
            result += string[index]
        index += 1

    return result

# Always check if you are repeating yourself, if you are, changes are that you
# can find a more concise way to write the code to avoid repetition.

# def crunch(string):
#     result = ''
#     index = 0

#     while index < len(string):
#         if index == len(string) - 1 or string[index] != string[index + 1]:
#                 result += string[index]
#         index += 1

#     return result

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')