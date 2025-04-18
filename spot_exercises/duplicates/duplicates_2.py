# Create a function that takes a string as an argument and returns a number
# representing occurrences of all letters and numbers that appears exactly
# twice,
# for example:

def count_duplic(string):
    count_list = []

    for char in string:
        if char.isalnum():
            if string.count(char) == 2 and char not in count_list:
                count_list.append(char)

    return len(count_list)

print(count_duplic('123123')) #; //=> 3
print(count_duplic('abcdea ab')) #; //=> 1
print(count_duplic('ab cd ea ab')) #; //=> 1
print(count_duplic('')) #; //=> 0

# PSEUDOCODE:
# SET counter_list
# LOOP through the characters of the string.
# If character is number or letter (.alnum()):
#   if character count is == 2 and character not in counter_list:
#       append character to counter list
#
# return len(counter_list)