# Given a string that consists of some words and an assortment of
# non-alphabetic characters, write a function that returns that string with all
# of the non-alphabetic characters replaced by spaces. If there are more than
# one space in a row, reduce it to just a single space

# PSEUDOCODE:
# Iterate through string:
#   IF char isalpha() returns True:
#       Concatenate charater to new string
#   ELSE add a space ' ' to new string
#   If multiple spaces in a row, then reduce it to one space only.
# Return new string

# Maybe a way to get just the words to a list, then join that list.

def clean_up(string):
    string_list = [char if char.isalpha() else ' ' for char in string]
    
    clean_string = ''.join(string_list)

    while True:
        if '  ' in clean_string:
            clean_string = clean_string.replace('  ', ' ')
        else:
            break    

    return clean_string

def clean_up(string):
    string_list = [char if char.isalpha() else ' ' for char in string]
    
    clean_string = ''.join(string_list)

    while '  ' in clean_string:
        clean_string = clean_string.replace('  ', ' ')

    return clean_string

# A solution similar to LS, checking if we are at the first index, or if the
# previous char was a space.

# Is there a way to make my solution more memory efficient using a list?

def clean_up(string):
    string_list = []

    for char in string:
        if char.isalpha():
            string_list.append(char)
        elif string_list == [] or string_list[-1] != ' ':     # [-1] is the last character/element in the sequence.
            string_list.append(' ')

    return ''.join(string_list)

print(clean_up("---what's my +*& line?") == " what s my line ")
# True